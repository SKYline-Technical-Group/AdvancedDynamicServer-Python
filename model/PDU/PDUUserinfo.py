from ServerNetwork import network



def server_message(tokens):
    callsign = tokens[0][3:]
    if tokens[2] == "ATC":
        data = f"$CRSERVER:{callsign}:ATC:Y:{callsign}"
        network.send_data(data,callsign)
        return
    if tokens[2] == "FP":
        data = f"{network.flight_plan[tokens[-1]]['raw_data']}\r\n"
        network.send_data(data,callsign)
        return

def Get_information(tokens,raw_data):
    to = tokens[1]
    if to == "SERVER":
        server_message(tokens)
        return
    network.send_data(raw_data,to)


def Recover_information(tokens,raw_data):
    to = tokens[1]
    network.send_data(raw_data,to)