#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_rotate( X, Y, Z, 
                    filename="superficie_hd.mp4",
                    pixel_size=(1920, 1080), 
                    dpi=100, 
                    colormap='viridis',
                    elev=30, 
                    frames=360, 
                    interval=30, 
                    fps=30):
    """
    Creates and saves a 3D animation of the surface Z = f(X, Y).

    Args:
        X (array-like): 2D array of X coordinates of the surface.
        Y (array-like): 2D array of Y coordinates of the surface.
        Z (array-like): 2D array of Z values of the surface.
        filename (str, optional): Output file name. Default is 'superficie_hd.mp4'.
        pixel_size (tuple, optional): Figure size in pixels (width, height). Default is (1920, 1080).
        dpi (int, optional): Figure resolution in dots per inch. Default is 100.
        colormap (str, optional): Colormap for the surface. Default is 'viridis'.
        elev (float, optional): Initial elevation of the camera. Default is 30.
        frames (int, optional): Total number of frames in the animation. Default is 360.
        interval (int, optional): Interval between frames in milliseconds. Default is 30.
        fps (int, optional): Frames per second for the video. Default is 30.

    Returns:
        None
    """
    width, height = pixel_size
    figsize = (width / dpi, height / dpi)  # calcula tamanho em polegadas
    fig = plt.figure(figsize=figsize, dpi=dpi)
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap=colormap)
    
    def update(frame):
        ax.view_init(elev=elev, azim=frame)
        return []

    def progresso(frame_number, total_frames):
        print(f"Renderizando frame {frame_number+1}/{total_frames}", end='\r')

    ani = FuncAnimation(fig, update, frames=frames, interval=interval, blit=False)

    ani.save(
        filename,
        writer='ffmpeg',
        fps=fps,
        dpi=dpi,
        progress_callback=progresso
    )
    print(f"\nVídeo salvo em {width}x{height} pixels como '{filename}'")


if __name__ == "__main__":
    plt.style.use('dark_background')

    X = np.linspace(-5, 5, 100)
    Y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(X, Y)
    Z = np.sin(np.sqrt(X**2 + Y**2))

    animate_rotate(X, Y, Z)


