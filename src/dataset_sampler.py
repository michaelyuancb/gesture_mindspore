import os,sys
import random
import shutil

typ=['train','val','test']
cl=['01_palm','02_l','03_fist','04_fist_moved','05_thumb','06_index','07_ok','08_palm_moved','09_c','10_down']
file_base='handgesture_datasets_mini'
if not os.path.exists(file_base):
    os.makedirs('handgesture_datasets')
for t in typ:
    filename_1=file_base+'\\'+t
    if not os.path.exists(filename_1):
        os.makedirs(filename_1)
    for j in cl:
        filename=filename_1+'\\'+j
        if not os.path.exists(filename):
            os.makedirs(filename)
ID_train=0
ID_dev=0;
ID_test=0
file_base_org='leapGestRecog'
for person_id in range(10):
    filename_1=file_base_org+'\\0'+str(person_id)
    for g in cl:
        filename_2=filename_1+'\\'+g 
        list_file=os.listdir(filename_2)
        n=len(list_file)
        n_train=int(n*0.07)
        n_dev=int(n*0.015)
        n_test=n_dev
        list_train=random.sample(list_file,n_train)
        for itm in list_train:
            list_file.remove(itm)
        list_dev=random.sample(list_file,n_dev)
        for itm in list_dev:
            list_file.remove(itm)
            list_test=list_file
        for x in list_train:
            file_dir='handgesture_datasets\\train\\'+g+'\\'+str(ID_train)+'.png'
            ID_train=ID_train+1
            shutil.copy(filename_2+'\\'+x,file_dir)
        for x in list_dev:
            file_dir='handgesture_datasets\\dev\\'+g+'\\'+str(ID_dev)+'.png'
            ID_dev=ID_dev+1
            shutil.copy(filename_2+'\\'+x,file_dir)
        for x in list_test:
            file_dir='handgesture_datasets\\test\\'+g+'\\'+str(ID_test)+'.png'
            ID_test=ID_test+1
            shutil.copy(filename_2+'\\'+x,file_dir)