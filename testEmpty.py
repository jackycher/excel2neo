from py2neo import Graph,Node
graph = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="1039"
)
root= graph.nodes.match(name="Thing").first()
graph.create(a)