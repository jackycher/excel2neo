from py2neo import Node, Relationship, Graph
import pandas as pd
import numpy as np
import re
import os

'''
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
'''


data = pd.read_excel("data.xls", header=None)


'''
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
