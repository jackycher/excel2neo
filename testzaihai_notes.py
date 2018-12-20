from py2neo import Node, Relationship, Graph
import pandas as pd
import ast
import pickle
from PIL import Image

# 读取img并序列化
# im = pickle.dumps(Image.open('1.jpg'))

# 创建图数据库连接
graph = Graph("bolt://localhost:7687", username="neo4j", password="1039")

# 删除数据库原数据
# graph.delete_all()

# 建立顶级类Thing
# tx = graph.begin()
# root = Node("Class", name="Thing")
# tx.create(root)
# tx.commit()

# 读取自然灾害类节点
rootyx = graph.nodes.match(name="自然灾害").first()
# 建立类natural
# tx = graph.begin()
# rootmedical = Node("Thing", name="natural")
# remedical = Relationship(root, "包含", rootmedical)
# remedical2 = Relationship(rootmedical, "属于", root)
# tx.create(rootmedical)
# tx.create(remedical)
# tx.create(remedical2)
# tx.commit()

# 建立类自然灾害
# tx = graph.begin()
# rootyx = Node("natural", name="自然灾害")
# remedical = Relationship(rootmedical, "包含", rootyx)
# remedical2 = Relationship(rootyx, "属于", rootmedical)
# tx.create(rootyx)
# tx.create(remedical)
# tx.create(remedical2)
#
# tx.commit()

# 读入data数据表（不要表头）
data = pd.read_excel("data_ziranzaihai.xls", header=None)

# 补充第1-3列key值及相应符号
data[0] = "{url:"+data[0]+"}"
data[1] = "{name:"+data[1]+"}"
data[2] = "{简介:"+data[2]+"}"

# 使用正则表达式处理"(替换成',已保证以后添加的"唯一成对)、换行符(去除)、以及在开头和结尾的{}符号(添加")
repdic = {'\"': '\'', '\n': '', '^{': '{\"', '}$': '\"}', '\s+': ''}
data1 = data.replace(repdic, regex=True)

# print(data1.index)
# print(data1.shape)
# print(data1.iloc)
# print(data1.loc)

# 按行遍历data1中数据
for indexs in data1.index:
    print("正在处理第", indexs+1, "行....")

    # 丢弃data1一行中NaN（避免使用split函数中的类型错误
    notes = data1.loc[indexs].dropna()

    # 处理一行一列中数据的:问题
    # 首先将数据按:符号分割成数组
    # 然后将第一个:符号前的数据添加":"，再合并以后的数组数据并补充原:符号
    # 目的是保证将第一个:替换成":"，其他不变
    notestmp = notes.map(lambda x: x.split(":"))
    notes = notestmp.map((lambda x: x[0] + '\":\"')) + notestmp.map(lambda x: ':'.join(x[1:]))

    # 定义一个空字典，以保证后面使用.update方法合并字典数据
    prodic = {}

    # 遍历一行中(已删除NaN)的每个格数据
    for values1 in notes.index:

        # 将数据类型转换为dic
        notes1 = ast.literal_eval(notes.loc[values1])
        # 将每个中数据dic合并
        prodic.update(**notes1)

    # 开始写入图数据库
    tx = graph.begin()
    # 定义节点，并将原每行的数据合并成的字典作为属性参数传入
    # ent = Node("实体", "医学", img=im, **prodic)
    ent = Node("实体", "自然灾害", **prodic)
    # 定义类到实体、实体到类的关系
    re1 = Relationship(rootyx, "实体", ent)
    re2 = Relationship(ent, "类", rootyx)
    # 建立节点和关系并提交数据库
    print(prodic.keys())
    tx.create(ent)
    tx.create(re1)
    tx.create(re2)
    tx.commit()



