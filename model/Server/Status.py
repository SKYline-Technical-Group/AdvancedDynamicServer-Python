from ServerNetwork import network
import time
def Status_detection():
    while True:
        for i in network.newclients:
            try:
                network.send_data("#DLSERVER:*:0:0", i)
            except:
                network.Disconnect_pool(i)
        time.sleep(15)