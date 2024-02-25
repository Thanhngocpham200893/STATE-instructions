import numpy as np
####
###remove the header 
##number of band
nob = 80
##number of kpoint for both channel
nk  = 200
#### end point in k path
end = '2.05444015'
with open('band.data', 'r+') as inp:
    nfinp = inp.readlines()

for i,line in enumerate(nfinp):
    if line.isspace():
        nfinp.pop(i)


band_up = []
for a,b in enumerate(nfinp):
    if a  % 2 == 0: # for spin up
        band_up.append(b)

with open('band_up.data', 'w+') as inp:
    for i,j in enumerate(band_up):
        if j.split()[0] == end:
            print(j, file = inp, end = '    ')
            print('    ', file = inp)
        else:
            print(j, end = '     ', file = inp)
band_dw = []
for a,b in enumerate(nfinp):
    if a  % 2 == 1: # for spin dw
        band_dw.append(b)

with open('band_dw.data', 'w+') as inp:
    for i,j in enumerate(band_dw):
        if j.split()[0] == end:
            print(j, file = inp, end = '    ')
            print('    ', file = inp)
        else:
            print(j, end = '     ', file = inp)
