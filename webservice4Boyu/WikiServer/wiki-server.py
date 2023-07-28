#!/usr/bin/env python3
import wikipediaapi
import socket
import json

HOST = "127.0.0.1"
PORT = 65432

# Receives connection data, send to wikipediaapi and returns summary value to requester
def handle_client(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        query = data.decode('utf-8')
        wiki_wiki = wikipediaapi.Wikipedia('youraddress@oregonstate.edu')
        page = wiki_wiki.page(query)
        if page.exists():
            retdata = "Summary: {}\n".format(page.summary)
        else:
            retdata = "Page not found.\n"

        conn.sendall(retdata.encode('utf-8'))
        print(f"Message received: {data.decode('utf-8')!r}")

    conn.close()

# opens the socket for listening
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server started, listening for connections...")
    while True:
        conn, addr = s.accept()  #if connection, accept it and send to handle_client for handling
        print(f"Connected by {addr}")
        handle_client(conn)
