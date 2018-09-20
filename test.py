from py2neo import Graph, Node, Relationship
graph = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="1039"
)
graph.run("CREATE (n:BBB{name:'ssss'}) return n")


