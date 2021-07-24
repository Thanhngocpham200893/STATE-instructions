
"""
Read the xyz file  and write coordinate in Bohr 
Usage: python3 xyz2nfinp.py  #.xyz > nfinp
"""

##-----import library here
import numpy as np
import sys
from ase.units import Bohr
from ase.io import read
##-----end load library


##read the name of state input from command line
if len(sys.argv) == 2:
    xyzinp = str(sys.argv[1])
else:
    sys.exit('Usage: python3 xyz2nfinp.py  #.xyz > nfinp')

Atoms = read(xyzinp)
cps = Atoms.get_positions()*(1/Bohr)
katm = cps.shape[0]
for i in range(katm):
    print(" %16.12f   %16.12f   %16.12f" %
         (cps[i,0],
          cps[i,1],
          cps[i,2]))
