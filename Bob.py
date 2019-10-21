from pyp2p.net import *

#Setup Bob's p2p node.
no2 = Net(passive_bind="192.168.1.12", passive_port=44445, interface="eth0:1", node_type="passive", debug=1)
no2.start()
no2.bootstrap()
no2.advertise()

#Event loop.
while 1:
    for con in no2:
        con.send_line("test")

    time.sleep(1)