import sys
import subprocess
import os

test_executable = sys.argv[1]


path = "./fuzz_out/queue" #文件夹目录
file = open("./fuzz_out/correct","r")
file1 = open("./fuzz_out/final","a+")
records = file.read().splitlines()
records = records[20:50]
for record in records:
    subprocess.run([test_executable, "-SD",path+"/"+record], check=True,stdout=file1,stderr=file1)
file1.close()
file.close()

