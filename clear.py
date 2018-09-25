from py2neo import Graph
import re

graph = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="1039"
)


graph.delete_all()
fileName = re.sub('[\/:*?"<>|·]','',title)#去掉非法字符
print re.sub