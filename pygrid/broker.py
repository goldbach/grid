import os
import zmq

print zmq.zmq_version()

clients_url = 'tcp://*:7000'
workers_url = 'tcp://*:7001'

context = zmq.Context()
client  = context.socket(zmq.ROUTER) # XREP
worker  = context.socket(zmq.ROUTER) # XREQ 

poller = zmq.Poller()
poller.register(client, zmq.POLLIN)
poller.register(worker, zmq.POLLIN)

client.bind(clients_url)
worker.bind(workers_url)

# zmq.device(zmq.QUEUE, client, worker)

lru = []

while True:
    
    socks = dict(poller.poll())
    if client in socks and socks[client] == zmq.POLLIN:
        address, empty, msg = client.recv_multipart()
        print "client req from", address
        print "lru q is", lru
        if len(lru) > 0:
            wrk = lru.pop()
            print "sending req to worker", wrk
            worker.send_multipart([wrk, '', msg])
        
    if worker in socks and socks[worker] == zmq.POLLIN:
        print "new worker",
        address, empty, msg = worker.recv_multipart()
        lru.append(address)
        if msg == "give me work":
            print "initial worker", address
        else:
            print "result from worker", address, msg



    
    
