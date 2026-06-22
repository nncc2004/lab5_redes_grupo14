import sys

from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi


def topology():
    net = Mininet_wifi()

    info("*** Creating nodes\n")
    ap1 = net.addAccessPoint(
        'ap1',
        ssid='ap1-ssid',
        channel='5',
        position='1,1,0'
    )

    ap2 = net.addAccessPoint(
        'ap2',
        ssid='ap2-ssid',
        channel='5',
        position='1,2,0'
    )

    sta1 = net.addStation(
        'sta1',
        mac='00:00:00:00:00:01',
        position='2,2,0'
    )

    sta2 = net.addStation(
        'sta2',
        mac='00:00:00:00:00:02',
        position='3,3,0'
    )

    c1 = net.addController('c1')

    info("*** Configuring nodes\n")
    net.configureNodes()

    info("*** Associating Stations\n")
    net.addLink(ap1, ap2)

    info("*** Rendering\n")
    net.plotGraph(min_x=-100, min_y=-100, max_x=100, max_y=100)

    info("*** Mobility initialization\n")
    net.startMobility(time=0)
    net.mobility(sta1, 'start', time=1, position='2,2,0')
    net.mobility(sta1, 'stop', time=10, position='10,2,0')
    net.stopMobility(time=10)

    info("*** Initialize network\n")
    net.build()
    c1.start()
    ap1.start([c1])
    ap2.start([c1])

    info("*** Starting Mininet CLI\n")
    CLI(net)

    info("*** Closing\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology()
