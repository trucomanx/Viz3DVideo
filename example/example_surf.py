#!/usr/bin/python3
# pip install viz3dvideo
import matplotlib.pyplot as plt
import numpy as np
from viz3dvideo.surf.rotate import animate_rotate

plt.style.use('dark_background')

X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))

animate_rotate( X, Y, Z, 
                filename="animate_rotate.mp4",
                pixel_size=(1920, 1080), 
                cb_enable=True,
                cb_title="Z")


