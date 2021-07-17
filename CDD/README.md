**Charge density difference and interface dipole moment for NO/Cu(111)**

     Thanh N. P, et al, JPCC 124, 2968 (2020)

     Charge density difference (CDD) upon the adsorption of NO is defined as
     CDD = charge (NO/Cu111) - charge (NO) - charge (Cu111).

     We seperated the adsorbed systems NO/Cu(111) into two fragments (NO and Cu(111)) 
     where two latter atomic configurations are kept fixed from the total system.

     The CDD calculation is then straightforward with two steps: (1) scf calculation and (2) valance charge density in real space

 (1) **Scf calculation to get the wave function**
     We perform scf calculation for three systems, i.e. NO/Cu(111), NO, and Cu(111)
     where atomic configuration is kept fixed
     forccr = 1.00D+03 (for scf) and edelta = 1.00D-10 (more accurate criterion) 

 (2) **Valance charge density in real space** 
     After scf step, valance density in real space is obtained by perform second STATE calculation with ICOND = 9
