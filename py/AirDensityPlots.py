import numpy as np
from matplotlib import pylab as plt
from ROOT import TFile, TH2
from root_numpy import array2hist, hist2array, fill_hist, tree2array, root2array, list_trees
import matplotlib.cm as cm

colors = cm.gist_rainbow(np.linspace(0, 1, 4))
fig,ax=plt.subplots(1,1,figsize=(8,6))
fig_e,ax_e=plt.subplots(1,1,figsize=(8,6))
rebin=True
rebin_factor=2

#---
paths=[ \
"100umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Aluminium_peaks-under-BlackOut_0mm_AirPp9", \
"100umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Aluminium_peaks-under-BlackOut_10mm_AirPp9", \
"100umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Aluminium_peaks-under-BlackOut_0mm_AirP1p4", \
"100umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Aluminium_peaks-under-BlackOut_10mm_AirP1p4" \
]
0

for j,path in enumerate(paths):

	filepath_e="/work/lb8075/PhaseSpaces/Flex/PhS3DoseFromElec_"+str(path)
	filepath_g="/work/lb8075/PhaseSpaces/Flex/PhS3DoseFromGamma_"+str(path)

	filename_e=filepath_e+"/Total-Edep.root"
	file_e=TFile(filename_e)
	hist_e=file_e.Get("histo")
	histnp_e=hist2array(hist_e)
	# print(thick)
	prof_x_e=histnp_e[60:140,:].mean(axis=0)
	prof_y_e=histnp_e[:,60:140].mean(axis=1)

	filename_g=filepath_g+"/Total-Edep.root"
	file_g=TFile(filename_g)
	hist_g=file_g.Get("histo")
	histnp_g=hist2array(hist_g)
	# print(thick)
	prof_x_g=histnp_g[60:140,:].mean(axis=0)
	prof_y_g=histnp_g[:,60:140].mean(axis=1)

	prof_x_e=prof_x_e*986/1855
	prof_y_e=prof_y_e*986/1855

	# if (j==0):
	# 	baseline=histnp[15:30,70:130].mean()
	# print(baseline)
	# prof_x=prof_x/baseline
	# prof_y=prof_y/baseline

	labelStr=path.split("_")[7]+" "+path.split("_")[8][4:]
	if (rebin):
		prof_x_e=prof_x_e.reshape(int(len(prof_x_e)/rebin_factor),rebin_factor).mean(axis=1)
		prof_y_e=prof_y_e.reshape(int(len(prof_y_e)/rebin_factor),rebin_factor).mean(axis=1)


		prof_x_g=prof_x_g.reshape(int(len(prof_x_g)/rebin_factor),rebin_factor).mean(axis=1)
		prof_y_g=prof_y_g.reshape(int(len(prof_y_g)/rebin_factor),rebin_factor).mean(axis=1)

	if ("AirPp9" in path):
		lstyle="dashed"
		# continue
	else:
		lstyle="solid"

	if ("10mm" in path):
		colorChoice="red"
		# continue
	else:
		colorChoice="blue"

	ax.plot(prof_x_g,color=colorChoice,label=labelStr,linestyle=lstyle)
	ax_e.plot(prof_x_e,color=colorChoice,label=labelStr,linestyle=lstyle)
	# ax[1,1].plot(prof_y,color=colorChoice,label=labelStr,linestyle=lstyle)
	ax.legend()
	ax_e.legend()
	# ax[1,0].legend()


fig.show()
fig_e.show()



plt.pause(0.01)
input('wait')
