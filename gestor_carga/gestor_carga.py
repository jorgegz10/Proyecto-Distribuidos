import os
import time
import zmq

GC_REP_PORT = int(os.getenv("GC_REP_PORT", "5555"))
GC_PUB_PORT = int(os.getenv("GC_PUB_PORT", "5556"))

context = zmq.Context()

# Socket REQ/REP para hablar con PS
rep_socket = context.socket(zmq.REP)

# Bind a TODAS las interfaces (clave para máquinas distintas)
rep_socket.bind(f"tcp://0.0.0.0:{GC_REP_PORT}")

# Socket PUB para notificar a los Actores
pub_socket = context.socket(zmq.PUB)

# Opcional: subir HWM para no bloquear en picos
pub_socket.set_hwm(10000)
pub_socket.bind(f"tcp://0.0.0.0:{GC_PUB_PORT}")

print(f"GestorCarga listo en puertos {GC_REP_PORT} (REP) y {GC_PUB_PORT} (PUB)")

time.sleep(1.0)

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
