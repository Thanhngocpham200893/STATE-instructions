###This script is use to generate the nfinp and nugded_2 from xyz file 

#! /bin/bash

for i in {2..6}
do

mkdir n$i
cd n$i
cp ../image"$i".xyz old.xyz
cp ../xyz2nfinp.py .
cp ../index.txt .
cp ../state2nudged_2.py .

cat ../nfinp_ini > nfinp
python3 xyz2nfinp.py old.xyz > cps.dat
paste cps.dat index.txt | gawk 'NR==1,NR==14' >> nfinp
cat ../nfinp_end >> nfinp
python3 state2nudged_2.py nfinp 0.02
cp nfinp  nfinp_1
state2xyz.py nfinp_1 > nfinp_1.xyz

let e=$i-1
let f=$i+1
ln -fs ../n$e/nudged_2 nudged_1
ln -fs ../n$f/nudged_2 nudged_3


cd ../

done
