from ServerNetwork import network
from geopy.distance import geodesic
def updataATCPosition(tokens):
    callsign = tokens[0][1:]
    frequency = tokens[1]
    frequency = f"1{frequency[0:2]}.{frequency[2:]}"
    atc_data = network.atc_list[callsign]
    atc_data["facility"] = tokens[2]
    atc_data["frequency"] = frequency
    atc_data["visual_range"] = tokens[3]
    atc_data["latitude"] = tokens[5]
    atc_data["longitude"] = tokens[6]
    network.atc_list[callsign] = atc_data


def Broadcast_location_ATC(tokens, raw_data):
    updataATCPosition(tokens)
    for a in network.atc_list:
        a = network.atc_list[a]
        if a["callsign"] != tokens[0][1:]:
            nm = geodesic((float(a["latitude"]), float(a["longitude"])), (float(tokens[5]), float(tokens[6]))).nm
            if int(nm) <= int(a["visual_range"]):
                network.send_data(f"{raw_data}\r\n", a["callsign"])
    for p in network.pilot_list:
        p = network.pilot_list[p]
        if p["callsign"] != tokens[0][1:]:
            if geodesic((p["latitude"], p["longitude"]), (float(tokens[5]), float(tokens[6]))).nm <= p["visual_range"]:
                network.send_data(f"{raw_data}\r\n", p["callsign"])
