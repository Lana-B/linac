import numpy as np
import math
# from matplotlib import pylab as plt
import pandas as pd
from root_pandas import read_root, to_root
import uproot
# from root_numpy import array2tree
# from ROOT import TFile,TTree,TObject

from scipy import stats

dftot = pd.read_pickle("electron10x10.pkl")

print("read files")

nparr=dftot.to_numpy()
values=nparr.T

kde = stats.gaussian_kde(values,bw_method=0.01)
print("generated KDE")

for i in range(1,5):
	newsample = stats.gaussian_kde.resample(kde,20000000)
	print("resampled KDE",i)

	newsample=newsample.T
	newdf=pd.DataFrame(newsample,columns=['X','Y','dX','dY','Weight','Ekine'])

	newdfsub=newdf[(newdf['Weight']>0)&(newdf['Ekine']>0)&(abs(newdf['X'])<30)&(abs(newdf['Y'])<30)]
	newdfsub['dZ']=-1*pow(1.0-newdfsub['dX']*newdfsub['dX']-newdfsub['dY']*newdfsub['dY'],0.5)
	newdfsub["Z"]=-0.0000005
	newdfsub=newdfsub.dropna(axis='index')
	newdfsub=newdfsub.astype('float32')
	newdfsub.to_root("generatedElectronSkimmed30mm"+str(i)+".root", key='PhaseSpace')
	print("root file saved",i)

print("Finished")
