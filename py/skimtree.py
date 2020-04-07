from ROOT import TFile,TTree
import lzma
import pickle
import numpy as np

for filenum in range(1,2):
      inFile="../PhS2_5x5/output-lana2-PhS-e"+str(filenum)+".root";
      outFile="../PhS2_5x5/Shoutput-lana2-PhS-e"+str(filenum);

      oldfile = TFile(inFile);
      oldtree = oldfile.Get("PhaseSpace");
      nEntries=oldtree.GetEntries();
      Ekine=np.empty((1), dtype="float32")
      CreatorProcess=np.empty((1), dtype="str")

      oldtree.SetBranchAddress( "Ekine", Ekine )
      oldtree.SetBranchAddress( "CreatorProcess", CreatorProcess )

      oldtree.SetBranchStatus("Ekine",1);
      oldtree.SetBranchStatus("X",1);
      oldtree.SetBranchStatus("Y",1);
      oldtree.SetBranchStatus("dX",1);
      oldtree.SetBranchStatus("dY",1);
      oldtree.SetBranchStatus("dZ",1);
      oldtree.SetBranchStatus("ProductionVolume",1);
      oldtree.SetBranchStatus("Weight",1);
      oldtree.SetBranchStatus("CreatorProcess",1);
      oldtree.SetBranchStatus("Z",0);
      oldtree.SetBranchStatus("AtomicNumber",0);
      oldtree.SetBranchStatus("Mass",0);
      oldtree.SetBranchStatus("ProcessDefinedStep",0);
      oldtree.SetBranchStatus("TrackID",0);
      oldtree.SetBranchStatus("ParentID",0);
      oldtree.SetBranchStatus("EventID",0);
      oldtree.SetBranchStatus("RunID",0);


      #Create a new file + a clone of old tree in new file
      newfile = TFile(str(outFile+".root"),"RECREATE");
      newtree = oldtree.CloneTree(0);
      for j in range(0,nEntries+1):
         oldtree.GetEntry(j);
         # print(j)
         # print(oldtree.Ekine)
         newtree.Fill();

      newtree.AutoSave()

      with lzma.open(str(outFile+".pkl"), "w") as f:
            pickle.dump(newtree, f)


      oldfile.Close()
      newfile.Close()



