import socket

target_host = "www.google.com"
target_port = 80

#create a socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #AF_INET parameter indicates that we'll use an IPv4 address, SOCK_STREAM indicates its a TCP client

#connect the client to the server

client.connect((target_host, target_port))

#send some data

client.send(b"GET / HTTP/1.1\ r\nHost: google.com \r\n\r\n")

#recieve some data

response = client.recv(4096)

print(response.decode())

client.close()
