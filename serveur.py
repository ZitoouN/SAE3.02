import socket
from socket import AF_INET
import platform
import psutil
from ipaddress import IPv4Network

def Serveur():
    data = ""
    conn = None
    server_socket = None

    while data != "kill" :
        data = ""
        server_socket = socket.socket()
        server_socket.bind(("127.0.0.1", 10013))

        server_socket.listen(5)
        print('-----SERVEUR-----')
        print('En attente de connexion client ...')

        while data != "kill" and data != "reset":
            data = ""
            try :
                conn, addr = server_socket.accept()
                print(f'Client connecté : {addr}')
            except ConnectionError:
                print ("CONNECTION ERROR")
                break
            else :
                while data != "disconnect" and data != "reset" and data != "kill":
                    data = conn.recv(1024).decode()
                    print ("Message du client : ", data)

                    if data == 'OS':
                        conn.send(f"{platform.system()}".encode())

                    elif data == 'CPU':
                        nbr_cpu = psutil.cpu_count()
                        cpus = psutil.cpu_percent(interval=2, percpu=True)
                        cpusfinal = str(cpus)[1:-1]
                        conn.send(f"Nombre de CPU logiques dans le système : {nbr_cpu}, Utilisation de tous les CPU : {cpusfinal}".encode())


                    elif data == 'RAM':
                        meminfo = psutil.virtual_memory()
                        total = round(meminfo.total / 1_073_741_824, 2)
                        utilise = round(meminfo.used / 1_073_741_824, 2)
                        disponible = round(meminfo.free / 1_073_741_824, 2)
                        conn.send(f"Total de RAM : {total} Go, RAM utilsé : {utilise} Go, RAM disponible : {disponible} Go".encode())


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
                        conn.send(
                            f"Le nom de la machine est {platform.node()}, son IP est la suivante : {socket.gethostbyname(socket.gethostname())}".encode())

                conn.close()
        print ("CONNECTION FERMÉ !")

        server_socket.close()
        print ("SERVEUR FERMÉ !")


if __name__ == '__main__':
    Serveur()
