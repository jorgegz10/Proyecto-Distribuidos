import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://gestor_carga:5556")
socket.setsockopt_string(zmq.SUBSCRIBE, "RENO")

print("ActorRenovacion escuchando eventos RENO...")

while True:
    msg = socket.recv_string()
    print(f"[ActorRenovacion] Procesando: {msg}")
