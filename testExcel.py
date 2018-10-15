from py2neo import Node, Relationship, Graph
import pandas as pd
import ast
import numpy as np
import re
import os


graph = Graph("bolt://localhost:7687", username="neo4j", password="1039")

# 删除数据库原数据
graph.delete_all()


data = pd.read_excel("data333.xls", header=None)
repdic = {'\n': '', '{': '{\'', '}': '\'}', ':': '\':\'', 'http\':\'//': 'http://'}
data1 = data.replace(repdic, regex=True)


print(data1.index)
print(data1.shape)
print(data1.iloc)
print(data1.loc)
print(data1.isna())

for indexs in data1.index:
    print(indexs)
    print(type(data1.loc[indexs]))
    notes = data1.loc[indexs].dropna()
    prodic = {}
    print(type(prodic))
    for values1 in notes.index:


        print(values1)
        print(type(notes.loc[values1]))
        print(notes.loc[values1])

        if(values1>=3):
            notes1 = ast.literal_eval(notes.loc[values1])
            prodic.update(**notes1)
            print(type(ast.literal_eval(notes.loc[values1])))
    tx = graph.begin()
    root = Node("Entity", **prodic)
    tx.create(root)
    tx.commit()





