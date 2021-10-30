import numpy as np
import math
import pandas as pd
from root_pandas import read_root, to_root
import uproot
from scipy import stats
# from matplotlib import pylab as plt
import argparse
import gc
from memory_profiler import profile

parser = argparse.ArgumentParser()
parser.add_argument('--field', help='field size')
parser.add_argument('--entries', help='entries to be generated')
parser.add_argument('--jobID', help='PBS job ID')
parser.add_argument('--filenum', help='file number for inputting multiple files into input phase space')
args = parser.parse_args()

@profile
def runthing(args):
	field_size=args.field
	PBS_ID=int(args.jobID)
	ents_gen=int(args.entries)
	n_file=int(args.filenum)
	filename=f"/work/lb8075/PhaseSpaces/PS2/PhS2_{field_size}_p1_Gamma_v3_highEn/Skimmed_output*1.root"
	print(f"input file: {filename}")
	ur=uproot.pandas.iterate(filename, "PhaseSpace", ['X','Y','dX','dY','Ekine'])
	mylist=list(ur)        
	dftot=pd.concat(mylist, ignore_index=True, sort=False  ,copy = False)

	print("read files")

	nparr=dftot.to_numpy()

	del ur
	del mylist
	del dftot

	gc.collect()

	values=nparr.T

	bandwidth=0.025
	events_to_be_generated=ents_gen   #1000000

	kde = stats.gaussian_kde(values,bw_method=bandwidth)
	print("generated KDE")

	del nparr
	del values

	gc.collect()

	for i in range(PBS_ID,PBS_ID+1):
		newsample = stats.gaussian_kde.resample(kde,events_to_be_generated)
		print("resampled KDE",i)
		del kde
		gc.collect()

		newsample=newsample.T
		newdf=pd.DataFrame(newsample,columns=['X','Y','dX','dY','Ekine'])
		del newsample
		gc.collect()
		newdf=newdf.astype('float32')

		newdf=newdf[(newdf['Ekine']>0)]
		newdf=newdf.astype('float32')

		newdf['dZ']=-1*pow(1.0-newdf['dX']*newdf['dX']-newdf['dY']*newdf['dY'],0.5)
		newdf=newdf.astype('float32')
		newdf=newdf[(newdf['dZ']<0)]

		newdf["Z"]=-0.0000005
		newdf=newdf.dropna(axis='index')
		newdf=newdf.astype('float32')
		newdf.to_root(f"/work/lb8075/PhaseSpaces/GenPhS2/Generated_PhS2_Gammas_highEn_{field_size}/generatedGamma_PhS2_{field_size}_{i}_file{n_file}.root", key='PhaseSpace')
		print("root file saved",i)

	print("Finished")
	return 0


runthing(args)

