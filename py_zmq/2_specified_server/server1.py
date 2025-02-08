import server

if __name__ == "__main__":
    server_addr = "ipc:///tmp/broker_server.ipc"  # 代理的地址
    name = "tasks/jack/jack.py"  # 服务端处理的 name 字段
    server.start_server(server_addr, name)