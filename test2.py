from py2neo import Node, Relationship, Graph
import pandas as pd
import numpy as np
import re
from os import path

graph = Graph("bolt://localhost:7687",
                username="neo4j",
                password="1039"
                )
#删除数据库原数据
graph.delete_all()

#获取路径
dir1 = path.dirname(__file__).split('/')
Cname = (dir1[-1])

#建立路径名称类
tx = graph.begin()
c = Node("Class", name=Cname, label="Class")
tx.create(c)
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
    ca = Relationship(c, "实体", a)
    tx.create(ca)
    tx.commit()

    if notes[4] != np.nan:
        print(notes[4])
        key1, values1 = notes[4].split(':')
        print(key1, values1)



    '''tx = graph.begin()
    a = Node("Person", name="Alice")
    tx.create(a)
    b = Node("Person", name="Bob")
    ab = Relationship(a, "KNOWS", b)
    tx.create(ab)
    tx.commit()'''

