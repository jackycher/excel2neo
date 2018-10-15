from py2neo import Node, Relationship, Graph


graph = Graph("bolt://localhost:7687", username="neo4j", password="1039")

# 删除数据库原数据
graph.delete_all()

node_info = {'id': '2344', 'name': 'xyz'}
tx = graph.begin()
root = Node("class", **node_info)
tx.create(root)
tx.commit()
# {**dic1,**dic2} 字典dic1与dic2合并
