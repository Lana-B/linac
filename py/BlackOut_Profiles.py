import numpy as np
from matplotlib import pylab as plt
from ROOT import TFile, TH2
from root_numpy import array2hist, hist2array, fill_hist, tree2array, root2array, list_trees
import matplotlib.cm as cm

thicknesses=np.array([50,100,200,300,350,400,500])#200,300,350,400,500
colors = cm.gist_rainbow(np.linspace(0, 1, 8))
fig,ax=plt.subplots(2,2,figsize=(8,6))

fig_peaks_under_BO_0mm,ax_peaks_under_BO_0mm=plt.subplots(2,2,figsize=(8,6))
fig_peaks_under_BO_10mm,ax_peaks_under_BO_10mm=plt.subplots(2,2,figsize=(8,6))
fig.suptitle("blackout under peaks")
fig_peaks_under_BO_10mm.suptitle("peaks under blackout 10mm")
fig_peaks_under_BO_0mm.suptitle("peaks under blackout 0mm")

baseline=1
rebin=False
rebin_factor=5
paths=[ \
"PhS3DoseFromGamma_50umpeak_20umBlackOut_peakMat_Lead_BOmat_Polyethylene_BlackOut-under-peaks", \
"PhS3DoseFromGamma_50umpeak_20umBlackOut_peakMat_Lead_BOmat_Aluminium_BlackOut-under-peaks", \
"PhS3DoseFromGamma_50umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_BlackOut-under-peaks", \
"PhS3DoseFromGamma_50umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Aluminium_BlackOut-under-peaks", \
"PhS3DoseFromGamma_50umpeak_300umBlackOut_peakMat_Lead_BOmat_Polyethylene_BlackOut-under-peaks", \
"PhS3DoseFromGamma_50umpeak_300umBlackOut_peakMat_Lead_BOmat_Aluminium_BlackOut-under-peaks", \
"PhS3DoseFromGamma_50umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_BlackOut-under-peaks", \
"PhS3DoseFromGamma_50umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Aluminium_BlackOut-under-peaks", \
"PhS3DoseFromGamma_100umpeak_20umBlackOut_peakMat_Lead_BOmat_Polyethylene_BlackOut-under-peaks", \
"PhS3DoseFromGamma_100umpeak_20umBlackOut_peakMat_Lead_BOmat_Aluminium_BlackOut-under-peaks", \
"PhS3DoseFromGamma_100umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_BlackOut-under-peaks", \
"PhS3DoseFromGamma_100umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Aluminium_BlackOut-under-peaks", \
"PhS3DoseFromGamma_100umpeak_300umBlackOut_peakMat_Lead_BOmat_Polyethylene_BlackOut-under-peaks", \
"PhS3DoseFromGamma_100umpeak_300umBlackOut_peakMat_Lead_BOmat_Aluminium_BlackOut-under-peaks", \
"PhS3DoseFromGamma_100umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_BlackOut-under-peaks", \
"PhS3DoseFromGamma_100umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Aluminium_BlackOut-under-peaks", \
"PhS3DoseFromGamma_50umpeak_20umBlackOut_peakMat_Lead_BOmat_Polyethylene_peaks-under-BlackOut_0mm", \
"PhS3DoseFromGamma_50umpeak_20umBlackOut_peakMat_Lead_BOmat_Polyethylene_peaks-under-BlackOut_10mm", \
"PhS3DoseFromGamma_50umpeak_20umBlackOut_peakMat_Lead_BOmat_Aluminium_peaks-under-BlackOut_0mm", \
"PhS3DoseFromGamma_50umpeak_20umBlackOut_peakMat_Lead_BOmat_Aluminium_peaks-under-BlackOut_10mm", \
"PhS3DoseFromGamma_50umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_peaks-under-BlackOut_0mm", \
"PhS3DoseFromGamma_50umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_peaks-under-BlackOut_10mm", \
"PhS3DoseFromGamma_50umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Aluminium_peaks-under-BlackOut_0mm", \
"PhS3DoseFromGamma_50umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Aluminium_peaks-under-BlackOut_10mm", \
"PhS3DoseFromGamma_50umpeak_300umBlackOut_peakMat_Lead_BOmat_Polyethylene_peaks-under-BlackOut_0mm", \
"PhS3DoseFromGamma_50umpeak_300umBlackOut_peakMat_Lead_BOmat_Polyethylene_peaks-under-BlackOut_10mm", \
"PhS3DoseFromGamma_50umpeak_300umBlackOut_peakMat_Lead_BOmat_Aluminium_peaks-under-BlackOut_0mm", \
"PhS3DoseFromGamma_50umpeak_300umBlackOut_peakMat_Lead_BOmat_Aluminium_peaks-under-BlackOut_10mm", \
"PhS3DoseFromGamma_50umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_peaks-under-BlackOut_0mm", \
"PhS3DoseFromGamma_50umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_peaks-under-BlackOut_10mm", \
"PhS3DoseFromGamma_50umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Aluminium_peaks-under-BlackOut_0mm", \
"PhS3DoseFromGamma_50umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Aluminium_peaks-under-BlackOut_10mm", \
"PhS3DoseFromGamma_100umpeak_20umBlackOut_peakMat_Lead_BOmat_Polyethylene_peaks-under-BlackOut_0mm", \
"PhS3DoseFromGamma_100umpeak_20umBlackOut_peakMat_Lead_BOmat_Polyethylene_peaks-under-BlackOut_10mm", \
"PhS3DoseFromGamma_100umpeak_20umBlackOut_peakMat_Lead_BOmat_Aluminium_peaks-under-BlackOut_0mm", \
"PhS3DoseFromGamma_100umpeak_20umBlackOut_peakMat_Lead_BOmat_Aluminium_peaks-under-BlackOut_10mm", \
"PhS3DoseFromGamma_100umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_peaks-under-BlackOut_0mm", \
"PhS3DoseFromGamma_100umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_peaks-under-BlackOut_10mm", \
"PhS3DoseFromGamma_100umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Aluminium_peaks-under-BlackOut_0mm", \
"PhS3DoseFromGamma_100umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Aluminium_peaks-under-BlackOut_10mm", \
"PhS3DoseFromGamma_100umpeak_300umBlackOut_peakMat_Lead_BOmat_Polyethylene_peaks-under-BlackOut_0mm", \
"PhS3DoseFromGamma_100umpeak_300umBlackOut_peakMat_Lead_BOmat_Polyethylene_peaks-under-BlackOut_10mm", \
"PhS3DoseFromGamma_100umpeak_300umBlackOut_peakMat_Lead_BOmat_Aluminium_peaks-under-BlackOut_0mm", \
"PhS3DoseFromGamma_100umpeak_300umBlackOut_peakMat_Lead_BOmat_Aluminium_peaks-under-BlackOut_10mm", \
"PhS3DoseFromGamma_100umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_peaks-under-BlackOut_0mm", \
"PhS3DoseFromGamma_100umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_peaks-under-BlackOut_10mm", \
"PhS3DoseFromGamma_100umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Aluminium_peaks-under-BlackOut_0mm", \
"PhS3DoseFromGamma_100umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Aluminium_peaks-under-BlackOut_10mm" \
]
# thick=50


