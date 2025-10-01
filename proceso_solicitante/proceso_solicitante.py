import os
import time
import zmq

GC_HOST = os.getenv("GC_HOST", "127.0.0.1")    # <- IP de PC-A
GC_REP_PORT = int(os.getenv("GC_REP_PORT", "5555"))
ARCHIVO = os.getenv("SOLICITUDES", "solicitudes.txt")

context = zmq.Context()
req = context.socket(zmq.REQ)
req.connect(f"tcp://{GC_HOST}:{GC_REP_PORT}")

print(f"[PS] Conectado a tcp://{GC_HOST}:{GC_REP_PORT}")

with open(ARCHIVO, "r", encoding="utf-8") as f:
    for linea in f:
        linea = linea.strip()
        if not linea or linea.startswith("#"):
            continue
        t0 = time.time()
        req.send_string(linea)
        resp = req.recv_string()
        t1 = time.time()
        print(f"[PS] {linea} -> {resp} ({(t1-t0)*1000:.2f} ms)")
        time.sleep(0.3) # Para no saturar el GC
print("[PS] Terminado")
