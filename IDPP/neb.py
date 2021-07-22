"""
Make intial path using IDPP method.
Coordinates of each image is written at "image#.xyz"
"""
from ase import io
from ase.neb import NEB
from ase.calculators.emt import EMT
from ase.optimize import BFGS

## number of image consisted of initial and final images
noi = 9

## Read initial and final states:
initial = io.read('initial.xsf')
final = io.read('final.xsf')
## Make a band consisting of noi images:
images = [initial]
images += [initial.copy() for i in range(noi-2)]
images += [final]
neb = NEB(images)

## interpolate:
neb.interpolate('idpp')

## Set calculators:
for image in images[1:(noi-1)]:
    image.set_calculator(EMT())


## Optimize:
optimizer = BFGS(neb, trajectory='path.traj')
optimizer.run(fmax=1000)

##write the initial path
for i in range(0,noi,1):
    name = "image{}.xyz".format(i+1)
    traj=io.read('path.traj',index = i)
    traj.write(filename=name,format ='xyz')
