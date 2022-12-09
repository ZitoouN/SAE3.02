import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from psutil import virtual_memory

frame_len = 200
y = []
fig = plt.figure(figsize=(8,4))

def animate(i):
    y.append(virtual_memory())

    if len(y) <= frame_len:
        plt.cla()
        plt.plot(y, 'r')
    else:
        plt.cla()
        plt.plot(y, 'r')

    plt.ylim(0,100)
    plt.xlabel('Temps en secondes (s)')
    plt.ylabel('Usage du CPU (%)')

ani = FuncAnimation(plt.gcf(), animate, interval=150)

def graph():
    plt.show()

if __name__ == '__main__':
    graph()
