
import pandas as pd
# import numpy as np
# from py2neo import authenticate, Graph, Node, Relationship
from py2neo import Graph, Node, Relationship,Database


data = pd.read_excel("1.xlsx", sheet_name=[0, 1])


graph = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="1039"
)

graph.delete_all()


col = data[0].columns
for indexs in data[0].index:
    notes = data[0].loc[indexs].values
    labels = notes[1].replace(' ', '').replace('.', '')
    str1 = "CREATE ("+labels+":"+notes[0]+"{"+col[1]+":'"+notes[1]+"',"+col[2]+":'"+notes[2]+"',"+col[3]+":'"+notes[3]+"'})"
    print(str1)
    graph.run(str1)

col = data[1].columns
for indexs in data[1].index:
    notes = data[1].loc[indexs].values
    str1 = "MATCH (a:"+notes[0]+"),(b:"+notes[3]+")  WHERE a."+col[1]+" = '"+notes[1]+"' AND b."+col[1]+"= '"+notes[4]+"' CREATE (a)-["+col[2]+":"+notes[2]+"  {"+col[5]+":['"+notes[5]+"']}]->(b)"
    print(str1)

    graph.run(str1)


