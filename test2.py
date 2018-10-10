from py2neo import Node, Relationship, Graph
import pandas as pd
import numpy as np
import re
import os

graph = Graph("bolt://localhost:7687", username="neo4j", password="1039")

# 删除数据库原数据
graph.delete_all()

rootDir = "//data"

# 建立顶级类Thing
tx = graph.begin()
root = Node("Class", name="Thing")
tx.create(root)
tx.commit()

# 获取路径
dir1 = path.dirname(__file__).split('/')
Cname = (dir1[-1])

# 建立路径名称类
tx = graph.begin()
troot = Node("Class", name=Cname, label="Class")
tx.create(troot)
roott = Relationship(root, "子类", troot)
tx.create(roott)
tx.commit()

data = pd.read_excel("data.xls", header=None)

col = data.columns

dic1={}

for indexs in data.index:
    notes = data.loc[indexs].values
    print(notes[1])
    tx = graph.begin()
    nname = 'n'+re.sub('[\/:*?"<>|·（）-]', '', notes[1])
    a = Node(Cname, url=notes[0], name=notes[1], desc=notes[2])
    tx.create(a)
    ta = Relationship(troot, "实体", a)
    tx.create(ta)
    tx.commit()
'''
    if notes[4] != np.nan:
        print(notes[4])
        key1, values1 = notes[4].split(':')
        print(key1, values1)'''



'''tx = graph.begin()
a = Node("Person", name="Alice")
tx.create(a)
b = Node("Person", name="Bob")
ab = Relationship(a, "KNOWS", b)
tx.create(ab)
tx.commit()'''


def Test1(rootDir):
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for d in dirs:
            print
            os.path.join(root, d)
        for f in files:
            print
            os.path.join(root, f)




def Test2(rootDir):
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        print
        path
        if os.path.isdir(path):
            Test2(path)