import os
import zmq

print zmq.zmq_version()

clients_url = 'tcp://*:7000'
workers_url = 'tcp://*:7001'

context = zmq.Context()
client  = context.socket(zmq.XREP)
worker  = context.socket(zmq.XREQ)

poller = zmq.Poller()
poller.register(client, zmq.POLLIN)
poller.register(worker, zmq.POLLIN)

client.bind(clients_url)
worker.bind(workers_url)

# zmq.device(zmq.QUEUE, client, worker)

while True:
    
    socks = dict(poller.poll())
    if client in socks and socks[client] == zmq.POLLIN:
        print "new client",
        msg = client.recv_multipart()
        print msg
        worker.send_multipart(msg)
        
    if worker in socks and socks[worker] == zmq.POLLIN:
        print "new worker",
        msg = worker.recv_multipart()
        print msg
        client.send_multipart(msg)

    
    
