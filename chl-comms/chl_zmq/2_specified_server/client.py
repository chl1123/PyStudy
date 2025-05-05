import zmq
import json

def start_client(server_addr, name, method, args):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)  # 使用 REQ 套接字
    socket.connect(server_addr)

    # 构建请求消息
    request = {
        "name": name,
        "method": method,
        "args": args
    }
    request_msg = json.dumps(request)

    print(f"Sending request: {request}")

    # 发送请求
    socket.send(request_msg.encode('utf-8'))

    # 接收响应
    response = socket.recv()
    response_data = json.loads(response.decode('utf-8'))
    print(f"Received response: {response_data}")

if __name__ == "__main__":
    server_addr = "ipc:///tmp/client_broker.ipc"  # 代理的地址
    # name = "tasks/jack/jack.py"  # 服务端处理的 name 字段
    # method = "test1"  # 请求的方法名
    # args = {"key1": "value1"}  # 请求的参数
    # start_client(server_addr, name, method, args)

    name = "tasks/move/move.py"  # 服务端处理的 name 字段
    method = "test2"  # 请求的方法名
    args = {"key2": "value2"}  # 请求的参数
    start_client(server_addr, name, method, args)