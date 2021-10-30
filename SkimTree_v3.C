#include "TFile.h"
#include "TTree.h"
#include <iostream>

void SkimTree_v3(int file_num_start,int file_num_end){

   // gSystem->Load("$ROOTSYS/test/libEvent");
   for (int filenum=file_num_start;filenum<file_num_end;filenum++){
      //Get old file, old tree and set top branch address
      //string inFile="/work/lb8075/PhaseSpaces/PhS1AB_Gamma_ZeroBias/output-PhS_bias1_"+std::to_string(filenum)+".root";
      //string outFile="/work/lb8075/PhaseSpaces/PhS1AB_Gamma_ZeroBias/Skimmed_output-PhS_bias1_"+std::to_string(filenum)+".root";
      string inFile="/work/lb8075/PhaseSpaces/PS1/PhS1AB_Elec_ZeroBias_HighEn/output_"+std::to_string(filenum)+".root";
      string outFile="/work/lb8075/PhaseSpaces/PS1/PhS1AB_Elec_ZeroBias_HighEn/Skimmed_output_"+std::to_string(filenum)+".root";

      TFile *oldfile = new TFile(inFile.c_str());
      TTree *oldtree = (TTree*)oldfile->Get("PhaseSpace");
      const Long64_t nentries = oldtree->GetEntries();
      cout<<filenum<<endl;
      // float Ekine   = 0;
      // float Weight   = 0;
      // float X  = 0;
      // float Y   = 0;
      // float Z   = 0;
      // float dX  = 0;
      // float dY   = 0;
      // float dZ   = 0;
      // char ProductionVolume   = 0;
      // char CreatorProcess   = 0;
      //oldtree->SetBranchAddress("Ekine",&Ekine);
      //oldtree->SetBranchAddress("Weight",&Weight);
      // oldtree->SetBranchAddress("X",&X);
      // oldtree->SetBranchAddress("Y",&Y);
      // oldtree->SetBranchAddress("dX",&dX);
      // oldtree->SetBranchAddress("dY",&dY);
      // oldtree->SetBranchAddress("ProductionVolume",&ProductionVolume);
      // oldtree->SetBranchAddress("CreatorProcess",&CreatorProcess);
      oldtree->SetBranchStatus("Ekine",1);
      oldtree->SetBranchStatus("X",1);
      oldtree->SetBranchStatus("Y",1);
      oldtree->SetBranchStatus("dX",1);
      oldtree->SetBranchStatus("dY",1);
      oldtree->SetBranchStatus("dZ",1);
      oldtree->SetBranchStatus("ProductionVolume",0);
      oldtree->SetBranchStatus("Weight",1);
      oldtree->SetBranchStatus("CreatorProcess",0);
      //oldtree->SetBranchStatus("ParticleName",1);
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
      TTree *newtree = oldtree->CloneTree(nentries);
      //cout<<"nt"<<oldtree->GetEntries()<<endl;
      //Long64_t nentries=10000000;
      //cout<<oldtree->GetEntriesFast()<<endl;
     
     // for (Long64_t i=0;i<nentries; i++) {
     //    if (i%10000==0){cout<<i<<"  "<<nentries<<" "<<(i<nentries)<<endl;}
     //       
     //    oldtree->GetEntry(i);
     //    newtree->Fill();
     // }
 
      newfile->SetCompressionAlgorithm(ROOT::kLZMA);
      newfile->SetCompressionLevel(9);
      newtree->AutoSave();
      delete oldfile;
      delete newfile;
   }  
}


