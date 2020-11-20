#include "TFile.h"
#include "TTree.h"

void SkimTree_v2() {

   // gSystem->Load("$ROOTSYS/test/libEvent");
   for (int filenum=1;filenum<2;filenum++){
      //Get old file, old tree and set top branch address
      string inFile="/work/lb8075/PhaseSpaces/PhS1AB_Gamma_ZeroBias/output-PhS_bias1_"+std::to_string(filenum)+".root";
      string outFile="/work/lb8075/PhaseSpaces/PhS1AB_Gamma_ZeroBias/Skimmed_output-PhS_bias1_"+std::to_string(filenum)+".root";

      TFile *oldfile = new TFile(inFile.c_str());
      TTree *oldtree = (TTree*)oldfile->Get("PhaseSpace");
      Long64_t nentries = oldtree->GetEntries();
      cout<<nentries<<endl;
      float Ekine   = 0;
      //float Weight   = 0;
      float X  = 0;
      float Y   = 0;
      float Z   = 0;
      float dX  = 0;
      float dY   = 0;
      float dZ   = 0;
      char ProductionVolume   = 0;
      char CreatorProcess   = 0;
      oldtree->SetBranchAddress("Ekine",&Ekine);
      //oldtree->SetBranchAddress("Weight",&Weight);
      oldtree->SetBranchAddress("X",&X);
      oldtree->SetBranchAddress("Y",&Y);
      oldtree->SetBranchAddress("dX",&dX);
      oldtree->SetBranchAddress("dY",&dY);
      oldtree->SetBranchAddress("ProductionVolume",&ProductionVolume);
      oldtree->SetBranchAddress("CreatorProcess",&CreatorProcess);
      oldtree->SetBranchStatus("Ekine",1);
      oldtree->SetBranchStatus("X",1);
      oldtree->SetBranchStatus("Y",1);
      oldtree->SetBranchStatus("dX",1);
      oldtree->SetBranchStatus("dY",1);
      oldtree->SetBranchStatus("dZ",1);
      oldtree->SetBranchStatus("ProductionVolume",1);
      oldtree->SetBranchStatus("Weight",0);
      oldtree->SetBranchStatus("CreatorProcess",1);
      oldtree->SetBranchStatus("Z",1);
      oldtree->SetBranchStatus("AtomicNumber",0);
      oldtree->SetBranchStatus("Mass",0);
      oldtree->SetBranchStatus("ProcessDefinedStep",0);
      oldtree->SetBranchStatus("TrackID",0);
      oldtree->SetBranchStatus("ParentID",0);
      oldtree->SetBranchStatus("EventID",0);
      oldtree->SetBranchStatus("RunID",0);
      oldtree->SetBranchStatus("TOut",0);
      oldtree->SetBranchStatus("TProd",0);

      //Create a new file + a clone of old tree in new file
      TFile *newfile = new TFile(outFile.c_str(),"recreate");
      TTree *newtree = oldtree->CloneTree(0);

      for (Long64_t i=0;i<nentries; i++) {
         oldtree->GetEntry(i);
       //  if (abs(X)<10.0 && abs(Y)<10.0){
         newtree->Fill();
            // cout<<"ja"<<endl;
         //}
         //else{
            // cout<<"nein"<<endl;
        // }
         
      }
 
      newfile->SetCompressionAlgorithm(ROOT::kLZMA);
      newfile->SetCompressionLevel(9);
      newtree->AutoSave();
      delete oldfile;
      delete newfile;
   }  
}


