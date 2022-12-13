import sys
import subprocess
import os

path1 = "./fuzz_out/correct_result/"
file2 = open("./fuzz_out/final", "rb")
corrects = []
for i in range(20, 50):
    with open(path1 + str(i), "rb") as file1:
        try:
            corrects.append(file1.read().split(str.encode('\n' + "./fuzz_out/queue/"))[1])
        except:
            corrects.append("")
check = file2.read()
checks = check.split(str.encode('\n' + "./fuzz_out/queue/"))
length = len(checks) - 1
count = 0
for i in checks:
    if i in corrects:
        count += 1

print(count)
print(length)
print(count / length)
file1.close()
file2.close()

