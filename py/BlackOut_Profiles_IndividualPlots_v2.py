import numpy as np
from matplotlib import pylab as plt
from ROOT import TFile, TH2
from root_numpy import array2hist, hist2array, fill_hist, tree2array, root2array, list_trees
import matplotlib.cm as cm

thicknesses=np.array([50,100,200,300,350,400,500])#200,300,350,400,500
colors = cm.gist_rainbow(np.linspace(0, 1, 8))

# fig_peaks_under_BO_0mm,ax_peaks_under_BO_0mm=plt.subplots(2,2,figsize=(8,6))
# fig_peaks_under_BO_10mm,ax_peaks_under_BO_10mm=plt.subplots(2,2,figsize=(8,6))
# fig.suptitle("blackout under peaks")
# fig_peaks_under_BO_10mm.suptitle("peaks under blackout 10mm")
# fig_peaks_under_BO_0mm.suptitle("peaks under blackout 0mm")

baseline=1
rebin=False
rebin_factor=4


#---
paths=["50umpeak_20umBlackOut_peakMat_Lead_BOmat_Polyethylene_BlackOut-under-peaks", \
"50umpeak_20umBlackOut_peakMat_Lead_BOmat_Aluminium_BlackOut-under-peaks", \
"50umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_BlackOut-under-peaks", \
"50umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Aluminium_BlackOut-under-peaks", \
"50umpeak_300umBlackOut_peakMat_Lead_BOmat_Polyethylene_BlackOut-under-peaks", \
"50umpeak_300umBlackOut_peakMat_Lead_BOmat_Aluminium_BlackOut-under-peaks", \
"50umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_BlackOut-under-peaks", \
"50umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Aluminium_BlackOut-under-peaks", \
"100umpeak_20umBlackOut_peakMat_Lead_BOmat_Polyethylene_BlackOut-under-peaks", \
"100umpeak_20umBlackOut_peakMat_Lead_BOmat_Aluminium_BlackOut-under-peaks", \
"100umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_BlackOut-under-peaks", \
"100umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Aluminium_BlackOut-under-peaks", \
"100umpeak_300umBlackOut_peakMat_Lead_BOmat_Polyethylene_BlackOut-under-peaks", \
"100umpeak_300umBlackOut_peakMat_Lead_BOmat_Aluminium_BlackOut-under-peaks", \
"100umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_BlackOut-under-peaks", \
"100umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Aluminium_BlackOut-under-peaks", \
"50umpeak_20umBlackOut_peakMat_Lead_BOmat_Polyethylene_peaks-under-BlackOut_0mm", \
"50umpeak_20umBlackOut_peakMat_Lead_BOmat_Polyethylene_peaks-under-BlackOut_10mm", \
"50umpeak_20umBlackOut_peakMat_Lead_BOmat_Aluminium_peaks-under-BlackOut_0mm", \
"50umpeak_20umBlackOut_peakMat_Lead_BOmat_Aluminium_peaks-under-BlackOut_10mm", \
"50umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_peaks-under-BlackOut_0mm", \
"50umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_peaks-under-BlackOut_10mm", \
"50umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Aluminium_peaks-under-BlackOut_0mm", \
"50umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Aluminium_peaks-under-BlackOut_10mm", \
"50umpeak_300umBlackOut_peakMat_Lead_BOmat_Polyethylene_peaks-under-BlackOut_0mm", \
"50umpeak_300umBlackOut_peakMat_Lead_BOmat_Polyethylene_peaks-under-BlackOut_10mm", \
"50umpeak_300umBlackOut_peakMat_Lead_BOmat_Aluminium_peaks-under-BlackOut_0mm", \
"50umpeak_300umBlackOut_peakMat_Lead_BOmat_Aluminium_peaks-under-BlackOut_10mm", \
"50umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_peaks-under-BlackOut_0mm", \
"50umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_peaks-under-BlackOut_10mm", \
"50umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Aluminium_peaks-under-BlackOut_0mm", \
"50umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Aluminium_peaks-under-BlackOut_10mm", \
"100umpeak_20umBlackOut_peakMat_Lead_BOmat_Polyethylene_peaks-under-BlackOut_0mm", \
"100umpeak_20umBlackOut_peakMat_Lead_BOmat_Polyethylene_peaks-under-BlackOut_10mm", \
"100umpeak_20umBlackOut_peakMat_Lead_BOmat_Aluminium_peaks-under-BlackOut_0mm", \
"100umpeak_20umBlackOut_peakMat_Lead_BOmat_Aluminium_peaks-under-BlackOut_10mm", \
"100umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_peaks-under-BlackOut_0mm", \
"100umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_peaks-under-BlackOut_10mm", \
"100umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Aluminium_peaks-under-BlackOut_0mm", \
"100umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Aluminium_peaks-under-BlackOut_10mm", \
"100umpeak_300umBlackOut_peakMat_Lead_BOmat_Polyethylene_peaks-under-BlackOut_0mm", \
"100umpeak_300umBlackOut_peakMat_Lead_BOmat_Polyethylene_peaks-under-BlackOut_10mm", \
"100umpeak_300umBlackOut_peakMat_Lead_BOmat_Aluminium_peaks-under-BlackOut_0mm", \
"100umpeak_300umBlackOut_peakMat_Lead_BOmat_Aluminium_peaks-under-BlackOut_10mm", \
"100umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_peaks-under-BlackOut_0mm", \
"100umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_peaks-under-BlackOut_10mm", \
"100umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Aluminium_peaks-under-BlackOut_0mm", \
"100umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Aluminium_peaks-under-BlackOut_10mm"]
# thick=50

