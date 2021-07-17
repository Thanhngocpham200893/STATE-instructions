**Charge density difference and interface dipole moment for NO/Cu(111)**

     Thanh N. P, et al, JPCC 124, 2968 (2020)

     Charge density difference (CDD) upon the adsorption of NO is defined as
     CDD = charge (NO/Cu111) - charge (NO) - charge (Cu111).

     We seperated the adsorbed system NO/Cu(111) into two fragments (NO and Cu(111)) 
     where two latter atomic configurations are kept fixed from the total system.

     The CDD calculation is performed with two steps: (1) scf calculation and (2) valance charge density in real space

 (1) **Scf calculation to get the wave function**
 
     We perform scf calculation for three systems, i.e. NO/Cu(111), NO, and Cu(111)
     where atomic configuration is kept fixed
     
     forccr = 1.00D+03 (for scf) and edelta = 1.00D-10 (more accurate criterion) 
     See ./nfinp_total ./nfinp_no ./nfinp_sur

 (2) **Valance charge density in real space**
     
     After scf step, valance density in real space is obtained by perform second STATE calculation with ICOND = 9
     The valance density in real space (VDR) is written in nfchgt_r.data (in STATE code format).
  
 **CDD visualization**
 
    To see CDD, we use VESTA software and VDR should be converted to some compatible formats (.xsf or .cube .vasp)
    To convert VDR in STATE format to .xsf format, Hamada-sensei wrote a code, i.e. chg2xsf.fep, for this purpose.
    To copy this code, you can find it in utils directory in state.5.6.6 or simply copy from my directory /home/thanhpn/STATE/src/Analysis/chg2xsf.fep
    VDR in .xsf format can be obtained by excecuting chg2xsf.fep
    chg2xsf.fep -i nfinp_scf -c nfchgt_r.data -p total
    Here -i nfinp_scf is the name of state input
         -c nfchgt_r.data is thr name of VDR in state format
         -p is prefix for new .xsf file
         
    We will obtain total.xsf for total system.
    Similarly, we can get the VDR for two fragments. 
    CDD in VESTA is done by a nice tutorial at http://renqinzhang.weebly.com/uploads/9/6/1/9/9619514/charge_density_difference.pdf
    Isosurface can be plotted nicely with VESTA (see attached picture)
    
**CDD profile along z direction**

    CDD profile along z direction is a good indicator to see charge transfer, 
    along work function difference.
    
    To obtain CDD profile, we need to get average charge density in xy plane from STATE code. 
    This can be done by grep CHGPRO: nfout_scf
               #z in Bohr #average charge density #Total potential #Electrostatic potential
    CHGPRO:      0.0000      0.2719382313     -0.6020253332      0.0512838242
    CHGPRO:      0.1562      0.2612894534     -0.6030569100      0.0362552707
    ## the value in coluum #5 i.e electrostatic potential is used to get vacuum level of slab.
    Therefore, we need to take the second and third collums (z in Bohr and average charge density) for three systems.
    
    Please prepare the z and charge density for three systems into three files chg_total.dat, chg_no.dat, and chg_sur.dat