i1=0
i2=0
i3=0

for j,path in enumerate(paths):
	if ("Lead" in path):
		continue
	filepath="/work/lb8075/PhaseSpaces/Flex/"+str(path)


	filename=filepath+"/Total-Edep.root"
	filey=TFile(filename)
	hist=filey.Get("histo")
	histnp=hist2array(hist)
	# print(thick)
	prof_x=histnp[60:140,:].mean(axis=0)
	prof_y=histnp[:,60:140].mean(axis=1)

	# if (j==0):
	# 	baseline=histnp[15:30,70:130].mean()
	# print(baseline)
	# prof_x=prof_x/baseline
	# prof_y=prof_y/baseline

	labelStr=path[17:-25]
	print(len(prof_x))
	if (rebin):
		prof_x=prof_x.reshape(int(len(prof_x)/rebin_factor),rebin_factor).mean(axis=1)
		prof_y=prof_y.reshape(int(len(prof_y)/rebin_factor),rebin_factor).mean(axis=1)



	if ("BOmat_Alum" in path):
		lstyle="dashed"
		# continue
	else:
		lstyle="solid"

	if("_0mm" in path):
		colorChoice=colors[i1]

		ax_peaks_under_BO_0mm[0,0].plot(prof_x,color=colorChoice,label=labelStr,linestyle=lstyle)
		ax_peaks_under_BO_0mm[0,1].plot(prof_y,color=colorChoice,label=labelStr,linestyle=lstyle)
		# ax_peaks_under_BO_0mm[0,0].legend()
		# ax_peaks_under_BO_0mm[0,1].legend()
		i1+=1

	elif("_10mm" in path):
		colorChoice=colors[i2]
		ax_peaks_under_BO_10mm[0,0].plot(prof_x,color=colorChoice,label=labelStr,linestyle=lstyle)
		ax_peaks_under_BO_10mm[0,1].plot(prof_y,color=colorChoice,label=labelStr,linestyle=lstyle)
		# ax_peaks_under_BO_10mm[0,0].legend()
		# ax_peaks_under_BO_10mm[0,1].legend()
		i2+=1

	else:
		colorChoice=colors[i3]
		ax[0,0].plot(prof_x,color=colorChoice,label=labelStr,linestyle=lstyle)
		ax[0,1].plot(prof_y,color=colorChoice,label=labelStr,linestyle=lstyle)
		# ax[0,0].legend()
		# ax[0,1].legend()
		i3+=1
		print (i3)

