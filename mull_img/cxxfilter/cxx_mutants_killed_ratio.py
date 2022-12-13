import sys
import subprocess
import os
from pylab import mpl
import matplotlib.pyplot as plt

def draw_from_dict(dicdata,RANGE):
    #dicdata：字典的数据。
    #RANGE：截取显示的字典的长度。
    #heng=0，代表条状图的柱子是竖直向上的。heng=1，代表柱子是横向的。考虑到文字是从左到右的，让柱子横向排列更容易观察坐标轴。
    by_value = sorted(dicdata.items(),key = lambda item:item[1],reverse=True)
    x = []
    y = []
    for d in by_value:
        x.append(d[0])
        y.append(d[1])

    plt.barh(x[0:RANGE], y[0:RANGE])
    plt.title("cxxfilter中变异算子被杀死的比例", fontsize=15, pad=20)

    # 设置显示中文字体
    mpl.rcParams["font.sans-serif"] = ["SimHei"]
    mpl.rcParams["axes.unicode_minus"] = False

    plt.subplots_adjust(left=0.4)
    plt.show()
    return


if __name__ == "__main__":

    with open('../../mull_result/cxxfilt_result', encoding='utf-8') as file_obj:
        contents = file_obj.read()
    # print(contents)
    contents=contents[contents.find("[info] Killed mutants"):contents.find("[info] Survived mutants")]
    contents=contents.replace("^","")
    contents=contents.split("\n")
    killed_mutant_dateDict = {}
    for i in range(len(contents)):
        if(contents[i].find("Cannot report")!=-1):
            temp=contents[i]
            key = contents[i][temp.find('\'')+1:temp.find('/')-1]
            originValue = killed_mutant_dateDict.get(key,0)
            killed_mutant_dateDict[key]=originValue+1

    with open('../../mull_result/cxxfilt_result', encoding='utf-8') as file_obj:
        contents = file_obj.read()

    contents = contents[contents.find("[info] Survived mutants"):contents.find("[info] Mutation score")]
    contents = contents.replace("^", "")
    contents = contents.split("\n")
    survived_mutant_dateDict = {}
    for i in range(len(contents)):
        if (contents[i].find("Cannot report")!=-1):
            temp = contents[i]
            key = contents[i][temp.find('\'')+1:temp.find('/')-1]
            originValue = survived_mutant_dateDict.get(key, 0)
            survived_mutant_dateDict[key] = originValue + 1

    ratioDict={}
    for i in (killed_mutant_dateDict).keys():
        if(survived_mutant_dateDict.get(i,0)==0):
            ratioDict[i]=1.0
        elif survived_mutant_dateDict.get(i,0)!=0:
            ratioDict[i]=killed_mutant_dateDict[i]/(survived_mutant_dateDict[i]+killed_mutant_dateDict[i])
            survived_mutant_dateDict.pop(i)

    for i in survived_mutant_dateDict.keys():
        ratioDict[i]=0

    draw_from_dict(ratioDict, len(ratioDict))



