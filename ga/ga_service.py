import os, json, zmq, psycopg2

GA_PORT = int(os.getenv("GA_PORT","5560"))

PG_HOST = os.getenv("PG_HOST","postgres")
PG_DB   = os.getenv("PG_DB","biblioteca")
PG_USER = os.getenv("PG_USER","postgres")
PG_PWD  = os.getenv("PG_PASSWORD","postgres")
PG_PORT = int(os.getenv("PG_PORT","5432"))

def get_conn():
    return psycopg2.connect(
        host=PG_HOST, dbname=PG_DB, user=PG_USER, password=PG_PWD, port=PG_PORT
    )

ctx = zmq.Context()
rep = ctx.socket(zmq.REP)
rep.bind(f"tcp://0.0.0.0:{GA_PORT}")
print(f"[GA] Listening REP on 0.0.0.0:{GA_PORT}")

while True:
    raw = rep.recv_string()
    try:
        data = json.loads(raw)
        op   = data.get("op")      # "DEVO" | "RENO"
        pay  = data.get("payload", {})

        with get_conn() as conn:
            with conn.cursor() as cur:
                # aquí procesas DEVO y RENO igual que te mostré antes
                cur.execute(
                    "INSERT INTO operations_log(type, book_code, user_id, site_id, payload_json) VALUES (%s,%s,%s,%s,%s)",
                    (op, pay.get("book_code"), pay.get("user_id"), pay.get("site_id"), json.dumps(pay))
                )
                rep.send_string(f"OK: {op} persistida")
    except Exception as e:
        rep.send_string(f"ERROR: {e}")
