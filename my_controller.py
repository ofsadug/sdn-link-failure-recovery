from pox.core import core
import pox.openflow.libopenflow_01 as of
import logging

logging.getLogger("packet").setLevel(logging.CRITICAL)
log = core.getLogger()

mac_to_port = {}
seen_packets = set()


def _handle_ConnectionUp(event):
    dpid = event.dpid
    log.info("Switch %s connected", dpid)
    mac_to_port[dpid] = {}


def _handle_PacketIn(event):
    packet = event.parsed
    if not packet.parsed:
        return

    dpid = event.dpid
    in_port = event.port

    src = packet.src
    dst = packet.dst

    # Ignore IPv6 multicast
    if str(dst).startswith("33:33"):
        return

    # Print once
    key = (str(src), str(dst))
    if key not in seen_packets:
        seen_packets.add(key)
        print("\n" + "="*40)
        print("📡 FLOW")
        print(f"SRC: {src}")
        print(f"DST: {dst}")
        print("="*40)

    # Learn source
    mac_to_port[dpid][src] = in_port

    # Decide port
    if dst in mac_to_port[dpid]:
        out_port = mac_to_port[dpid][dst]

        # ✅ Install forward flow
        flow = of.ofp_flow_mod()
        flow.match.dl_src = src
        flow.match.dl_dst = dst
        flow.actions.append(of.ofp_action_output(port=out_port))
        event.connection.send(flow)

        # ✅ Install reverse flow (CRITICAL FIX)
        rev = of.ofp_flow_mod()
        rev.match.dl_src = dst
        rev.match.dl_dst = src
        rev.actions.append(of.ofp_action_output(port=in_port))
        event.connection.send(rev)

    else:
        out_port = of.OFPP_FLOOD

    # Always send packet
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=out_port))
    msg.in_port = in_port
    event.connection.send(msg)


def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
