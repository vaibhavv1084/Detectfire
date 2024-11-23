import socket

import os

HOST '172.26.156.196'

PORT=56

file_counter 0

with socket.socket(socket.AF_INET, socket.SOCK STREAM) as server_socket:

   server_socket.bind((HOST, PORT))

   server_socket.listen()

   print(f"Server listening on [HOST): (PORT)")

   while True:

    conn, addr server_socket.accept()

    print(f"Connected to (addr)")

    try:

      filename = conn.recv(1024).decode()

      if filename.endswith('.exe'):

         with open(filename, 'rb') as f:

          file_dataf.read()

        conn.sendall(file_data)

        print(f"Sent (filename) to the client.")

        file_counter1

        if file_counter>-2:

            print("Served 2.exe files. Closing the server.")
            break

      else:

         conn.sendall(b"File not found or not an executable.")

         print(f"Requested file '(filename)' not found or not an executable.")

  except Exception as e:

    print(f"Error: (e)")

  finally:

    conn.close()