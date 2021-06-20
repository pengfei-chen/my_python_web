import socket 

# 建立服务
sk = socket.socket()
# 绑定ip
sk.bind(("192.168.153.128",5500))
# 监听
sk.listen()
print("服务器开始运行啦。。。")

while True:
    # 链接客户端
    conn, addr = sk.accept()
    # 接收数据
    data = conn.recv(1024)
    print(data)
    if data:
        conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
        conn.send(bytes("我是python客户端,我已接到你的请求。。。", encoding="utf-8"))
        break