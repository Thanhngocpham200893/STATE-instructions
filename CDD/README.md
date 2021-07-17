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
 
    To see CDD, we use VESTA software, VDR should be converted to some compatible formats (.xsf or .cube .vasp)
    To convert VDR in STATE format to .xsf format, Hamada-sensei wrote a code, i.e. chg2xsf.fep, for this purpose.
    To copy this code, You can find it in utils directory in state.5.6.6 or simply copy from my directory /home/thanhpn/STATE/src/Analysis/chg2xsf.fep
    VDR in .xsf format can be obtained by excecuting chg2xsf.fep
    chg2xsf.fep -i nfinp_scf -c nfchgt_r.data -p total
    Here -i nfinp_scf is the name of state input
         -c nfchgt_r.data is thr name of VDR in state format
         -p is prefix for new .xsf file
         
    We will obtain total.xsf for total system.
    
