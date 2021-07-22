"""
#!/home/thanhpn/Env/bin/python3
Read the state input and write nudged_2 
Usage: state2nudged_2.py nfinp_# spring_constant
"""

##-----import library here
import numpy as np
import sys
##-----end load library

##read the name of state input from command line
if len(sys.argv) == 3:
    stateinp = str(sys.argv[1])
    spring   = float(sys.argv[2])
else:
    sys.exit('state2nudged_2.py nfinp_# spring_constant')


with open(stateinp,"r") as inp:
    dummy =inp.readline()
    dummy =inp.readline()
    ktyp = int(dummy.split()[2])
    katm = int(dummy.split()[3])
    print(katm)
    inp.readline()
    inp.readline()
    inp.readline()
    inp.readline()
    inp.readline()
    inp.readline()
    inp.readline()
    cps = np.zeros((katm,3),dtype = float)
    ktyp_l = np.zeros((katm,1),dtype = int)
    for i in range(katm):
        dummy = inp.readline()
        cps[i,0:3] = dummy.split()[0:3]


###print the output

with open('nudged_2', 'w+') as nudged:
    nudged.truncate(0)

with open('nudged_2','a+') as nudged:
    print('%.12f' %(spring),file = nudged)
    for i in range(katm):
        print(" %3i   % 16.12f   % 16.12f   % 16.12f" %
         (i+1,
          cps[i,0],
          cps[i,1],
          cps[i,2]),file = nudged)