#---
paths=[ \
"PhS3DoseFromElec_50umpeak_20umBlackOut_peakMat_Lead_BOmat_Polyethylene_BlackOut-under-peaks", \
"PhS3DoseFromElec_50umpeak_20umBlackOut_peakMat_Lead_BOmat_Aluminium_BlackOut-under-peaks", \
"PhS3DoseFromElec_50umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_BlackOut-under-peaks", \
"PhS3DoseFromElec_50umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Aluminium_BlackOut-under-peaks", \
"PhS3DoseFromElec_50umpeak_300umBlackOut_peakMat_Lead_BOmat_Polyethylene_BlackOut-under-peaks", \
"PhS3DoseFromElec_50umpeak_300umBlackOut_peakMat_Lead_BOmat_Aluminium_BlackOut-under-peaks", \
"PhS3DoseFromElec_50umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_BlackOut-under-peaks", \
"PhS3DoseFromElec_50umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Aluminium_BlackOut-under-peaks", \
"PhS3DoseFromElec_100umpeak_20umBlackOut_peakMat_Lead_BOmat_Polyethylene_BlackOut-under-peaks", \
"PhS3DoseFromElec_100umpeak_20umBlackOut_peakMat_Lead_BOmat_Aluminium_BlackOut-under-peaks", \
"PhS3DoseFromElec_100umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_BlackOut-under-peaks", \
"PhS3DoseFromElec_100umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Aluminium_BlackOut-under-peaks", \
"PhS3DoseFromElec_100umpeak_300umBlackOut_peakMat_Lead_BOmat_Polyethylene_BlackOut-under-peaks", \
"PhS3DoseFromElec_100umpeak_300umBlackOut_peakMat_Lead_BOmat_Aluminium_BlackOut-under-peaks", \
"PhS3DoseFromElec_100umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_BlackOut-under-peaks", \
"PhS3DoseFromElec_100umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Aluminium_BlackOut-under-peaks", \
"PhS3DoseFromElec_50umpeak_20umBlackOut_peakMat_Lead_BOmat_Polyethylene_peaks-under-BlackOut_0mm", \
"PhS3DoseFromElec_50umpeak_20umBlackOut_peakMat_Lead_BOmat_Polyethylene_peaks-under-BlackOut_10mm", \
"PhS3DoseFromElec_50umpeak_20umBlackOut_peakMat_Lead_BOmat_Aluminium_peaks-under-BlackOut_0mm", \
"PhS3DoseFromElec_50umpeak_20umBlackOut_peakMat_Lead_BOmat_Aluminium_peaks-under-BlackOut_10mm", \
"PhS3DoseFromElec_50umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_peaks-under-BlackOut_0mm", \
"PhS3DoseFromElec_50umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_peaks-under-BlackOut_10mm", \
"PhS3DoseFromElec_50umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Aluminium_peaks-under-BlackOut_0mm", \
"PhS3DoseFromElec_50umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Aluminium_peaks-under-BlackOut_10mm", \
"PhS3DoseFromElec_50umpeak_300umBlackOut_peakMat_Lead_BOmat_Polyethylene_peaks-under-BlackOut_0mm", \
"PhS3DoseFromElec_50umpeak_300umBlackOut_peakMat_Lead_BOmat_Polyethylene_peaks-under-BlackOut_10mm", \
"PhS3DoseFromElec_50umpeak_300umBlackOut_peakMat_Lead_BOmat_Aluminium_peaks-under-BlackOut_0mm", \
"PhS3DoseFromElec_50umpeak_300umBlackOut_peakMat_Lead_BOmat_Aluminium_peaks-under-BlackOut_10mm", \
"PhS3DoseFromElec_50umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_peaks-under-BlackOut_0mm", \
"PhS3DoseFromElec_50umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_peaks-under-BlackOut_10mm", \
"PhS3DoseFromElec_50umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Aluminium_peaks-under-BlackOut_0mm", \
"PhS3DoseFromElec_50umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Aluminium_peaks-under-BlackOut_10mm", \
"PhS3DoseFromElec_100umpeak_20umBlackOut_peakMat_Lead_BOmat_Polyethylene_peaks-under-BlackOut_0mm", \
"PhS3DoseFromElec_100umpeak_20umBlackOut_peakMat_Lead_BOmat_Polyethylene_peaks-under-BlackOut_10mm", \
"PhS3DoseFromElec_100umpeak_20umBlackOut_peakMat_Lead_BOmat_Aluminium_peaks-under-BlackOut_0mm", \
"PhS3DoseFromElec_100umpeak_20umBlackOut_peakMat_Lead_BOmat_Aluminium_peaks-under-BlackOut_10mm", \
"PhS3DoseFromElec_100umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_peaks-under-BlackOut_0mm", \
"PhS3DoseFromElec_100umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_peaks-under-BlackOut_10mm", \
"PhS3DoseFromElec_100umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Aluminium_peaks-under-BlackOut_0mm", \
"PhS3DoseFromElec_100umpeak_20umBlackOut_peakMat_Aluminium_BOmat_Aluminium_peaks-under-BlackOut_10mm", \
"PhS3DoseFromElec_100umpeak_300umBlackOut_peakMat_Lead_BOmat_Polyethylene_peaks-under-BlackOut_0mm", \
"PhS3DoseFromElec_100umpeak_300umBlackOut_peakMat_Lead_BOmat_Polyethylene_peaks-under-BlackOut_10mm", \
"PhS3DoseFromElec_100umpeak_300umBlackOut_peakMat_Lead_BOmat_Aluminium_peaks-under-BlackOut_0mm", \
"PhS3DoseFromElec_100umpeak_300umBlackOut_peakMat_Lead_BOmat_Aluminium_peaks-under-BlackOut_10mm", \
"PhS3DoseFromElec_100umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_peaks-under-BlackOut_0mm", \
"PhS3DoseFromElec_100umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Polyethylene_peaks-under-BlackOut_10mm", \
"PhS3DoseFromElec_100umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Aluminium_peaks-under-BlackOut_0mm", \
"PhS3DoseFromElec_100umpeak_300umBlackOut_peakMat_Aluminium_BOmat_Aluminium_peaks-under-BlackOut_10mm" \
]
# thick=50
i1=0
i2=0
i3=0

