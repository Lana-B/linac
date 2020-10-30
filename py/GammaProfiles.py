import numpy as np
from matplotlib import pylab as plt
from ROOT import TFile, TH2
from root_numpy import array2hist, hist2array, fill_hist, tree2array, root2array, list_trees
import matplotlib.cm as cm

thicknesses=np.array([50,100,200,300,350,400,500])#200,300,350,400,500
colors = iter(cm.gist_rainbow(np.linspace(0, 1, 7)))
fig,ax=plt.subplots(2,2,figsize=(8,6))
baseline=1
rebin=True
rebin_factor=5
for j,thick in enumerate(thicknesses):
	filepath="/work/lb8075/PhaseSpaces/PhS3DoseFromGamma_"+str(thick)+"um"

	filename=filepath+"/Total-Epi-30mm-no-bias-Edep.root"
	filey=TFile(filename)
	hist=filey.Get("histo")
	histnp=hist2array(hist)
	print(thick)
	prof_x=histnp[60:140,:].mean(axis=0)
	prof_y=histnp[:,60:140].mean(axis=1)

	if (j==0):
		baseline=histnp[15:30,70:130].mean()
	print(baseline)
	prof_x=prof_x/baseline
	prof_y=prof_y/baseline
	print(len(prof_x))
	if (rebin):
		prof_x=prof_x.reshape(int(len(prof_x)/rebin_factor),rebin_factor).mean(axis=1)
		prof_y=prof_y.reshape(int(len(prof_y)/rebin_factor),rebin_factor).mean(axis=1)
	colorChoice=next(colors)
	ax[0,0].plot(prof_x,color=colorChoice,label=str(thick)+"um")
	ax[0,1].plot(prof_y,color=colorChoice,label=str(thick)+"um")
	ax[0,0].legend()

	filepath_e="/work/lb8075/PhaseSpaces/PhS3DoseFromElec_"+str(thick)+"um"

	filename_e=filepath_e+"/Total-Epi-30mm-no-bias-Edep_ALLfiles.root"
	filey_e=TFile(filename_e)
	hist_e=filey_e.Get("histo")
	histnp_e=hist2array(hist_e)
	prof_x_e=histnp_e[60:140,:].mean(axis=0)
	prof_y_e=histnp_e[:,60:140].mean(axis=1)

	if (j==0):
		baseline_e=histnp_e[15:30,70:130].mean()
	print(baseline_e)
	prof_x_e=prof_x_e/baseline_e
	prof_y_e=prof_y_e/baseline_e
	print(len(prof_x_e))
	if (rebin):
		prof_x_e=prof_x_e.reshape(int(len(prof_x_e)/rebin_factor),rebin_factor).mean(axis=1)
		prof_y_e=prof_y_e.reshape(int(len(prof_y_e)/rebin_factor),rebin_factor).mean(axis=1)
	ax[1,0].plot(prof_x_e,color=colorChoice,label=str(thick)+"um")
	ax[1,1].plot(prof_y_e,color=colorChoice,label=str(thick)+"um")

plt.pause(0.01)
input('wait')

