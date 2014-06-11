import os
import zmq
import time

broker_url = 'tcp://localhost:7001'

ctx = zmq.Context()
broker = ctx.socket(zmq.REP)
broker.connect(broker_url)

while True:
    cmd = broker.recv()
    print "command is", cmd
    print "doing heavy work"
    time.sleep(2)
    broker.send("result is 42")
    