for j,path in enumerate(paths):

	if ("Lead" in path):
		continue

	filepath="/work/lb8075/PhaseSpaces/Flex/"+str(path)

	filename=filepath+"/Total-Edep.root"
	filey=TFile(filename)
	hist=filey.Get("histo")
	histnp=hist2array(hist)
	# print(thick)
	prof_x=histnp[60:140,:].mean(axis=0)
	prof_y=histnp[:,60:140].mean(axis=1)

	# if (j==0):
	# 	baseline=histnp[15:30,70:130].mean()
	# print(baseline)
	# prof_x=prof_x/baseline
	# prof_y=prof_y/baseline

	labelStr=path[17:-25]
	print(len(prof_x))
	if (rebin):
		prof_x=prof_x.reshape(int(len(prof_x)/rebin_factor),rebin_factor).mean(axis=1)
		prof_y=prof_y.reshape(int(len(prof_y)/rebin_factor),rebin_factor).mean(axis=1)


	prof_x=prof_x*988/2090


	if ("BOmat_Alum" in path):
		lstyle="dashed"
		# continue
	else:
		lstyle="solid"

	if("_0mm" in path):
		colorChoice=colors[i1]

		ax_peaks_under_BO_0mm[1,0].plot(prof_x,color=colorChoice,label=labelStr,linestyle=lstyle)
		ax_peaks_under_BO_0mm[1,1].plot(prof_y,color=colorChoice,label=labelStr,linestyle=lstyle)
		# ax_peaks_under_BO_0mm[0,0].legend()
		# ax_peaks_under_BO_0mm[1,1].legend()
		i1+=1

	elif("_10mm" in path):
		colorChoice=colors[i2]
		ax_peaks_under_BO_10mm[1,0].plot(prof_x,color=colorChoice,label=labelStr,linestyle=lstyle)
		ax_peaks_under_BO_10mm[1,1].plot(prof_y,color=colorChoice,label=labelStr,linestyle=lstyle)
		# ax_peaks_under_BO_10mm[0,0].legend()
		# ax_peaks_under_BO_10mm[1,1].legend()
		i2+=1

	else:
		colorChoice=colors[i3]
		ax[1,0].plot(prof_x,color=colorChoice,label=labelStr,linestyle=lstyle)
		ax[1,1].plot(prof_y,color=colorChoice,label=labelStr,linestyle=lstyle)
		# ax[0,0].legend()
		# ax[1,0].legend()
		i3+=1
		print (i3)

fig.show()
fig_peaks_under_BO_0mm.show()
fig_peaks_under_BO_10mm.show()


plt.pause(0.01)
input('wait')
