import os
import zmq
import time
import sys

broker_url = 'tcp://localhost:7001'

wid = sys.argv[1]

ctx = zmq.Context()
broker = ctx.socket(zmq.REQ)
broker.setsockopt(zmq.IDENTITY, wid)
broker.connect(broker_url)

       
broker.send("give me work")
while True:
    cmd = broker.recv()
    print wid, "doing heavy work"
    time.sleep(2)
    broker.send("result is 42 - give me more work")
    
    