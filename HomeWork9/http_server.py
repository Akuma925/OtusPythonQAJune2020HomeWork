# https://docs.python.org/3/library/socket.html
import socket

HOST = '127.0.0.1'                 # Symbolic name meaning all available interfaces
PORT = 8889              # Arbitrary non-privileged port
BUFFER_SIZE = 2048
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as so:
    so.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    so.bind((HOST, PORT))
    so.listen(10)
    data_list = list()
    while True:
        conn, addr = so.accept()
        print('Connect:', addr)
        data = conn.recv(BUFFER_SIZE)
        print("Got data:", data.decode("utf-8"))
        data_list.append(data.decode("utf-8"))
        text_resp = f"""<html>
                        <body>
                        <h2>Begin</h2>
                        <h3>{data_list}</h3>
                        <h2>End</h2>
                        </body>
                        </html>"""
        resp = bytes(f"""HTTP/1.1 200 OK\n Content-Length:{len(text_resp)}\n Connection: close\nContent-Type:
        text/html\n\n  {text_resp}>""", encoding="utf8")
        conn.send(resp)
        conn.close()
        print("ОТКЛЮЧЕНО:", addr, "\n")

