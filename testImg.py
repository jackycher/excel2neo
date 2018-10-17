from PIL import Image
import numpy as np
from py2neo import Node, Relationship, Graph
import pickle

# 创建图数据库连接
graph = Graph("bolt://localhost:7687", username="neo4j", password="1039")

# 删除数据库原数据
graph.delete_all()

# 读取img并序列化
im = pickle.dumps(Image.open('1.jpg'))
print(im)


# 建立顶级类Thing

tx = graph.begin()
root = Node("Class", name="Thing", img=im)
tx.create(root)
tx.commit()


im2 = pickle.loads(root["img"])

im2.show()
