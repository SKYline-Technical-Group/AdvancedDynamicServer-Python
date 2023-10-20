from ServerNetwork.network import main
from tool import kill_port, Connection_pooling
import threading


if __name__ == '__main__':
    kill_port.kill_fsdport()
    server_address = ('localhost', 6809)
    pool = threading.Thread(target=Connection_pooling.Print_connection_pools).start()
    main(server_address)
