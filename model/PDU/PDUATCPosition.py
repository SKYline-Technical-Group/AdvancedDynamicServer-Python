from ServerNetwork import network

def updataATCPosition(tokens):
    callsign = tokens[0][1:]
    frequency = tokens[1]
    frequency = f"1{frequency[0:2]}.{frequency[2:]}"
    atc_data = network.atc_list[callsign]
    atc_data["facility"] = tokens[2]
    atc_data["frequency"] = frequency
    atc_data["visual_range"] = tokens[3]
    network.atc_list[callsign] = atc_data