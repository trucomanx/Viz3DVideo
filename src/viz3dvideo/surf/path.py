#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.interpolate import interp1d

def animate_path(   X, Y, Z, camera_points, 
                    pixel_size=(1920, 1080), 
                    dpi=100, 
                    colormap='viridis',
                    filename="superficie_path.mp4", 
                    steps=360,
                    interval=30,
                    fps=30, 
                    cb_enable=False,
                    cb_title="Z"):
    """
    Creates and saves a 3D animation of the surface Z = f(X, Y) following a camera path
    defined by `camera_points`.

    Args:
        X (array-like): 2D array of X coordinates of the surface.
        Y (array-like): 2D array of Y coordinates of the surface.
        Z (array-like): 2D array of Z values of the surface.
        camera_points (list of tuple): List of (elev, azim) tuples defining the camera path.
        steps (int, optional): Total number of frames in the animation. Default is 360.
        pixel_size (tuple, optional): Figure size in pixels (width, height). Default is (1920, 1080).
        dpi (int, optional): Figure resolution in dots per inch. Default is 100.
        colormap (str, optional): Colormap for the surface. Default is 'viridis'.
        filename (str, optional): Output file name. Default is 'superficie_path.mp4'.
        fps (int, optional): Frames per second for the video. Default is 30.
        interval (int, optional): Interval between frames in milliseconds. Default is 30.

    Returns:
        None
    """
    # --- Calcula figsize ---
    width, height = pixel_size
    figsize = (width / dpi, height / dpi)

    # --- Cria figura ---
    fig = plt.figure(figsize=figsize, dpi=dpi)
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap=colormap)

    # --- Interpolação ---
    camera_points = np.array(camera_points)
    n_points = len(camera_points)
    t_original = np.linspace(0, 1, n_points)
    t_interp = np.linspace(0, 1, steps)

    elev_interp = interp1d(t_original, camera_points[:,0], kind='cubic')(t_interp)
    azim_interp = interp1d(t_original, camera_points[:,1], kind='cubic')(t_interp)

    # --- Função de atualização ---
    def update(frame):
        ax.view_init(elev=elev_interp[frame], azim=azim_interp[frame])
        return []

    def progresso(frame_number, total_frames):
        print(f"Renderizando frame {frame_number+1}/{total_frames}", end='\r')

    ani = FuncAnimation(fig, update, frames=steps, interval=interval, blit=False)

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

    # Lista de pontos de câmera pelos quais a animação deve passar
    camera_points = [(30, 0), (45, 90), (60, 180), (30, 270), (30, 360)]

    animate_path(X, Y, Z, camera_points, steps=360)

