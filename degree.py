import networkx as nx
import pandas as pd
import numpy as np


def takeSecond(elem):
    return elem[1]


dataname= 'NELL-995.test'
if 'NELL' in dataname:
    f1 = open("./data/"+dataname+"/train.dev.triples", 'r', encoding='utf-8')
else:
    f1 = open("./data/" + dataname + "/train.triples", 'r', encoding='utf-8')

f2 = open("./data/"+dataname+"/test.triples", 'r', encoding='utf-8')
f3= open("./data/"+dataname+"/dev.triples", 'r', encoding='utf-8')
global G
global sum
global num





if __name__ == '__main__':
    G={}
    num=0
    sum=0
    def add_edge1(e1, r, e2):
        global num, sum
        if e1 not in G:
            G[e1] = []
            num += 1
            G[e1].append((e2, r))
            sum += 1
        else:
            if r not in G[e1]:
                G[e1].append((e2, r))
                sum += 1
    fact=0
    entity = set()
    relation = set()
    for line in f1.readlines():
        fact+= 1
        line = line.split()
        if(len(line)==3):
            relation.add(line[2])
            add_edge1(line[0], line[1],line[2])
    # for line in f2.readlines():
    #     fact+= 1
    #     line = line.split()
    #     if(len(line)==3):
    #         relation.add(line[2])
    #     add_edge1(line[0], line[1],line[2])
    # for line in f3.readlines():
    #     fact+= 1
    #     line = line.split()
    #     if(len(line)==3):
    #         relation.add(line[2])
    #     add_edge1(line[0], line[1],line[2])

    f1.close()
    f2.close()
    f3.close()
    print("ent:"+str(num))
    print("rel:"+str(len(relation)))
    print("fact:"+str(fact))
    #计算G每个元素长度的中位数
    print(sum / num)
    print(np.median([len(G[i]) for i in G]))

    # print("avg degree: ", np.mean(list(dict(G.degree()).values())))
    # print("median degree: ", np.median(list(dict(G.degree()).values())))
    #


