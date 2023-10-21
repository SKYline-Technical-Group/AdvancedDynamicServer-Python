from ServerNetwork.network import main
from tool import kill_port, Connection_pooling, Server
import threading


if __name__ == '__main__':
    kill_port.kill_fsdport()
    server_address = ('0.0.0.0', 6809)
    # pool = threading.Thread(target=Connection_pooling.Print_connection_pools).start()
    threading.Thread(target=Server.Server_data).start()
    main(server_address)
