from ServerNetwork import network
import time
import json
import datetime
def Server_data():
    while True:
        data = {}
        foundation = {
        "update": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "update_timestamp": int(time.time()),
        "pilots": len(network.pilot_list),
        "atc": len(network.atc_list)
        }
        data["general"] = foundation
        data["pilots"] = network.pilot_list
        data["atc"] = network.atc_list
        with open("data.json","w") as f:
            json.dump(data,f)
        time.sleep(5)
