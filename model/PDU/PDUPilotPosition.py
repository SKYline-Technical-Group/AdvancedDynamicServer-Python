from ServerNetwork import network
from geopy.distance import geodesic
def unpack_pitch_bank_heading(pbh):
    # 从整数中获取pitch值
    pitch_int = pbh >> 22

    # 将pitch转换为浮点数
    pitch = float(pitch_int) / 1024.0 * -360.0
    if pitch > 180.0:
        pitch -= 360.0
    elif pitch <= -180.0:
        pitch += 360.0

    # 从整数中获取bank值
    bank_int = (pbh >> 12) & 0x3FF
    # 将bank转换为浮点数
    bank = float(bank_int) / 1024.0 * -360.0
    if bank > 180.0:
        bank -= 360.0
    elif bank <= -180.0:
        bank += 360.0

    # 从整数中获取heading值
    hdg_int = (pbh >> 2) & 0x3FF
    # 将heading转换为浮点数
    heading = float(hdg_int) / 1024.0 * 360.0
    if heading < 0.0:
        heading += 360.0
    elif heading >= 360.0:
        heading -= 360.0

    return [pitch, bank, heading]


def pack_pitch_bank_heading(pitch, bank, heading):
    # 计算pitch的整数值
    p = pitch / -360.0
    if p < 0:
        p += 1.0
    p *= 1024.0

    # 计算bank的整数值
    b = bank / -360.0
    if b < 0:
        b += 1.0
    b *= 1024.0

    # 计算heading的整数值
    h = heading / 360.0 * 1024.0

    # 组合整数值并返回
    return int(p) << 22 | int(b) << 12 | int(h) << 2


def updataPilotPosition(tokens):
    unpacked_values = unpack_pitch_bank_heading(int(tokens[-2]))
    pilotdata = network.pilot_list[tokens[1]]
    pilotdata["latitude"] = float(tokens[4])
    pilotdata["longitude"] = float(tokens[5])
    pilotdata["altitude"] = float(tokens[6])
    pilotdata["ground_speed"] = float(tokens[7])
    pilotdata["Squawk"] = float(tokens[2])
    pilotdata["heading"] = unpacked_values[-1]
    pilotdata["pitch"] = unpacked_values[0]
    pilotdata["bank"] = unpacked_values[1]
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