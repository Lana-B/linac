

void SkimTree_ultimate() {

   // gSystem->Load("$ROOTSYS/test/libEvent");
   //Get old file, old tree and set top branch address
   string inFile="/work/lb8075/PhaseSpaces/PhS2_10x10_p1_Elec_v2/Skimmed_output_500files.root";
   string outFile="/work/lb8075/PhaseSpaces/PhS2_10x10_p1_Elec_v2/Skimmed_output_500files_reskimmed.root";

   TFile *oldfile = new TFile(inFile.c_str());
   TTree *oldtree = (TTree*)oldfile->Get("PhaseSpace");
   const Long64_t nentries = oldtree->GetEntries();

   oldtree->SetBranchStatus("Ekine",1);
   oldtree->SetBranchStatus("X",1);
   oldtree->SetBranchStatus("Y",1);
   oldtree->SetBranchStatus("dX",1);
   oldtree->SetBranchStatus("dY",1);
   oldtree->SetBranchStatus("dZ",1);
   oldtree->SetBranchStatus("Weight",0);
   oldtree->SetBranchStatus("Z",0);
   oldtree->SetBranchStatus("ParticleName",0);
   oldtree->SetBranchStatus("ProductionVolume",0);
   oldtree->SetBranchStatus("CreatorProcess",0);
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


