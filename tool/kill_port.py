import psutil

# 找出占用指定端口的进程
def find_process_using_port(port):
    for conn in psutil.net_connections(kind='inet'):
        if conn.laddr.port == port:
            return conn.pid
    return None

# 终止指定PID的进程
def kill_process(pid):
    try:
        process = psutil.Process(pid)
        process.terminate()
        print(f"Process with PID {pid} has been terminated.")
    except psutil.NoSuchProcess:
        print(f"No process found with PID {pid}.")

# 定义要查找和终止的端口
def kill_fsdport():
    port_to_terminate = 6809

    # 找出占用指定端口的进程
    pid_using_port = find_process_using_port(port_to_terminate)

    if pid_using_port:
        # 终止占用指定端口的进程
        kill_process(pid_using_port)
    else:
        print(f"No process found using port {port_to_terminate}.")
