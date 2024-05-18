from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numpy import random

square = plt.Rectangle((-0.5, -0.5), 1, 1, fill=False)
circle = plt.Circle((0, 0), 0.5, color='b', fill=False)
fig, ax = plt.subplots()
ax.add_patch(square)
ax.add_patch(circle)
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.5, 0.5)
x = 0

index = count()
next(index)


def animate(*args, **kwargs):
    num = next(index)
    global x
    if num == 10000:
        ani.event_source.stop()
    k = random.uniform(low=-1, high=1, size=2)
    if k[0] ** 2 + k[1] ** 2 <= 1:
        x += 1
    print(x / num * 4)
    ax.scatter(k[0], k[1], s=1, c='black')


ani = FuncAnimation(plt.gcf(), animate, interval=0)

plt.tight_layout()
plt.show()
