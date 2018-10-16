from py2neo import Node, Relationship, Graph
import pandas as pd
import ast
import numpy as np
import re
import os


graph = Graph("bolt://localhost:7687", username="neo4j", password="1039")

# 删除数据库原数据
graph.delete_all()

# 建立顶级类Thing
tx = graph.begin()
root = Node("Class", name="Thing")
tx.create(root)
tx.commit()

data = pd.read_excel("data333.xls", header=None)
data[0] = "{url:"+data[0]+"}"
data[1] = "{name:"+data[1]+"}"
data[2] = "{简介:"+data[2]+"}"

repdic = {'\"': '\'', '\n': '', '^{': '{\"', '}$': '\"}'}
data1 = data.replace(repdic, regex=True)


# print(data1.index)
# print(data1.shape)
# print(data1.iloc)
# print(data1.loc)


for indexs in data1.index:
    #     print(indexs)
    #    print(type(data1.loc[indexs]))

    notes = data1.loc[indexs].dropna()
    #  print("dropna")
    notestmp = notes.map(lambda x: x.split(":"))
    notes = notestmp.map((lambda x: x[0] + '\":\"')) + notestmp.map(lambda x: ':'.join(x[1:]))
    notes = notes.str.replace('\n', '')
    prodic = {}
    print(type(prodic))
    for values1 in notes.index:

        print(values1)
        print(type(notes.loc[values1]))
        print(notes.loc[values1])

        notes1 = ast.literal_eval(notes.loc[values1])
        print(type(notes1))
        prodic.update(**notes1)
        print(type(ast.literal_eval(notes.loc[values1])))

    tx = graph.begin()
    ent = Node("Entity", **prodic)
    re1 = Relationship(root, "实体", ent)
    re2 = Relationship(ent, "类", root)
    tx.create(ent)
    tx.create(re1)
    tx.create(re2)
    tx.commit()
    






