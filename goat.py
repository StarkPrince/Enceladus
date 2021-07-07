import os

os.chdir("D:\paker")

j = 1
for i in os.listdir():
    os.rename(i,"house_"+str(j).zfill(2)+".png")
    j+=1