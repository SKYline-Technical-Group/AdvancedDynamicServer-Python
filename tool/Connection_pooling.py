import ServerNetwork.network as network
import time
def Print_connection_pools():
    while True:
        print(network.atc_list,network.pilot_list)
        time.sleep(5)
