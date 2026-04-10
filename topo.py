from mininet.topo import Topo

class MyTopo(Topo):
    def build(self):
        # Add hosts
        h1 = self.addHost('h1',resolvconf='')
        h2 = self.addHost('h2',resolvconf='')

        # Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # Add links
        self.addLink(h1, s1)
        self.addLink(s1, s2)   # Primary path
        self.addLink(s1, s3)   # Backup path start
        self.addLink(s3, s2)   # Backup path end
        self.addLink(s2, h2)

topos = {'mytopo': (lambda: MyTopo())}
