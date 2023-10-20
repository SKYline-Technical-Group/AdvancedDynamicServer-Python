from ServerNetwork import network
from geopy.distance import geodesic

def updataPilotPosition(tokens):
    print(tokens)

def Broadcast_location_Pilot(tokens):
    updataPilotPosition(tokens)
    for a in network.atc_list:
        if a["cid"] != tokens[0][1:]:
            if geodesic((a["latitude"], a["longitude"]), (float(tokens[5]),float(tokens[6])).nm <= a["visual_range"]):
                network.send_data(f"{tokens}\r\n",a["cid"])
    for p in network.pilot_list:
        if p["cid"] != tokens[0][1:]:
            if geodesic((p["latitude"], p["longitude"]), (float(tokens[5]), float(tokens[6])).nm <= p["visual_range"]):
                network.send_data(f"{tokens}\r\n",p["cid"])