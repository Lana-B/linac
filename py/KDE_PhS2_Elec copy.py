import numpy as np
import math
import pandas as pd
from root_pandas import read_root, to_root
import uproot
from scipy import stats
# from matplotlib import pylab as plt
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--field', help='foo help')
parser.add_argument('--entries', help='foo help')
parser.add_argument('--jobID', help='foo help')
parser.add_argument('--filenum', help='file number for inputting multiple files into input phase space')

args = parser.parse_args()
field_size=args.field
file_num=int(args.jobID)
ents_gen=int(args.entries)
n_file=int(args.filenum)

filename=f"/work/lb8075/PhaseSpaces/PhS2_{field_size}_p1_Elec_v3/output*.root"
print(f"input file: {filename}")
ur=uproot.pandas.iterate(filename, "PhaseSpace", ['X','Y','dX','dY','Ekine'])
mylist=list(ur)        
dftot=pd.concat(mylist, ignore_index=True, sort=False  ,copy = False)

print("read files")

nparr=dftot.to_numpy()
values=nparr.T

bandwidth=0.025
events_to_be_generated=ents_gen   #1000000

kde = stats.gaussian_kde(values,bw_method=bandwidth)
print("generated KDE")

for i in range(file_num,file_num+1):
	newsample = stats.gaussian_kde.resample(kde,events_to_be_generated)
	print("resampled KDE",i)

	newsample=newsample.T
	newdf=pd.DataFrame(newsample,columns=['X','Y','dX','dY','Ekine'])

	newdfsub=newdf[(newdf['Ekine']>0)]
	newdfsub['dZ']=-1*pow(1.0-newdfsub['dX']*newdfsub['dX']-newdfsub['dY']*newdfsub['dY'],0.5)
	newdfsub=newdfsub[(newdfsub['dZ']<0)]
	newdfsub["Z"]=-0.0000005
	newdfsub=newdfsub.dropna(axis='index')
	newdfsub=newdfsub.astype('float32')
	newdfsub.to_root(f"/work/lb8075/PhaseSpaces/Generated_PhS2_Electrons_{field_size}/generatedElectron_PhS2_v4_{field_size}_{i}_file{n_file}.root", key='PhaseSpace')
	print("root file saved",i)

print("Finished")
