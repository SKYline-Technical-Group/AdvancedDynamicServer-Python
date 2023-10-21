from ServerNetwork import network
from geopy.distance import geodesic
def Judge_the_distance(callsign):
    userdata = network.pilot_list[callsign]
    raw_data = network.flight_plan[callsign]["raw_data"]
    for a in network.atc_list:
        a = network.atc_list[a]
        if a["callsign"] != userdata["callsign"]:
            nm = geodesic((float(a["latitude"]), float(a["longitude"])), (float(userdata["latitude"]), float(userdata["longitude"]))).nm
            if int(nm) <= int(a["visual_range"]):
                network.send_data(f"{raw_data}\r\n", a["callsign"])
    for p in network.pilot_list:
        p = network.pilot_list[p]
        if p["callsign"] != userdata["callsign"]:
            if geodesic((float(p["latitude"]), float(p["longitude"])), (float(userdata["latitude"]), float(userdata["longitude"]))).nm <= p["visual_range"]:
                network.send_data(f"{raw_data}\r\n", p["callsign"])
def updataPilotFlightPlan(tokens,raw_data):
    filght_plan = {
        "flight_rules": tokens[2],
        "aircraft_type": tokens[3],
        "cruising_speed": tokens[4],
        "departure_airport": tokens[5],
        "departure_time": tokens[6],
        "cruising_altitude": tokens[8],
        "arrival_airport": tokens[9],
        "alternate_airport": tokens[14],
        "remarks": tokens[-2],
        "route": tokens[-1],
        "raw_data": raw_data,
    }
    network.flight_plan[tokens[0][3:]] = filght_plan

def flight_plan(tokens,raw_data):
    updataPilotFlightPlan(tokens,raw_data)
    Judge_the_distance(tokens[0][3:])

