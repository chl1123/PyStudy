import zmq

def start_broker(frontend_addr, backend_addr):
    context = zmq.Context()

    # 创建 ROUTER 套接字监听客户端请求
    frontend = context.socket(zmq.ROUTER)
    frontend.bind(frontend_addr)

    # 创建 DEALER 套接字连接到服务端
    backend = context.socket(zmq.DEALER)
    backend.bind(backend_addr)

    print(f"Broker started: frontend={frontend_addr}, backend={backend_addr}")

    # 启动代理
    zmq.proxy(frontend, backend)

    frontend.close()
    backend.close()
    context.term()

if __name__ == "__main__":
    frontend_addr = "ipc:///tmp/cpp2python_client.ipc"  # 客户端连接地址
    backend_addr = "ipc:///tmp/cpp2python_broker.ipc"  # 服务端连接地址
    start_broker(frontend_addr, backend_addr)
