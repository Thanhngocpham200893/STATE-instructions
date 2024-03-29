**Charge density difference and interface dipole moment for NO/Cu(111)**

     Thanh N. P, et al, JPCC 124, 2968 (2020)

     Charge density difference (CDD) upon the adsorption of NO is defined as
     CDD = charge (NO/Cu111) - charge (NO) - charge (Cu111).

     We seperated the adsorbed system NO/Cu(111) into two fragments (NO and Cu(111)) 
     where two latter atomic configurations are kept fixed from the total system.

     The CDD calculation is performed with two steps: (1) scf calculation and (2) valance charge density in real space

 (1) **Scf calculation with ESM to get the wave function**
 
     We perform scf calculation for three systems, i.e. NO/Cu(111), NO, and Cu(111)
     where atomic configuration is kept fixed.

     One should use PE2 boundary condition (recommended by Morikawa-sensei).
     
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
   
    Please prepare the z and charge density for three systems into three files chg_total.dat, chg_no.dat, and chg_sur.dat
    We estimate CDD profile by subtract the charge density of total system from two framents parts.
    This can be done nicely by using this command
    paste chg_total.dat chg_sur.dat chg_no.dat | gawk '{printf "%.5f %.12f\n", $1, $2-$4-$6}' > CDD.dat
    
**Plot CDD profile**

    Since we use ESM with ESM regions are placed at +/- z/2  and the Cu(111) slab is placed at z < 0,
    we need to plot the CDD from -z/2 to z/2
    CDD profile printed at z of (0, z), so we need to apply PBC to CDD and plot CDD.
    I make a mathplotlib script to plot such feature.
    To use this script, you need to use my python3 environments by using this command.
    source /home/thanhpn/myenv/bin/activate
    To excecute the plot, use this command
    python3 plot.py
    
    Comments on results:
    For the adsorption of NO on metal surfaces, back-donation from metal to NO gas occurs (charge is transfered from metal to NO).
    From CDD profile we can see that at the interface of NO/Cu(111), 
    charge depletion is located at Cu surface (z is around 0),
    while charge accumulation is at NO sites (z = 2, 4 for N,O).
    We also see some charge loss at N-O bond, it may be due to the bond elongation or the donation of NO to the surface. 

**Work function change**
    
    The work function change upon the adsorption is proportionaly to the interface dipole moments induced by adsorption,
    as well as reflects the charge transfer between molecule and surface.
    Positive value indicates interface dipole moment has negative pole outward the surface, and vice vesa.
    
    By using ESM, vacuum level and thus work function are accurately estimated from electrostatic profile.
    Work function of NO/Cu(111) is 5.838 eV,
    whereas Cu(111) has work function of 4.894 eV obtained by STATE (4.94 eV in exp https://doi.org/10.1116/1.4934685).
    Therefore, work function change upon the NO adsorption is 0.944 eV, indicating negative pole outward the surface,
    Or charge is transfer from surface to NO.
    Our calculation result is consistent with NO adsorbs on other transition metals (https://doi.org/10.1039/B920857G)
    

**Interface dipole moment**
    
    
    In STATE code, dipole moment in z direction is calculated.
    To check the dipole moment in z direction, grep "DPL2:" nfout_scf
    DPL2: mu(Debye)
    DPL2:  -0.52448
    The sign of value printed indicate the sign of dipole moments
    Negative (positive) value indicates negative pole outward (inward) the surface.
   
    We divided surface dipole moment of NO/Cu(111) into three different part.
    mu(NO/Cu) = mu(NO) + mu(Cu) + delta_mu,
    where mu(NO), and mu(Cu) is dipole moment of NO and Cu surface at ther adsorbed geometries (from CDD calculation)
    delta_mu is dipole moment arised from electronic interaction between NO and surface
    
    delta_mu =  mu(NO/Cu) - mu(NO) - mu(Cu)  =  -0.52448 - 0.12554 - -0.00161 = -0.64841 (D)
    
    Calculated delta_mu further supports the work function change.
    
    Further reading: https://doi.org/10.1063/1.2940334
