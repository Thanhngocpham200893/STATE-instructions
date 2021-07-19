import numpy as np
import matplotlib.pyplot as plt
import os
##-----end load library
z,cdd = np.loadtxt('CDD.dat', usecols =(0,1),unpack = True)


#set font
plt.rcParams["mathtext.fontset"]="dejavuserif"
font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }

font2 = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 10,
        }

#set xrange
ylb = -30
ylt = 30
plt.ylim(ylb,ylt)
#ly = lx*0
#ef_new = ef*27.211396132 + lx*0
#plt.plot(lx,ly, '--', color = 'gray', linewidth=1)
#plt.plot(lx,ef_new, '--', color = 'black', linewidth=2)


#set label
plt.ylabel('$z/ a_\mathrm{0}$', fontdict = font)
plt.xlabel('CDD', fontdict = font)
#set tick
#plt.yticks(np.arange(-40, 200, step=20))

#plot
p1 = plt.plot(np.concatenate((cdd,cdd)),np.concatenate((z-60,z)), '-', color = 'red', markersize = 10,linewidth=3)
plt.legend(loc = 0,handlelength=3, borderpad=0.2, labelspacing=0.3, fontsize=14)

plt.tight_layout()
plt.savefig('CDD.png', dpi=300)
plt.show()
