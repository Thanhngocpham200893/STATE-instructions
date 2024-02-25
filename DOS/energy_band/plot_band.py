import numpy as np
from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt

from ase.io import read, write
from ase.visualize import view

import sys

nk = 100
nb = 80
def split_given_size(a, size):
    return np.split(a, np.arange(size,len(a),size))


energy     = sys.argv[1]
with open(energy, 'r+') as inp:
    nfinp = inp.readlines()

dis,energy = np.loadtxt(energy,usecols = (0,1), unpack = True)

e  =  split_given_size(energy, size = nk)
k  =  split_given_size(dis, size = nk)
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

plt.axvline(x = k[0][36])
plt.axvline(x = k[0][56])
plt.xlim(k[0][0],k[0][-1])
plt.ylim(-10,5)
plt.xlabel('K path ($\mathrm{\AA}^{-1}$)', fontdict = font)
plt.ylabel('Energy (eV)', fontdict = font)

for i in range(nb):
    plt.plot(k[i],e[i], '-o',  color = 'red', markersize = 1,linewidth=1)


plt.tight_layout()
plt.savefig('band.png', dpi=300)
plt.show()
