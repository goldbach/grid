import os
import zmq

broker = 'tcp://localhost:7000'

context = zmq.Context()
socket  = context.socket(zmq.REQ)

socket.setsockopt(zmq.IDENTITY, "fly")
socket.connect(broker)

socket.send("please, what is answer")
print "Reply from broker/worker", 
print socket.recv()
