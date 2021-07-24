
**Image Dependent Pair Potential (IDPP) for improved interpolation of initial NEB path**

IDPP provide an excellent initial path interpolation for NEB,
where bond lengths are employed to interpolate the initial images rather than simple linear interpolation.

This example provides how to use IDPP to generate an initial path for STATE code.

**(1) Make initial path by IDPP.**

First prepare initial and final images in .xsf file, then execute the neb.py to get all images in xyz file.

    python3 neb.py


In STATE code, NEB calculation for each intermediate image is run in different folder. 
Therefore, we need to prepare the nfinp in n$i directory by make_path.sh

    sh make_path.sh

Here, the coordinate of the fixed atoms are copied from initial or final path.
This is because there is a slightly different in some units employed in STATE and in ASE,
leading to 1 meV different in total energy.
Therefore, we use the same coordinate for fixed atoms by copying from the old input.


Reference:

[1] J. Chem. Phys. **140**, 214106 (2014).

[2] https://wiki.fysik.dtu.dk/ase/tutorials/neb/idpp.html
