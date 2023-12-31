import socket
import threading
import time

from model.Server import base_data
oldclients = {}
newclients = {}
atc_list = {}
pilot_list = {}
flight_plan = {}

#删除异常连接
def Delete_the_abnormal_connection(client_socket, client_address):
    client_socket.close()
    try:
        del oldclients[client_address]
    except:
        pass
    for i in newclients:
        if newclients[i] == client_socket:
            del newclients[i]
            try:
                del pilot_list[i]
            except:
                pass
            try:
                del flight_plan[i]
            except:
                pass
            try:
                del atc_list[i]
            except:
                pass
            break

def handle_client(client_socket, client_address):
    # 接收客户端发送的数据
    while True:
        try:
            data = client_socket.recv(1024)
        # 处理接收到的数据
            if not data:
                pass
            try:
                data = data.decode('utf-8')
            except:
                continue
            threading.Thread(target=base_data.split_data(data,client_address)).start()
        except:
            Delete_the_abnormal_connection(client_socket, client_address)


def send_data(data, client_address):
    if client_address in newclients:
        # 假设客户端地址为唯一标识符
        dest_client = newclients[client_address]
        dest_client.sendall(data.encode('utf-8')+"\r\n".encode('utf-8'))

def Adduser_pool(callsign,client_address):
    print("添加用户到连接池",callsign)
    newclients[callsign] = oldclients[client_address]

def Disconnect_pool(callsign):
    time.sleep(1)
    newclients[callsign].close()
    try:
        del oldclients[callsign]
    except:
        pass
    try:
        del newclients[callsign]
    except:
        pass
    try:
        del pilot_list[callsign]
    except:
        pass
    try:
        del flight_plan[callsign]
    except:
        pass
    try:
        del atc_list[callsign]
    except:
        pass
    for i in oldclients:
        if oldclients[i] == newclients[callsign]:
            del oldclients[i]
            break
    print("删除用户连接池",callsign)


def Disconnect_Native_pools(address):
    time.sleep(1)
    oldclients[address].close()
    del oldclients[address]

def Native_send_data(data,client_address):
    if client_address in oldclients:
        # 假设客户端地址为唯一标识符
        dest_client = oldclients[client_address]
        dest_client.sendall(data.encode('utf-8'))
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