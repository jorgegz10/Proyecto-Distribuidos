import zmq

context = zmq.Context()

# Socket REQ/REP para hablar con los PS
rep_socket = context.socket(zmq.REP)
rep_socket.bind("tcp://*:5555")

# Socket PUB para notificar a los Actores
pub_socket = context.socket(zmq.PUB)
pub_socket.bind("tcp://*:5556")

print("GestorCarga listo en puertos 5555 (REP) y 5556 (PUB)")

while True:
    # Espera solicitud de un PS
    message = rep_socket.recv_string()
    print(f"[GestorCarga] Recibido: {message}")

    # Identifica tipo de operación
    if message.startswith("DEVO"):
        pub_socket.send_string(message)
        rep_socket.send_string("OK: Devolución registrada")

    elif message.startswith("RENO"):
        pub_socket.send_string(message)
        rep_socket.send_string("OK: Renovación registrada")

    else:
        rep_socket.send_string("ERROR: Operación no reconocida")
