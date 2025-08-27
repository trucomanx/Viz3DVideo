#!/usr/bin/python3
# pip install viz3dvideo
import sys
sys.path.append("../../src")
import matplotlib.pyplot as plt
import numpy as np
import viz3dvideo as vz3 

plt.style.use('dark_background')

w = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(w, w)
Z = np.sin(np.sqrt(X**2 + Y**2))

vz3.surf.animate_rotate( 
                X, Y, Z, frames=1440, 
                output_path="rotate.mp4",
                pixel_size=(2560, 1440) )

vz3.overlay.image_on_video( 
                video_path="rotate.mp4",
                image_path="code.png",
                position=(20,20),
                output_path="rotate_logo.mp4" )
