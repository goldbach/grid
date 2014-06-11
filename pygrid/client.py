import os
import zmq

broker = 'tcp://localhost:7000'

context = zmq.Context()
socket  = context.socket(zmq.REQ)
socket.connect(broker)


msg = 'hello'

