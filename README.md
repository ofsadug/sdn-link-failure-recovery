# sdn-link-failure-recovery
Name:Apurv Kumar Singh
SRN:PES1UG24CS077

# 🔗 Link Failure Detection and Recovery using SDN (Mininet + POX)

## 📌 Problem Statement

The objective of this project is to **detect link failures in a network and dynamically update routing to restore connectivity** using Software Defined Networking (SDN).

---

## 🎯 Objectives

* Monitor network topology
* Simulate link failures
* Update flow rules dynamically
* Restore connectivity using alternate paths

---

## 🧠 Concepts Used

* Software Defined Networking (SDN)
* OpenFlow Protocol
* POX Controller
* Mininet Network Emulator
* Flow Tables & Match-Action Rules
* Spanning Tree Protocol (STP)

---

## 🏗️ Network Topology

```
h1 --- s1 ------- s2 --- h2
        \       /
          \   /
            s3
```

* **Primary Path:** h1 → s1 → s2 → h2
* **Backup Path:** h1 → s1 → s3 → s2 → h2

---

## ⚙️ Tools & Technologies

* Mininet
* POX Controller
* Open vSwitch
* Python (for controller logic)

---

## 🚀 How to Run the Project

### 1️⃣ Start Controller

```bash
cd ~/pox
./pox.py log.level --INFO openflow.discovery openflow.spanning_tree my_controller
```

---

### 2️⃣ Start Mininet

```bash
sudo mn -c
sudo mn --custom topo.py --topo mytopo --controller=remote
```

---

### 3️⃣ Verify Topology

```bash
net
```

---

### 4️⃣ Test Connectivity

```bash
pingall
```

---

## 💣 Failure Simulation

### 🔴 Break Link

```bash
link s1 s2 down
```

---

### 🔍 Observe Failure

```bash
pingall
```

---

## 🔄 Recovery Mechanism

### Clear Flow Rules

```bash
sh ovs-ofctl del-flows s1
sh ovs-ofctl del-flows s2
sh ovs-ofctl del-flows s3
```

---

### Test Recovery

```bash
pingall
```

---

## 📊 Observations

| Scenario           | Result                   |
| ------------------ | ------------------------ |
| Normal operation   | Successful communication |
| After link failure | Packet loss observed     |
| After flow reset   | Connectivity restored    |

---

## 🧠 Working Explanation

* The controller installs flow rules based on incoming packets.
* When a link fails, existing flow rules become invalid.
* By clearing flow tables, switches send new packets to the controller.
* The controller installs updated rules using an alternate path.

---

## 💡 Key Features

* Custom SDN controller implementation
* Redundant topology for failover
* Flow rule-based routing
* Link failure simulation and recovery

---

## ⚠️ Limitations

* Recovery is semi-dynamic (manual flow reset required)
* No automatic topology event handling

---

## 🚀 Future Improvements

* Automatic failure detection using topology events
* Dynamic rerouting without manual intervention
* Integration with advanced SDN controllers (Ryu)

---

## 📸 Screenshots

Screenshots demonstrating:

* Topology setup
* Ping results
* Flow tables
* Link failure
* Recovery

(Refer to `/screenshots` folder)

---

## 🧠 Viva Notes

* SDN separates control plane and data plane
* Controller manages network behavior centrally
* Flow rules define packet forwarding
* Link failure disrupts routing until flows are updated

---

## 🎯 Conclusion

This project demonstrates how SDN enables **programmable, flexible, and adaptive networking**, allowing efficient recovery from failures compared to traditional static networks.

---
