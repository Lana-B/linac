import numpy as np
import os

#change time / primaries
cu_thick_um=np.array([1,4,8,12,16,20,40,50,75,100,200,300,350,400])
field_s=np.array(["10x10","20x20","30x30","40x40"])
sim_type=["Gammas","Electrons","ElectronsFromPhS1","Gammas_highEn","Electrons_highEn","ElectronsFromPhS1_highEn"]
material=["Copper","Aluminium"]
# cu_thick_um=(1,2)
start_pos_mm=470
start_pos_um=470*1000
pass_thick_um=7 #10
epi_thick_um=5 #10
bulk_thick_um=700
airbox_thick_um=1000
macroFolder="/home/lb8075/linac/mac/"
script="Main_PhS3_BigSensor_Flexible_airbox_wCopper.mac"

entries={}
#LowEn
entries["10x10_Gammas"]=5000000
entries["20x20_Gammas"]=21850000
entries["30x30_Gammas"]=52275000
entries["40x40_Gammas"]=99380000

entries["10x10_Electrons"]=1000000
entries["20x20_Electrons"]=5432990
entries["30x30_Electrons"]=12233680	
entries["40x40_Electrons"]=19901450

entries["10x10_ElectronsFromPhS1"]=1010000
entries["20x20_ElectronsFromPhS1"]=5487320
entries["30x30_ElectronsFromPhS1"]=12356020	
entries["40x40_ElectronsFromPhS1"]=20100470

#highEn
entries["10x10_Gammas_highEn"]=5000000
entries["20x20_Gammas_highEn"]=21404540
entries["30x30_Gammas_highEn"]=50192120
entries["40x40_Gammas_highEn"]=94018480

entries["10x10_Electrons_highEn"]=1000000
entries["20x20_Electrons_highEn"]=4172110
entries["30x30_Electrons_highEn"]=8339070	
entries["40x40_Electrons_highEn"]=12697550

entries["10x10_ElectronsFromPhS1_highEn"]=1000000
entries["20x20_ElectronsFromPhS1_highEn"]=5206910
entries["30x30_ElectronsFromPhS1_highEn"]=11634950
entries["40x40_ElectronsFromPhS1_highEn"]=18978380

def make_jobs_list(folder_path,thick,mat):
    temp_list=[]
    for i in range(1,201):
        file_path=f"{folder_path}/Epi-{thick}_um_{mat}-{i}-Edep.root"
        if (os.path.exists(file_path)):
            continue
        else:
            temp_list.append(str(i))
    final_list=",".join(temp_list)
    list_size=len(temp_list)
    return list_size,final_list

total_jobs=0

