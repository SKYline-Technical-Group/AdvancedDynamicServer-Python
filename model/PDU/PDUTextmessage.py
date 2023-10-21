from ServerNetwork import network
from geopy.distance import geodesic
def server_message(message,callsign):
    data = f"#TMSERVER:{callsign}:{message}\r\n"
    print("发送消息：",data)
    network.send_data(data,callsign)

def err_server_message(message,address,callsign):
    data = f"#TMSERVER:{callsign}:{message}\r\n"
    print("发送消息：",data)
    network.Native_send_data(data,address)
def atc_message(raw_data):
    for a in network.atc_list:
        network.send_data(f"{raw_data}\r\n",a)
def broadcast(raw_data):
    for p in network.newclients:
        network.send_data(f"{raw_data}\r\n",p)
def wallop(raw_data):
    for p in network.atc_list:
        p = network.atc_list[p]
        if p["rating"] >= "11":
            network.send_data(f"{raw_data}\r\n",p)
def server_user(tokens):
    callsign = tokens[0][3:]
    if tokens[2] == "FP":
        data = f"{network.flight_plan[tokens[-1]]['raw_data']}\r\n"
        network.send_data(data, callsign)
        return
def Send_to_users_in_scope(tokens,raw_data):
    callsign = tokens[0][3:]
    userdata = network.pilot_list[callsign]
    for a in network.atc_list:
        a = network.atc_list[a]
        if a["callsign"] != userdata["callsign"]:
            nm = geodesic((float(a["latitude"]), float(a["longitude"])),
                          (float(userdata["latitude"]), float(userdata["longitude"]))).nm
            if int(nm) <= int(a["visual_range"]):
                network.send_data(f"{raw_data}\r\n", a["callsign"])
    for p in network.pilot_list:
        p = network.pilot_list[p]
        if p["callsign"] != userdata["callsign"]:
            if geodesic((float(p["latitude"]), float(p["longitude"])),
                        (float(userdata["latitude"]), float(userdata["longitude"]))).nm <= p["visual_range"]:
                network.send_data(f"{raw_data}\r\n", p["callsign"])
def Private_chat(tokens,raw_data):
    to = tokens[1]
    if to == "SERVER":
        server_user(tokens)
        return
    if to == "@49999":
        atc_message(raw_data)
        return
    if to == "*":
        broadcast(raw_data)
        return
    if to == "*S":
        wallop(raw_data)
        return
    if to == "@94835":
        Send_to_users_in_scope(tokens,raw_data)
        return
    network.send_data(f"{raw_data}\r\n",to)