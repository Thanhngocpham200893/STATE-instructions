**This tutorials discuss how to get layer-resolved-band structures (LRDOS) and K-resolved LRDOS**

Here, single C is adsorbed on top of Cu(1x1) surface.

#Step 1. 
**Perform scf calculation to get wave function and charge density by STATE code.**

See nfinp_1 nfinp_2, nfinp_3


#**Step 2. Perform LRDOS calculation by STATE code.**

We performed LRDOS as follows

(1) Create  nfaldos.data file

(2) Change ICOND = 33 

(3) Running STATE

#**Step 2. Plot LRDOS**

The aldos.data file is generated by STATE,

in which

first coluum corresponds to index of layer,

second one corresponds to the energy range,

third one corresponds to the DOS,

**Excecute python3 code plot_layer.py to plot**