for mat in material:
    for sims in sim_type:
        for field_sz in field_s:
            for thick in cu_thick_um:

                cu_pos_um=start_pos_um-(thick/2.0)
                pass_pos_um=start_pos_um-(pass_thick_um/2.0)-thick
                epi_pos_um=start_pos_um-(epi_thick_um/2.0)-pass_thick_um-thick
                # print(start_pos_um,bulk_thick_um)
                bulk_pos_um=start_pos_um-(bulk_thick_um/2.0)-epi_thick_um-pass_thick_um-thick
                # print(start_pos_um,bulk_thick_um,bulk_pos_um)
                prim_ents=entries[f"{field_sz}_{sims}"]
                outputPath=f"/work/lb8075/PhaseSpaces/PS3/PhS3BigSensor_v6_{sims}_{field_sz}"
                n_lst,lst=make_jobs_list(outputPath,thick,mat)
                # print(outputPath,',',mat,',',thick,',',n_lst)
                if n_lst<1:
                    # print("nothing")
                    continue
                if n_lst==200:
                    # print("all files exist already")
                    continue
                else:
                    print(outputPath,',',mat,',',thick,',',n_lst,lst)
                if(mat=="Copper"):
                    total_jobs+=n_lst

                wall_t=""
                if 'Gamma' in sims:
                    particle='gamma'
                    inputFile=f"/work/lb8075/PhaseSpaces/GenPhS2/Generated_PhS2_{sims}_{field_sz}/generatedGamma_PhS2_{field_sz}"
                    wall_t="71:59:59"


                else:
                    particle='e-'
                    inputFile=f"/work/lb8075/PhaseSpaces/GenPhS2/Generated_PhS2_{sims}_{field_sz}/generatedElectron_PhS2_v4_{field_sz}"
                    wall_t="22:59:59"


                try:
                    os.lstat(f"{inputFile}_1_file1.root")
                    # print(f"yes .... {inputFile}")

                except:
                    print(f"no .... {inputFile}")
                with open(f"scripts/script_{mat}_{thick}_{sims}_{field_sz}_v6_redo.pbs", 'w') as f:

                    print("#!/bin/bash \n" 
                    f"#PBS -l walltime={wall_t}\n" 
                    "#PBS -j oe\n"
                    "#PBS -l select=1:ncpus=1\n"
                    "#PBS -l select=1:ncpus=1:mem=500mb\n"
                    f"#PBS -J {lst}\n"
                    # "#PBS -J 1-200 \n"

                    "#PBS -o /work/lb8075/job_logfiles\n",file=f)

                    print("module add apps/gate/8.2\n"
                    f"myScript=\"{script}\"\n"
                    f"cat {macroFolder}{script}\n"
                    "now=$(date)\n"
                    "echo \"Start: $now\"\n"
                    f"prim={prim_ents} #for elec\n",file=f)

                    outputPath=f"/work/lb8075/PhaseSpaces/PS3/PhS3BigSensor_v6_{sims}_{field_sz}"
                    try:
                        os.mkdir(outputPath)
                        print(f"creating {outputPath}")
                    except:
                        pass
                    #     print(f"{outputPath} path exists")   
                    # print(inputFile)
                    print(f"myCommand=\"cp {macroFolder}{script} .; Gate $myScript -a '[seed,$RANDOM$RANDOM$RANDOM] [primaries,$prim] [pathGateMaterials,/home/lb8075/linac/data/GateMaterials.db] [id,$PBS_ARRAY_INDEX] [pathOutputDose,{outputPath}] [inputParticleType,/gate/source/beam_g/setParticleType {particle}] [inputPhaseSpaceFile,{inputFile}] [grating_material,{mat}] [foil_thick_um,{thick}] [foil_z_um,{cu_pos_um}] [pass_z_um,{pass_pos_um}] [epi_z_um,{epi_pos_um}] [bulk_z_um,{bulk_pos_um}]'\" ",file=f)


                    print("eval $myCommand",file=f)
                    print("echo \"Completion time is $(date)\" ",file=f)
                    print("",file=f)


                    # print(f"hadd {outputPath}/Total-{thick}-um.root {outputPath}/Epi-{thick}_um_{mat}*Edep.root")
                    # print(f"myCommand=\"Gate $myScript -a '[seed,$RANDOM$RANDOM$RANDOM] [primaries,$prim] [pathGateMaterials,/home/lb8075/linac/data/GateMaterials.db] [id,$PBS_ARRAY_INDEX] [pathOutputDose,/work/lb8075/PhaseSpaces/PhS3BigSensor_v2_10x10_Gamma/] [inputParticleType,/gate/source/beam_g/setParticleType gamma] [inputPhaseSpaceFile,/work/lb8075/PhaseSpaces/Generated_PhS2_Gammas_10x10/generatedGamma_PhS2_10x10] [grating_material,Copper] [foil_thick_um,{thick}] [foil_z_um,{cu_pos_um}] [pass_z_um,{pass_pos_um}] [epi_z_um,{epi_pos_um}] [bulk_z_um,{bulk_pos_um}]'\" ",file=f)

                    
                    # print(f"myCommand=\"Gate $myScript -a '[seed,$RANDOM$RANDOM$RANDOM] [primaries,$prim] [pathGateMaterials,/home/lb8075/linac/data/GateMaterials.db] [id,$PBS_ARRAY_INDEX] [pathOutputDose,/work/lb8075/PhaseSpaces/PhS3BigSensor_v2_10x10_Elec/] [inputParticleType,/gate/source/beam_g/setParticleType e-] [inputPhaseSpaceFile,/work/lb8075/PhaseSpaces/Generated_PhS2_Electrons_10x10/generatedElectron_PhS2_v4_10x10] [grating_material,Silicon] [foil_thick_um,{thick}] [foil_z_um,{cu_pos_um}] [pass_z_um,{pass_pos_um}] [epi_z_um,{epi_pos_um}] [bulk_z_um,{bulk_pos_um}]'\" ",file=f)

                    # print(f"myCommand=\"Gate $myScript -a '[seed,$RANDOM$RANDOM$RANDOM] [primaries,$prim] [pathGateMaterials,/home/lb8075/linac/data/GateMaterials.db] [id,$PBS_ARRAY_INDEX] [pathOutputDose,/work/lb8075/PhaseSpaces/PhS3BigSensor_v2_10x10_Elec_ASL/] [inputParticleType,/gate/source/beam_g/setParticleType e-] [inputPhaseSpaceFile,/work/lb8075/PhaseSpaces/Generated_PhS2_Electrons_10x10_AlexSeaLevel/generatedElectron_PhS2_v4_10x10] [grating_material,Copper] [foil_thick_um,{thick}] [foil_z_um,{cu_pos_um}] [pass_z_um,{pass_pos_um}] [epi_z_um,{epi_pos_um}] [bulk_z_um,{bulk_pos_um}]'\" ",file=f)

                    # print(f"myCommand=\"Gate $myScript -a '[seed,$RANDOM$RANDOM$RANDOM] [primaries,$prim] [pathGateMaterials,/home/lb8075/linac/data/GateMaterials.db] [id,$PBS_ARRAY_INDEX] [pathOutputDose,/work/lb8075/PhaseSpaces/PhS3BigSensor_v2_10x10_Gamma_ASL/] [inputParticleType,/gate/source/beam_g/setParticleType gamma] [inputPhaseSpaceFile,/work/lb8075/PhaseSpaces/Generated_PhS2_Electrons_10x10_AlexSeaLevel/generatedElectron_PhS2_v4_10x10] [grating_material,Copper] [foil_thick_um,{thick}] [foil_z_um,{cu_pos_um}] [pass_z_um,{pass_pos_um}] [epi_z_um,{epi_pos_um}] [bulk_z_um,{bulk_pos_um}]'\" ",file=f)


                    # print(f"myCommand=\"Gate $myScript -a '[seed,$RANDOM$RANDOM$RANDOM] [primaries,$prim] [pathGateMaterials,/home/lb8075/linac/data/GateMaterials.db] [id,$PBS_ARRAY_INDEX] [pathOutputDose,/work/lb8075/PhaseSpaces/PhS3BigSensor_v2_10x10_Elec_fromPhS1Elec/] [inputParticleType,/gate/source/beam_g/setParticleType e-] [inputPhaseSpaceFile,/work/lb8075/PhaseSpaces/Generated_PhS2_Electrons_10x10_FromPhS1Elec/generatedElectron_PhS2_v4_10x10] [grating_material,Copper] [foil_thick_um,{thick}] [foil_z_um,{cu_pos_um}] [pass_z_um,{pass_pos_um}] [epi_z_um,{epi_pos_um}] [bulk_z_um,{bulk_pos_um}]'\" ",file=f)


                    # print("eval $myCommand",file=f)
                    # print("echo \"Completion time is $(date)\" ",file=f)
                    # print("",file=f)


                    # "myScript=\"/home/lb8075/linac/mac/Main_PhS3_BigSensor_Flexible_airbox_wCopper_gammaVac.mac\"\n"


            # print(f"myCommand=\"Gate $myScript -a '[seed,$RANDOM$RANDOM$RANDOM] [primaries,$prim] [pathGateMaterials,/home/lb8075/linac/data/GateMaterials.db] [id,$PBS_ARRAY_INDEX] [pathOutputDose,/work/lb8075/PhaseSpaces/PhS3BigSensor_v2_10x10_Elec/] [inputParticleType,/gate/source/beam_g/setParticleType e-] [inputPhaseSpaceFile,/work/lb8075/PhaseSpaces/Generated_PhS2_Electrons_10x10/generatedElectron_PhS2_v4_10x10] [grating_material,Aluminium] [foil_thick_um,{thick}] [foil_z_um,{cu_pos_um}] [pass_z_um,{pass_pos_um}] [epi_z_um,{epi_pos_um}] [bulk_z_um,{bulk_pos_um}]'\" ")

