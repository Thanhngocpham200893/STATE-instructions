import numpy as np
from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt
from matplotlib import cm
from ase.io import read, write
from ase.visualize import view

import sys


x,y,z = np.loadtxt('aldos_k.data', unpack = True, usecols= (0,1,2))
x_new = (x-1)*0.5*0.02088826
###best
fig = plt.figure(figsize = [3.5,2.625])
ax = fig.gca()
ax.tick_params(labelsize='small', direction = 'in',width=1)
ax.spines['top'].set_linewidth(1)
ax.spines['bottom'].set_linewidth(1)
ax.spines['right'].set_linewidth(1)
ax.spines['left'].set_linewidth(1)
#set font
#plt.rcParams["mathtext.fontset"]="dejavuserif"
font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 12,
        }

marker_size=2
norm_z = np.array(z)
norm_z = (norm_z - min(norm_z)) / (max(norm_z) - min(norm_z))

# Define the color range you want to visualize
vmin = 0.0
vmax = 0.5
scatter = plt.scatter(x_new, y, marker_size, c=z, vmin=vmin, vmax=vmax,
                      cmap='viridis')
###
ax.set_ylim(-10,5)
plt.xlabel('K path ($\mathrm{\AA}^{-1}$)', fontdict = font)
plt.ylabel('Energy (eV)', fontdict = font)
#ax.axvline(x = 0,linestyle='--', color = 'grey', linewidth = 0.5)
# Set colorbar
cbar = plt.colorbar(scatter)
cbar.set_label('DOS')
plt.tight_layout()
plt.savefig('layer_dos.png', dpi=300)
