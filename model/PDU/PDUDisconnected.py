from ServerNetwork import network
def Userdisconnected(tokens):
    callsign = tokens[0][3:]
    if "#DA" in tokens[0]:
        print(f"ATC:{callsign}断开连接")
        del network.atc_list[callsign]
    if "$DP" in tokens[0]:
        print(f"飞行员:{callsign}断开连接")
        del network.pilot_list[callsign]
    network.Disconnect_pool(callsign)


