import numpy as np
import math
#from matplotlib import pylab as plt
from ROOT import TTree, TFile, TH2D, TCanvas, TH1F, gROOT
from root_numpy import array2hist, hist2array, fill_hist, tree2array, root2array, list_trees

filename="../output/ClusterAllOne_main_phs1_gamma.root"
inputFile=TFile(filename)
tree=inputFile.Get("PhaseSpace")
list_trees(inputFile)
# Energy = hist2array(inputFile)
E_dep = root2array(tree, treename="dX")

plt.hist(E_kinetic)
plt.pause(0.01)
#print(E_kinetic)
#np.save('pythonArr', E_kinetic)
input("press enter to exit")