i1=0
i2=0
i3=0
fig,ax=plt.subplots(3,2,figsize=(8,6))

for j,path in enumerate(paths):

	if "Lead" in path:
		continue
	if (("300umBlackOut" in path) and ("BOmat_Aluminium" in path)):
		continue
	if (\
		("50umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_BlackOut-under-peaks" in path) or \
		("50umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_BlackOut-under-peaks" in path) or \
		("100umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_BlackOut-under-peaks" in path) or \
		("100umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Aluminium_BlackOut-under-peaks" in path) or \
		("100umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_BlackOut-under-peaks" in path) or \
		("50umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_peaks-under-BlackOut_0mm" in path) \
		# ("100umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Aluminium_peaks-under-BlackOut_0mm" in path) or \
		):
		continue

	pathsplit=path.split("_")
	pathsplitstr=f"{pathsplit[0]}{pathsplit[3]} {pathsplit[1]}{pathsplit[5]} {pathsplit[6:]}"
	fig.suptitle(pathsplitstr,fontsize=10)
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

	# if (j==0):
	baseline_e=histnp_e[15:30,70:130].mean()
	prof_x_e_base=prof_x_e/baseline_e
	prof_y_e_base=prof_y_e/baseline_e

	baseline_g=histnp_g[15:30,70:130].mean()
	prof_x_g_base=prof_x_g/baseline_g
	prof_y_g_base=prof_y_g/baseline_g

	colorChoice="Red"
	lstyle="solid"

	labelStr=path[17:-25]
	prof_x_e=prof_x_e*10
	# prof_y_e=prof_y_e
	# print(len(prof_x_w))
	if (rebin):
		prof_x_e=prof_x_e.reshape(int(len(prof_x_e)/rebin_factor),rebin_factor).mean(axis=1)
		prof_y_e=prof_y_e.reshape(int(len(prof_y_e)/rebin_factor),rebin_factor).mean(axis=1)


		prof_x_g=prof_x_g.reshape(int(len(prof_x_g)/rebin_factor),rebin_factor).mean(axis=1)
		prof_y_g=prof_y_g.reshape(int(len(prof_y_g)/rebin_factor),rebin_factor).mean(axis=1)



	ax[1,0].plot(prof_x_e,color=colorChoice,label=labelStr,linestyle=lstyle)
	ax[1,1].plot(prof_x_e_base,color=colorChoice,label=labelStr,linestyle=lstyle)
	ax[1,0].set_ylim(0.6,1)
	ax[1,1].set_ylim(0.85,1.15)
	# ax[1,1].plot(prof_y_e,color=colorChoice,label=labelStr,linestyle=lstyle)

	ax[0,0].plot(prof_x_g,color=colorChoice,label=labelStr,linestyle=lstyle)
	ax[0,1].plot(prof_x_g_base,color=colorChoice,label=labelStr,linestyle=lstyle)
	# ax[0,1].plot(prof_y_g,color=colorChoice,label=labelStr,linestyle=lstyle)
	ax[0,0].set_ylim(0.5,1.3)
	ax[0,1].set_ylim(0.9,1.6)

	# ax[2,0].plot(prof_x_g,color=colorChoice,label=labelStr,linestyle=lstyle)
	# ax[2,1].plot(prof_y_g,color=colorChoice,label=labelStr,linestyle=lstyle)
	ax[2,0].plot(prof_x_e+prof_x_g,color="green",label=labelStr,linestyle=lstyle)
	ax[2,1].plot((prof_x_g/prof_x_e),color="green",label=labelStr,linestyle=lstyle)
	# ax[2,1].plot(prof_y_e+prof_y_g,color="green",label=labelStr,linestyle=lstyle)
	ax[2,0].set_ylim(1.1,1.8)
	ax[2,1].set_ylim(0.6,1.7)


	i3+=1


	plt.pause(0.01)
	plt.savefig("plots/"+path+"plot.png")
	# input(path)
	# plt.clf()
	ax[1,0].cla()
	ax[1,1].cla()
	ax[0,0].cla()
	ax[0,1].cla()
	ax[2,0].cla()
	ax[2,1].cla()
