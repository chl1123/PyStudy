import zmq
import json

def start_server(server_addr, name):
    context = zmq.Context()
    socket = context.socket(zmq.DEALER)  # 使用 DEALER 套接字
    socket.connect(server_addr)
    print(f"Server connected to {server_addr}")

    # 发送注册信息到代理
    register_msg = {"name": name}
    print(f"Sending registration message: {register_msg}")
    socket.send_multipart([b"", json.dumps(register_msg).encode('utf-8')])

    # 接收注册响应
    response_parts = socket.recv_multipart()
    print(f"Received registration response: {response_parts}")
    if len(response_parts) != 2:
        print("Invalid registration response format")
        return
    empty, register_response_str = response_parts
    register_response = json.loads(register_response_str.decode('utf-8'))

    if register_response["code"] != 0:
        print(f"Registration failed: {register_response['error']}")
        return

    print(f"Registered successfully for {name}")

    while True:
        try:
            # 接收请求
            message_parts = socket.recv_multipart()
            for message_part in message_parts:
                print(f"Received message part: {message_part}")
            if len(message_parts) != 4:
                print("Invalid request format")
                continue
            empty, client_id, empty, request_str = message_parts
            request = json.loads(request_str.decode('utf-8'))

            # 处理请求
            method = request.get("method")
            args = request.get("args")
            name = request.get("name")

            # 模拟处理逻辑
            response = {"code": 0, "result": method + "ok"}
            print(f"response => {response}")

            # 发送响应
            socket.send_multipart([client_id, b"", json.dumps(response).encode('utf-8')])
        except Exception as e:
            print(f"Error handling request: {e}")

if __name__ == "__main__":
    server_addr = "ipc:///tmp/broker_server.ipc"  # 代理的后端地址
    name = "tasks/jack/jack.py"  # 服务端处理的 name 字段
    start_server(server_addr, name)