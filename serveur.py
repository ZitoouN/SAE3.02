import socket
from socket import AF_INET
import platform
import psutil
from ipaddress import IPv4Network

host = "127.0.0.1"
port = 8080
disc = True

server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(1)


print('En attente de connexion client ...')
conn, address = server_socket.accept()
print(f'Client connecté : {address}')


while disc:
    data = conn.recv(1024).decode()

    if data == 'OS':
        conn.send(f"{platform.system()}".encode())
        print(f"Message du client : OS")


    elif data == 'disconnect':
        conn.close()
        print(f"Message du client : disconnect")
        print(f"Client déconnecté ... en attente d'une nouvelle connexion")
        conn, address = server_socket.accept()


    elif data == 'CPU':
        nbr_cpu = psutil.cpu_count()
        cpus = psutil.cpu_percent(interval=2, percpu=True)
        cpusfinal = str(cpus)[1:-1]
        conn.send(f"Nombre de CPU logiques dans le système : {nbr_cpu} ".encode())
        conn.send(f"Utilisation de tous les CPU : {cpusfinal} ".encode())
        print(f"Message du client : CPU")


    elif data == 'RAM':
        meminfo = psutil.virtual_memory()
        total = round(meminfo.total / 1_073_741_824, 2)
        utilise = round(meminfo.used / 1_073_741_824, 2)
        disponible = round(meminfo.free / 1_073_741_824, 2)
        conn.send(f"Total de RAM : {total} Go, RAM utilsé : {utilise} Go, RAM disponible : {disponible} Go".encode())
        print(f"Message du client : RAM")


    elif data == 'IP':
        ipa = []
        for nic, addrs in psutil.net_if_addrs().items():
            for addr in addrs:
                address = addr.address
                if addr.family == AF_INET and not address.startswith("169.254"):
                    ipa.append(f"{address}/{IPv4Network('0.0.0.0/' + addr.netmask).prefixlen}")
        ipfinal = str(ipa)[1:-1]
        conn.send(f"IP de la machine : {ipfinal}".encode())
        print(f"Message du client : IP")


    elif data == 'Name':
        conn.send(f"Nom de la machine : {platform.node()}".encode())
        print(f"Message du client : Name")


    elif data == 'Connexion information':
        conn.send(f"Le nom de la machine est {socket.gethostbyname(socket.gethostname())} ".encode())
        print(f"Message du client : Name")





    else :
        print(f"Message du client : {data}")
