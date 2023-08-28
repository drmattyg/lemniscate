import numpy as np
import svgwrite
import pandas as pd
from pandas import Dataframe
import trimesh as trm

# draws a simple lemniscate
def bernoulli_lemniscate(z_scale=1, z_function=np.sin):
    t = np.linspace(0, 2*np.pi, 1000)  # Generate values of t from 0 to 2*pi
    x = np.sqrt(2) * np.cos(t) / (np.sin(t)**2 + 1)  # Compute x values using the equation
    y = np.sqrt(2) * np.cos(t) * np.sin(t) / (np.sin(t)**2 + 1)  # Compute y values using the equation
    z = z_scale*z_function(t)

def plot_3d(x, y, z):
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

# todo: Make this handle 3D
def write_svg(output_name, x, y):
    dwg = svgwrite.Drawing(output_name, profile='tiny')
    dwg.add(svgwrite.path.Path(d='M' + ' '.join([f'{px},{py}' for px, py in zip(x, y)]), fill='none', stroke='black'))
    dwg.save()

def sweep_mesh(x, y, z, poly):
    path = zip(x, y, z)
    mesh = trm.creation.sweep_polygon(poly, path)
    return sweep_mesh

def display_mesh(mesh):
    from IPython.display import display, HTML
    from trimesh.viewer.notebook import scene_to_html

    scene = trm.Scene(geometry=mesh)
    html= scene_to_html(scene)
    display(HTML(html))

