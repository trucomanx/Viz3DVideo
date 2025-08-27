#!/usr/bin/python3
# pip install viz3dvideo
import matplotlib.pyplot as plt
import numpy as np
from viz3dvideo.surf.rotate import animate_rotate

plt.style.use('dark_background')

w = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(w, w)
Z = np.sin(np.sqrt(X**2 + Y**2))

animate_rotate( X, Y, Z, 
                filename="animate_rotate.mp4",
                pixel_size=(2560, 1440) )


