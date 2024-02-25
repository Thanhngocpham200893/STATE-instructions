**How to perform energy band structure and energy band structure projected onto adsorbate layer**

**First step is to get energy band structure**

Here I focus on spin polarization calculation <br />
(1) getting wave function and charge density from STATE by running nfinp_1, nfinp_2, and nfinp_3 <br />
(2) Prepare the k-path by using Xcrysden and prepare nfkpt.data (the units of K points is 2pi/a* 2pi/b*, 2pi/c*)
(3) Running STATE with ICOND = 22
(4) After finishing calculations, energy.data is generated.
Then, we use energy2band program by Hamada-sensei to get band.data to plot in gnuplot.<br />
However, spin up and down are not seperated..<br />
Hence, we use split_band.py to split band.data to band_up.data and band_dw.data<br />

