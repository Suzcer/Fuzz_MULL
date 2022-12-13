import sys
import subprocess
import os

test_executable = sys.argv[1]


path = "./fuzz_out/queue" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名
s = []
for file in files:
    if not file.endswith(".elf"):
        os.rename(path+"/"+file,path+"/"+file+".elf")
record = open("./fuzz_out/correct","w+")
recordE = open("./fuzz_out/error","w+")
i = 0
for file in files: #遍历文件夹
    if not os.path.isdir(file) and file!=".state": #判断是否是文件夹，不是文件夹才打开
        file1 = open("./fuzz_out/correct_result/"+str(i),"w+")
        try:
            subprocess.run([test_executable, "-SD",path+"/"+file], check=True,stdout=file1)
            record.write(file+'\n')
        except:
            recordE.write(file+'\n')
        file1.close()
        size = os.path.getsize("./fuzz_out/correct_result/"+str(i))
        if size==0:
            os.remove("./fuzz_out/correct_result/"+str(i))
            i-=1
        i = i+1
record.close()

