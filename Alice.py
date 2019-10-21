
from pyp2p.net import *
import time

#Setup Alice's p2p node.
no1 = Net(passive_bind="192.168.1.11", passive_port=44444, interface="eth0:2", node_type="passive", debug=1)
no1.start()
no1.bootstrap()
no1.advertise()

#Event loop.
while 1:
    for con in no1:
        for reply in con:
            print(reply)

    time.sleep(1)