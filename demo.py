# -*- coding: utf-8 -*-
import socket

"""
-------------------------------------------------
   File Name：     demo
   Description :
   Author :       burt
   date：          2019-02-12
-------------------------------------------------
   Change Activity:
                   2019-02-12:
-------------------------------------------------
"""


def main():
    # 1. 创建tcp的套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 链接服务器
    # tcp_socket.connect(("192.168.33.11", 7890))
    server_ip = '192.168.0.100'
    server_port = 2222
    server_addr = (server_ip, server_port)
    tcp_socket.connect(server_addr)

    # 3. 发送数据/接收数据
    send_data = 'are you ok?'
    tcp_socket.send(send_data.encode("utf-8"))

    # 4. 关闭套接字
    tcp_socket.close()


if __name__ == "__main__":
    main()
