from ServerNetwork import network
from geopy.distance import geodesic

def updataPilotPosition(tokens):
    pilotdata = network.pilot_list[tokens[1]]
    pilotdata["latitude"] = float(tokens[4])
    pilotdata["longitude"] = float(tokens[5])
    pilotdata["altitude"] = float(tokens[6])
    pilotdata["ground_speed"] = float(tokens[7])
    pilotdata["Squawk"] = float(tokens[2])
    network.pilot_list[tokens[1]] = pilotdata

def Broadcast_location_Pilot(tokens,raw_data):
    updataPilotPosition(tokens)
    for a in network.atc_list:
        a = network.atc_list[a]
        if a["callsign"] != tokens[1]:
            nm = geodesic((float(a["latitude"]), float(a["longitude"])), (float(tokens[4]), float(tokens[5]))).nm
            if int(nm) <= int(a["visual_range"]):
                network.send_data(f"{raw_data}\r\n", a["callsign"])
    for p in network.pilot_list:
        p = network.pilot_list[p]
        if p["callsign"] != tokens[1]:
            if geodesic((float(p["latitude"]), float(p["longitude"])), (float(tokens[4]), float(tokens[5]))).nm <= p["visual_range"]:
                network.send_data(f"{raw_data}\r\n", p["callsign"])