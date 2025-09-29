import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://gestor_carga:5556")
socket.setsockopt_string(zmq.SUBSCRIBE, "DEVO")

print("ActorDevolucion escuchando eventos DEVO...")

while True:
    msg = socket.recv_string()
    print(f"[ActorDevolucion] Procesando: {msg}")
