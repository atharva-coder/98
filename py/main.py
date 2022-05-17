import os
import shutil
source=input("enter folder name to be sorted:  ")
list_of_file=os.listdir(source)
for file in list_of_file:
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    if ext=='':
        continue
    if os.path.exists(source+'/'+ext):
        shutil.move(source+'/'+file,source+'/'+ext+'/'+file)
    else:
        os.makedirs(source+'/'+ext)
        shutil.move(source+'/'+file,source+'/'+ext+'/'+file)
# dest=input("enter destination folder name: ")
# source=source+'/'
# dest = dest+'/'
# list_of_files=os.listdir(source)
# for file in list_of_files:
#     shutil.copy((source+file),dest)
