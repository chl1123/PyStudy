import zmq
import json


def start_server(server_addr):
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.connect(server_addr)

    print(f"Server started: connected to {server_addr}")

    while True:
        # 接收请求
        message = socket.recv()
        request = json.loads(message.decode('utf-8'))
        print("request <=", request)

        # 处理请求
        method = request.get("method")
        args = request.get("args")
        name = request.get("name")

        # 模拟处理逻辑
        response = {"code": 0, "result": f"Processed {method} with args {args} for {name}"}
        print("response =>", response)

        # 发送响应
        socket.send_string(json.dumps(response))


if __name__ == "__main__":
    server_addr = "ipc:///tmp/cpp2python_broker.ipc"  # 代理的后端地址
    start_server(server_addr)
