import numpy as np
from matplotlib import pylab as plt
from ROOT import TFile, TH2
from root_numpy import array2hist, hist2array, fill_hist, tree2array, root2array, list_trees
import matplotlib.cm as cm

thicknesses=np.array([50,100,200,300,350,400,500])#200,300,350,400,500
colors = iter(cm.gist_rainbow(np.linspace(0, 1, 4)))
fig,ax=plt.subplots(2,2,figsize=(8,6))
baseline=1
rebin=True
rebin_factor=5
paths=["PhS3DoseFromGamma_50um","PhS3DoseFromGamma_50um_plastic1cm"]
thick=50
for j,path in enumerate(paths):
	filepath="/work/lb8075/PhaseSpaces/"+str(path)

	filename=filepath+"/Total-Epi-30mm-no-bias-Edep.root"
	filey=TFile(filename)
	hist=filey.Get("histo")
	histnp=hist2array(hist)
	print(thick)
	prof_x=histnp[60:140,:].mean(axis=0)
	prof_y=histnp[:,60:140].mean(axis=1)

	# if (j==0):
	# 	baseline=histnp[15:30,70:130].mean()
	# print(baseline)
	# prof_x=prof_x/baseline
	# prof_y=prof_y/baseline
	print(len(prof_x))
	if (rebin):
		prof_x=prof_x.reshape(int(len(prof_x)/rebin_factor),rebin_factor).mean(axis=1)
		prof_y=prof_y.reshape(int(len(prof_y)/rebin_factor),rebin_factor).mean(axis=1)
	colorChoice=next(colors)
	if j==0:
		labelStr="none"
	else:
		labelStr="plastic"
	ax[0,0].plot(prof_x,color=colorChoice,label=labelStr)
	ax[0,1].plot(prof_y,color=colorChoice,label=labelStr)
	# ax[0,0].legend()

plt.pause(0.01)
input('wait')

#---
paths=["PhS3DoseFromElec_50um","PhS3DoseFromElec_50um_Plastic1cm"]
thick=50
for j,path in enumerate(paths):
	filepath="/work/lb8075/PhaseSpaces/"+str(path)

	filename=filepath+"/Total-Epi-30mm-no-bias-Edep.root"
	filey=TFile(filename)
	hist=filey.Get("histo")
	histnp=hist2array(hist)
	print(thick)
	prof_x=histnp[60:140,:].mean(axis=0)
	prof_y=histnp[:,60:140].mean(axis=1)

	# if (j==0):
	# 	baseline=histnp[15:30,70:130].mean()
	# print(baseline)
	# prof_x=prof_x/baseline
	# prof_y=prof_y/baseline
	if j==0:
		labelStr="none"
	else:
		labelStr="plastic"
	print(len(prof_x))
	if (rebin):
		prof_x=prof_x.reshape(int(len(prof_x)/rebin_factor),rebin_factor).mean(axis=1)
		prof_y=prof_y.reshape(int(len(prof_y)/rebin_factor),rebin_factor).mean(axis=1)
	colorChoice=next(colors)
	ax[1,0].plot(prof_x,color=colorChoice,label=labelStr)
	ax[1,1].plot(prof_y,color=colorChoice,label=labelStr)
	ax[0,0].legend()
	ax[1,0].legend()

plt.pause(0.01)
input('wait')
