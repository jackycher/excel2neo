from py2neo import Node, Relationship, Graph, NodeMatcher
import pandas as pd
import ast


# 创建图数据库连接
graph = Graph("bolt://localhost:7687", username="neo4j", password="1039")


# 读取需整理类节点
# rootyx = graph.nodes.match(name="自然灾害").first()
notes = graph.nodes.match("医学")
# matcher = NodeMatcher(graph)
# note1 = matcher.match("自然灾害")
for note in notes:
    dic1 = dict(note)
    for key in dic1.keys():

        print('1', key, dic1[key])
        if (key.replace(' ', '')!=key):
            # 个别数据中存在简介key 会使key重复不能更新
            if(key.replace(' ', '')=='简介'):
                dic1['简介1'] = dic1.pop(key)
            else:
                dic1[key.replace(' ', '')] = dic1.pop(key)
    for key in dic1.keys():

        print('2', key)


# 按行遍历data1中数据
# for indexs in data1.index:
#     print("正在处理第", indexs+1, "行....")
#
#     # 丢弃data1一行中NaN（避免使用split函数中的类型错误
#     notes = data1.loc[indexs].dropna()
#
#     # 处理一行一列中数据的:问题
#     # 首先将数据按:符号分割成数组
#     # 然后将第一个:符号前的数据添加":"，再合并以后的数组数据并补充原:符号
#     # 目的是保证将第一个:替换成":"，其他不变
#     notestmp = notes.map(lambda x: x.split(":"))
#     notes = notestmp.map((lambda x: x[0] + '\":\"')) + notestmp.map(lambda x: ':'.join(x[1:]))
#
#     # 定义一个空字典，以保证后面使用.update方法合并字典数据
#     prodic = {}
#
#     # 遍历一行中(已删除NaN)的每个格数据
#     for values1 in notes.index:
#
#         # 将数据类型转换为dic
#         notes1 = ast.literal_eval(notes.loc[values1])
#         # 将每个中数据dic合并
#         prodic.update(**notes1)
#
#     # 开始写入图数据库
#     tx = graph.begin()
#     # 定义节点，并将原每行的数据合并成的字典作为属性参数传入
#     # ent = Node("实体", "医学", img=im, **prodic)
#     ent = Node("实体", "自然灾害", **prodic)
#     # 定义类到实体、实体到类的关系
#     re1 = Relationship(rootyx, "实体", ent)
#     re2 = Relationship(ent, "类", rootyx)
#     # 建立节点和关系并提交数据库
#     print(prodic.keys())
#     tx.create(ent)
#     tx.create(re1)
#     tx.create(re2)
#     tx.commit()