print("totalJobs: ",total_jobs)


for mat in material:
    for sims in sim_type:
        for field_sz in field_s:
            for thick in cu_thick_um:
                outputPath=f"/work/lb8075/PhaseSpaces/PS3/PhS3BigSensor_v6_{sims}_{field_sz}"

                with open(f"hadd_scripts/script_{mat}_{thick}_{sims}_{field_sz}_v6_redo.pbs", 'w') as g:

                    print("#!/bin/bash \n" 
                    "#PBS -l walltime=00:59:00\n" 
                    "#PBS -j oe\n"
                    "#PBS -l select=1:ncpus=1\n"
                    "#PBS -l select=1:ncpus=1:mem=500mb\n"
                    "#PBS -o /work/lb8075/job_logfiles\n",file=g)

                    print("module add apps/gate/8.2\n"
                    "now=$(date)\n"
                    "echo \"Start: $now\"\n",file=g)


                    print(f"hadd -f {outputPath}/Total-{mat}-{thick}-um-Edep.root {outputPath}/Epi-{thick}_um_{mat}*Edep.root",file=g)
                    print(f"hadd -f {outputPath}/Total-{mat}-{thick}-um-Edep-Squared.root {outputPath}/Epi-{thick}_um_{mat}*Edep-Squared.root",file=g)
                    print(f"hadd -f {outputPath}/Total-{mat}-{thick}-um-NbOfHits.root {outputPath}/Epi-{thick}_um_{mat}*NbOfHits.root",file=g)                    

                if ("FromPhS1" in sims):

                    with open(f"hadd_scripts/script_{mat}_{thick}_{sims}_{field_sz}_elecx2_v6_redo.pbs", 'w') as g:
                        print("#!/bin/bash \n" 
                        "#PBS -l walltime=00:59:00\n" 
                        "#PBS -j oe\n"
                        "#PBS -l select=1:ncpus=1\n"
                        "#PBS -l select=1:ncpus=1:mem=500mb\n"
                        "#PBS -o /work/lb8075/job_logfiles\n",file=g)

                        print("module add apps/gate/8.2\n"
                        "now=$(date)\n"
                        "echo \"Start: $now\"\n",file=g)
                        
                        if "highEn" in sims:
                            outputPath2=f"/work/lb8075/PhaseSpaces/PS3/PhS3BigSensor_v6_Electrons_highEn_{field_sz}"
                            outputPath3=f"/work/lb8075/PhaseSpaces/PS3/PhS3BigSensor_v6_ElecPhS1PhS2_highEn_{field_sz}"
                        else:
                            outputPath2=f"/work/lb8075/PhaseSpaces/PS3/PhS3BigSensor_v6_Electrons_{field_sz}"
                            outputPath3=f"/work/lb8075/PhaseSpaces/PS3/PhS3BigSensor_v6_ElecPhS1PhS2_{field_sz}"
                        print(f"hadd -f {outputPath3}/Total-{mat}-{thick}-um-Edep.root {outputPath}/Epi-{thick}_um_{mat}*Edep.root {outputPath2}/Epi-{thick}_um_{mat}*Edep.root",file=g)
                        print(f"hadd -f {outputPath3}/Total-{mat}-{thick}-um-Edep-Squared.root {outputPath}/Epi-{thick}_um_{mat}*Edep-Squared.root  {outputPath2}/Epi-{thick}_um_{mat}*Edep-Squared.root",file=g)
                        print(f"hadd -f {outputPath3}/Total-{mat}-{thick}-um-NbOfHits.root {outputPath}/Epi-{thick}_um_{mat}*NbOfHits.root  {outputPath2}/Epi-{thick}_um_{mat}*NbOfHits.root",file=g)

