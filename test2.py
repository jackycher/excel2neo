from py2neo import Node, Relationship, Graph

g = Graph("bolt://localhost:7687",
                username="neo4j",
                password="1039"
                )



tx = g.begin()
a = Node("Person", name="Alice")
tx.create(a)
b = Node("Person", name="Bob")
ab = Relationship(a, "KNOWS", b)
tx.create(ab)
tx.commit()