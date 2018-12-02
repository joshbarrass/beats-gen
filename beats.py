#!/usr/bin/env python3.6

# Matplotlib animated plot of beats

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

AMPLITUDE = 5
K1 = 15 #15
K2 = 12 #12
OMEGA1 = 5.85 #5.85
OMEGA2 = 5.75 #5.75

YRANGE = AMPLITUDE + 3
FPS = 30
FRAME_INTERVAL = 1/FPS

def beats(x,t,A,k1,k2,omega1,omega2):
    deltak = (k1 - k2)/2
    deltaomega = (omega1 - omega2)/2
    avgk = (k1 + k2)/2
    avgomega = (omega1 + omega2)/2

    return A * np.cos(deltak*x - deltaomega*t) *\
           np.sin(avgk*x - avgomega*t)

def calc_phase_vel(k1,k2,omega1,omega2):
    avgk = (k1 + k2)/2
    avgomega = (omega1 + omega2)/2
    return avgomega/avgk

def calc_group_vel(k1,k2,omega1,omega2):
    deltak = (k1 - k2)/2
    deltaomega = (omega1 - omega2)/2
    return deltaomega/deltak

#BEAT_WAVELENGTH = (2*np.pi)/((K1 - K2)/2)
#TIME_LENGTH = BEAT_WAVELENGTH/calc_group_vel(K1,K2,OMEGA1,OMEGA2)
TIME_LENGTH = (2*np.pi)/((OMEGA1 - OMEGA2)/2)

print(f"Phase vel: {calc_phase_vel(K1,K2,OMEGA1,OMEGA2)}")
print(f"Group vel: {calc_group_vel(K1,K2,OMEGA1,OMEGA2)}")
print(f"Animation Length: {TIME_LENGTH}")

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes([0,0,1,1],xlim=(0,20),ylim=(-YRANGE,YRANGE))#xlim=(0, 2), ylim=(-2, 2))
ax.set_axis_off()
line, = ax.plot([], [], "r")

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    t = i/FPS
    x = np.linspace(0, 20, 1000)
    y = beats(x,t,AMPLITUDE,K1,K2,OMEGA1,OMEGA2)
    line.set_data(x, y)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=int(FPS*TIME_LENGTH), interval=FRAME_INTERVAL, blit=True)

#anim.save('beats_small.mp4', fps=FPS, extra_args=['-vcodec', 'libx264', "-preset", "veryslow"])

plt.show()

