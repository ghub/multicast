import socket

MCAST_GRP = '239.255.43.21'
MCAST_PORT = 45454

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
sock.sendto("robot", (MCAST_GRP, MCAST_PORT))
