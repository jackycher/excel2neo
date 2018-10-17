import os


# 广度遍历文件
def BFSdir(rootDir):
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for d in dirs:
            print(d)
        for f in files:
            print(f)


# 深度遍历文件
def DFSdir(rootDir):
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)

        if os.path.isdir(path):
            DFSdir(path)
        else:
            print(path)


BFSdir('C:\\Users\\Xujing\\PycharmProjects\\csvtoneo\\data')
print('------------------------------')
DFSdir('C:\\Users\\Xujing\\PycharmProjects\\csvtoneo\\data')
