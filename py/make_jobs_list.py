import os

def make_jobs_list(folder_path):
    temp_list=[]
    for i in range(1,201):
        file_path=f"{folder_path}/Epi-200_um_Copper-{i}-Edep.root"
        if (os.path.exists(file_path)):
            continue
        else:
            temp_list.append(str(i))
    final_list=",".join(temp_list)
    list_size=len(temp_list)
    return list_size,final_list

n,lst=make_jobs_list("/work/lb8075/PhaseSpaces/PS3/PhS3BigSensor_v6_Electrons_highEn_10x10")
print(n,lst)