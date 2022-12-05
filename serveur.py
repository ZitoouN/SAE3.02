import socket
from socket import AF_INET
import platform
import psutil
from ipaddress import IPv4Network

def Serveur():
    data = ''
    conn = None
    serveur_socket = None

    while data != "kill":
        serveur_socket = socket.socket()
        serveur_socket.bind(("127.0.0.1", 8080))
        serveur_socket.listen(1)
        print('En attente de connexion client ...')

        while data != "reset" and "kill":
            data = ''
            try:
                conn, addr = serveur_socket.accept()
                print(f'Client connecté : {addr}')
            except ConnectionError:
                print("Connection ERROR")
                break
            else:
                while data != "kill" and data != "reset" and data != "disconnect":
                    data = conn.recv(1024).decode()
                    print("Message du client : ", data)

                    if data == 'OS':
                        conn.send(f"{platform.system()}".encode())

                    elif data == 'CPU':
                        nbr_cpu = psutil.cpu_count()
                        cpus = psutil.cpu_percent(interval=2, percpu=True)
                        cpusfinal = str(cpus)[1:-1]
                        conn.send(f"Nombre de CPU logiques dans le système : {nbr_cpu} ".encode())
                        conn.send(f"Utilisation de tous les CPU : {cpusfinal} ".encode())


                    elif data == 'RAM':
                        meminfo = psutil.virtual_memory()
                        total = round(meminfo.total / 1_073_741_824, 2)
                        utilise = round(meminfo.used / 1_073_741_824, 2)
                        disponible = round(meminfo.free / 1_073_741_824, 2)
                        conn.send(
                            f"Total de RAM : {total} Go, RAM utilsé : {utilise} Go, RAM disponible : {disponible} Go".encode())


                    elif data == 'IP':
                        ipa = []
                        for nic, addrs in psutil.net_if_addrs().items():
                            for addr in addrs:
                                address = addr.address
                                if addr.family == AF_INET and not address.startswith("169.254"):
                                    ipa.append(f"{address}/{IPv4Network('0.0.0.0/' + addr.netmask).prefixlen}")
                        ipfinal = str(ipa)[1:-1]
                        conn.send(f"IP de la machine : {ipfinal}".encode())


                    elif data == 'Name':
                        conn.send(f"Nom de la machine : {platform.node()}".encode())


                    elif data == 'Connexion information':
                        conn.send(f"Le nom de la machine est {platform.node()}, son IP est la suivante : {socket.gethostbyname(socket.gethostname())}".encode())

            conn.close()

        print("Fermetture de la connection")
        serveur_socket.close()
        print("Serveur fermé")

if __name__ == '__main__':
    Serveur()
