import socket
import threading
from model.Server import base_data
oldclients = {}
newclients = {}
atc_list = {}
pilot_list = {}
def handle_client(client_socket, client_address):
    # 接收客户端发送的数据
    while True:
        data = client_socket.recv(1024)
        # 处理接收到的数据
        if not data:
            pass
        data = data.decode('utf-8')
        threading.Thread(target=base_data.split_data(data,client_address)).start()

def send_data(data, client_address):
    if client_address in newclients:
        # 假设客户端地址为唯一标识符
        dest_client = newclients[client_address]
        dest_client.sendall(data.encode('utf-8'))
        print(f"向 {client_address} 发送消息：{data}")

def Adduser_pool(callsign,client_address):
    print("添加用户到连接池",callsign)
    newclients[callsign] = oldclients[client_address]
def Deluser_pool(callsign):
    del newclients[callsign]
def main(ip_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(ip_port)
    server_socket.listen(5)

    print("Server listening on port 6809...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connected with {client_address}")
        # 为每个连接的客户端创建一个单独的线程
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()
        # 存储客户端连接信息
        oldclients[client_address] = client_socket