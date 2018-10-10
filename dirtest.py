import os

# 广度遍历文件
def BFSdir(rootDir):
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for d in dirs:
            print(os.path.join(root, d))
        for f in files:
            print(os.path.join(root, f))



# 深度遍历文件
def DFSdir(rootDir):
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        print(path)
        if os.path.isdir(path):
            DFSdir(path)

BFSdir('E:\\dir')
print('------------------------------')
DFSdir('E:\\dir')
