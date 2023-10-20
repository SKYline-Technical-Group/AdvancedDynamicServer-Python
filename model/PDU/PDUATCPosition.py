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
    network.atc_list[callsign] = atc_data


def Broadcast_location_ATC(tokens):
    updataATCPosition(tokens)
    for a in network.atc_list:
        if a["cid"] != tokens[0][1:]:
            if geodesic((a["latitude"], a["longitude"]), (float(tokens[5]),float(tokens[6])).nm <= a["visual_range"]):
                network.send_data(f"{tokens}\r\n",a["cid"])
    for p in network.pilot_list:
        if p["cid"] != tokens[0][1:]:
            if geodesic((p["latitude"], p["longitude"]), (float(tokens[5]), float(tokens[6])).nm <= p["visual_range"]):
                network.send_data(f"{tokens}\r\n",p["cid"])
