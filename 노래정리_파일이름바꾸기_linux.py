
import os

ddir = "\\192.168.0.2\\yeon\\HardDisk\\�뷡\\����Ŭ�轼"

old_name = "_"
new_name = ' '

os.chdir(ddir)
list_screen = os.listdir(ddir)
print(list_screen)

for file in list_screen:

   
    new_file=file.replace(old_name,new_name)
    print(new_file)

    os.renames(file,new_file)
    

#print(list_screen)
