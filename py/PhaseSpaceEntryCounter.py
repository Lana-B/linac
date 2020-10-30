import numpy as np
from ROOT import TFile, TTree
# entries=np.array([])

stringy=""

for i in range (1,361):
	filename="/work/lb8075/PhaseSpaces/PhS2Elec/ElecFromElec/output2e9primaries-lana2-PhS-e_nobias"+str(i)+".root"
	rfile=TFile(filename)
	rtree=rfile.Get("PhaseSpace")
	ent=rtree.GetEntries()
	# entries=np.append(entries,ent)
	# print(ent)
	if i==1:
		stringy=stringy+"["+str(ent)
	stringy=stringy+" "+str(ent)
stringy=stringy+"]"
print(stringy)
