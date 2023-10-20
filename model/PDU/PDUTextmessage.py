from ServerNetwork import network
def server_message(message,callsign):
    data = f"#TMSERVER:{callsign}:{message}\r\n"
    print("发送消息：",data)
    network.send_data(data,callsign)