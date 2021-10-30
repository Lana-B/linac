import numpy as np

cu_thick_um=(1,4,8,12,16,20,40,50,75,100,300,350,400)
# cu_thick_um=(1,2)
start_pos_mm=470
start_pos_um=470*1000
pass_thick_um=10
epi_thick_um=10
bulk_thick_um=700
airbox_thick_um=1000

for thick in cu_thick_um:
    cu_pos_um=start_pos_um-(thick/2.0)
    pass_pos_um=start_pos_um-(pass_thick_um/2.0)-thick
    epi_pos_um=start_pos_um-(epi_thick_um/2.0)-pass_thick_um-thick
    # print(start_pos_um,bulk_thick_um)
    bulk_pos_um=start_pos_um-(bulk_thick_um/2.0)-epi_thick_um-pass_thick_um-thick
    # print(start_pos_um,bulk_thick_um,bulk_pos_um)
    


    # print(f"myCommand=\"Gate $myScript -a '[seed,$RANDOM$RANDOM$RANDOM] [primaries,$prim] [pathGateMaterials,/home/lb8075/linac/data/GateMaterials.db] [id,$PBS_ARRAY_INDEX] [pathOutputDose,/work/lb8075/PhaseSpaces/PhS3BigSensor_v2_40x40_Elec/] [inputParticleType,/gate/source/beam_g/setParticleType e-] [inputPhaseSpaceFile,/work/lb8075/PhaseSpaces/Generated_PhS2_Electrons_40x40/generatedElectron_PhS2_v4_40x40] [grating_material,Aluminium] [foil_thick_um,{thick}] [foil_z_um,{cu_pos_um}] [pass_z_um,{pass_pos_um}] [epi_z_um,{epi_pos_um}] [bulk_z_um,{bulk_pos_um}]'\" ")

    print(f"myCommand=\"Gate $myScript -a '[seed,$RANDOM$RANDOM$RANDOM] [primaries,$prim] [pathGateMaterials,/home/lb8075/linac/data/GateMaterials.db] [id,$PBS_ARRAY_INDEX] [pathOutputDose,/work/lb8075/PhaseSpaces/PhS3BigSensor_v2_10x10_Elec/] [inputParticleType,/gate/source/beam_g/setParticleType e-] [inputPhaseSpaceFile,/work/lb8075/PhaseSpaces/Generated_PhS2_Electrons_10x10/generatedElectron_PhS2_v4_10x10] [grating_material,Silicon] [foil_thick_um,{thick}] [foil_z_um,{cu_pos_um}] [pass_z_um,{pass_pos_um}] [epi_z_um,{epi_pos_um}] [bulk_z_um,{bulk_pos_um}]'\" ")

    print("eval $myCommand")
    print("echo \"The time is $(date)\" ")
    print("")



# thick=0
# cu_pos_um=start_pos_um-(thick/2.0)
# pass_pos_um=start_pos_um-(pass_thick_um/2.0)-thick
# epi_pos_um=start_pos_um-(epi_thick_um/2.0)-pass_thick_um-thick
# # print(start_pos_um,bulk_thick_um)
# bulk_pos_um=start_pos_um-(bulk_thick_um/2.0)-epi_thick_um-pass_thick_um-thick
# # print(start_pos_um,bulk_thick_um,bulk_pos_um)



# print(f"myCommand=\"Gate $myScript -a '[seed,$RANDOM$RANDOM$RANDOM] [primaries,$prim] [pathGateMaterials,/home/lb8075/linac/data/GateMaterials.db] [id,$PBS_ARRAY_INDEX] [pathOutputDose,/work/lb8075/PhaseSpaces/PhS3BigSensor_v2_40x40_Elec/] [inputParticleType,/gate/source/beam_g/setParticleType e-] [inputPhaseSpaceFile,/work/lb8075/PhaseSpaces/Generated_PhS2_Electrons_40x40/generatedElectron_PhS2_v4_40x40] [pass_z_um,{pass_pos_um}] [epi_z_um,{epi_pos_um}] [bulk_z_um,{bulk_pos_um}]'\" ")

# print("eval $myCommand")
# print("echo \"The time is $(date)\" ")
# print("")
