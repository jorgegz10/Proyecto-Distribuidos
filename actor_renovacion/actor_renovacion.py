import os
import zmq

GC_HOST = os.getenv("GC_HOST", "127.0.0.1")
GC_PUB_PORT = int(os.getenv("GC_PUB_PORT", "5556"))

context = zmq.Context()
sub = context.socket(zmq.SUB)
sub.connect(f"tcp://{GC_HOST}:{GC_PUB_PORT}")
sub.setsockopt_string(zmq.SUBSCRIBE, "RENO")

print(f"[ActorRenovacion] SUB a tcp://{GC_HOST}:{GC_PUB_PORT} (topic=RENO)")

while True:
    msg = sub.recv_string()
    print(f"[ActorRenovacion] {msg}")
