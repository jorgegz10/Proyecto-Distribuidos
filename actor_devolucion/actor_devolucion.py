import os
import zmq

GC_HOST = os.getenv("GC_HOST", "127.0.0.1")    # <- IP de PC-A si corre fuera de docker
GC_PUB_PORT = int(os.getenv("GC_PUB_PORT", "5556"))

context = zmq.Context()
sub = context.socket(zmq.SUB)
sub.connect(f"tcp://{GC_HOST}:{GC_PUB_PORT}")
sub.setsockopt_string(zmq.SUBSCRIBE, "DEVO")

print(f"[ActorDevolucion] SUB a tcp://{GC_HOST}:{GC_PUB_PORT} (topic=DEVO)")

while True:
    msg = sub.recv_string()
    # msg ejemplo: "DEVO book=BK001 user=u01 ..."
    print(f"[ActorDevolucion] {msg}")
