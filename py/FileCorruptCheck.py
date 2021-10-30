import numpy as np
import os
from ROOT import TFile
from matplotlib import pylab as plt
import tqdm
#change time / primaries
cu_thick_um=np.array([1,4,8,12,16,20,40,50,75,100,200,300,350,400])
field_s=np.array(["30x30","40x40"])
sim_type=["Gammas","Electrons","ElectronsFromPhS1"]
material=["Copper","Aluminium"]
# cu_thick_um=(1,2)
start_pos_mm=470
start_pos_um=470*1000
pass_thick_um=10
epi_thick_um=10
bulk_thick_um=700
airbox_thick_um=1000

# _gamma=np.array([])
# all_integrals_elec=np.array([])
# all_integrals_elecphs1=np.array([])

# for mat in material:
for sims in sim_type:
    all_integrals=np.array([])

    for field_sz in tqdm.tqdm(field_s):
        for thick in cu_thick_um:
            for filenum in range(1,201,1):
                filename=f"/work/lb8075/PhaseSpaces/PS3/PhS3BigSensor_v4_{sims}_{field_sz}/Epi-{thick}_um_Copper-{filenum}-Edep.root"
                fi=TFile(filename)
                try:
                    histo=fi.Get("histo")
                    inte=histo.Integral(105,145,105,145)
                    histo.Delete()
                    # del histo
                    # print(inte,sims,field_sz,thick,filenum)
                    all_integrals=np.append(all_integrals,inte)
                    # if("gamma" in sims):
                    #     all_integrals_gamma=np.append(all_integrals_gamma,inte)
                    # elif("PhS1" in sims):
                    #     all_integrals_elecphs1=np.append(all_integrals_elecphs1,inte)
                    # else:
                    #     all_integrals_elec=np.append(all_integrals_elec,inte)
                    # print("exists")
                except:
                    print("file is",filename)
                    print("!!!corrupt!!!")
                    
                if (fi.IsZombie()):
                    print("zombie")


                fi.Close()
                fi.Delete()

    plt.plot(all_integrals)
    plt.pause(0.01)
    input("")

# plt.plot(all_integrals_gamma)
# plt.pause(0.01)
# input("")
# plt.clf()
# plt.cla()
# plt.plot(all_integrals_gamma)
# plt.pause(0.01)
# input("")

# plt.clf()
# plt.cla()
# plt.plot(all_integrals_gamma)
# plt.pause(0.01)
# input("")