from py2neo import Node, Relationship, Graph
import pandas as pd


graph = Graph("bolt://localhost:7687",
                username="neo4j",
                password="1039"
                )

graph.delete_all()


data = pd.read_excel("data.xls")

col = data.columns
for indexs in data.index:
    notes = data.loc[indexs].values
    print(notes[1])
    tx = graph.begin()
    a = Node(notes[1], name=notes[1])
    tx.create(a)
    tx.commit()



'''tx = graph.begin()
a = Node("Person", name="Alice")
tx.create(a)
b = Node("Person", name="Bob")
ab = Relationship(a, "KNOWS", b)
tx.create(ab)
tx.commit()'''
