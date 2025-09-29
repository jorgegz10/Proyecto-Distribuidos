import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://gestor_carga:5555")

print("ProcesoSolicitante conectado al GestorCarga")

with open("solicitudes.txt", "r") as f:
    for linea in f:
        solicitud = linea.strip()
        if not solicitud:
            continue

        print(f"[PS] Enviando: {solicitud}")
        socket.send_string(solicitud)

        # Espera respuesta inmediata (síncrona)
        respuesta = socket.recv_string()
        print(f"[PS] Respuesta: {respuesta}")
        time.sleep(2)  # Simula tiempo entre solicitudes
