from pyp2p.net import *

#Setup Bob's p2p node.
no3 = Net(passive_bind="192.168.1.12", passive_port=44446, interface="eth0:1", node_type="passive", debug=1)
no3.start()
no3.bootstrap()
no3.advertise()

#Event loop.
while 1:
    for con in no3:
        con.send_line("test")

    time.sleep(1)