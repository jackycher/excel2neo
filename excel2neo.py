
import pandas as pd
# import numpy as np
# from py2neo import authenticate, Graph, Node, Relationship
from py2neo import Graph, Node, Relationship,Database

# load the excel data into a pandas dataframe
#data = pd.read_excel("1.xlsx")
data = pd.read_excel("1.xlsx",sheet_name=[0,1])
# name the business quarter that the survey data was collected
# quarter_year = 'Q42017'

# set up authentication parameters for the local neo4j server
# authenticate('localhost:7687', 'user', 'pass')
# connect to the local instance of neo4j with created password
graph = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="1039"
)

graph.delete_all()
# slice the dataframe for the indexes and rows of choice
# questions = [val for val in data.columns[1:5]]
# answers = data.iloc[1:4, 1:5]
# respondents = data.iloc[1:4, 0]

# print(data[0].columns)
col=data[0].columns
for indexs in data[0].index:
    notes = data[0].loc[indexs].values
    labels=notes[1].replace(' ','').replace('.','')
    str="CREATE ("+labels+":"+notes[0]+"{"+col[1]+":'"+notes[1]+"',"+col[2]+":'"+notes[2]+"',"+col[3]+":'"+notes[3]+"'})"
    str=str
    print(str)
    graph.run(str)
#    graph.run("CREATE (n:BBB{name:'ssss'}) return n")

col=data[1].columns
for indexs in data[1].index:
    notes = data[1].loc[indexs].values
#    str="CREATE (n:"+notes[0]+"{"+col[3]+":'"+notes[3]+"',"+col[2]+":'"+notes[2]+"',"+col[1]+":'"+notes[1]+"'}) return n"
    str = "MATCH (a:"+notes[0]+"),(b:"+notes[3]+")  WHERE a."+col[1]+" = '"+notes[1]+"' AND b."+col[1]+"= '"+notes[4]+"'  CREATE (a)-["+col[2]+":"+notes[2]+"  {"+col[5]+":['"+notes[5]+"']}]->(b)"
    print(str)

    graph.run(str)

        # print(data.columns[cols]+"="+notes[cols])
# print(data[1])



# define ranges for the number of questions and answers
# ques_num = range(len(questions))
# ans_num = range(len(answers))

# define a function to enter respondent and answer data for one question
# def populateDB(x):
#     q = Node('Question', question=questions[x]) # enters the question title at index 'x' as a node
#
#    for y in ans_num:
#        a = Node('Answer', response=answers.iloc[y, x], quarter=quarter_year)
#        r = Node('Respondent', ID=respondents.iloc[y])
#        qa = Relationship(q, 'Contains', a)
#        ar = Relationship(a, 'From', r)
#        graph.create(qa)
#        graph.create(ar)

# for i in ques_num:
#     populateDB(i)

# add nodes and relationships individually
# r = Node('Respondent', ID=respondents.iloc[0])
# a = Node('Answer', response=answers.iloc[0, 1], quarter=quarters[4])
# q = Node('Question', question=questions[0])
# qa = Relationship(q, 'Contains', a)
# ar = Relationship(a, 'From', r)
# # ra = Relationship(r, 'Answered', a)
# # aq = Relationship(a, 'InResponseTo', q)
# graph.create(qa)
# graph.create(ar)


# import question nodes
# for index in questions:
#     graph.create(Node('Question', question=index))
#
# for row in respondents:
#     graph.create(Node('Respondent', ID=row))