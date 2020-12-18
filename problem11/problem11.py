import math
dataList = []
with open('data','r') as dFile:
    for line in dFile.readlines():
        dataList.append(line.split())
col = len(dataList[0])
row = len(dataList)
maxProduct = -float('inf')
for x in range(col):
    for y in range(row):
        #(1,0)
        if 0<=x<=col-4:
            p = 1
            for i in range(4):
                p*=int(dataList[y][x+i])
            if p >= maxProduct:
                maxProduct = p
        #(0,-1)
        if 0<=y<=row-4:
            p = 1
            for i in range(4):
                p*=int(dataList[y+i][x])
            if p >= maxProduct:
                maxProduct = p
        #(1,-1)
        if 0<=x<=col-4 and 0<=y<=row-4:
            p = 1
            for i in range(4):
                p*=int(dataList[y+i][x+i])
            if p >= maxProduct:
                maxProduct = p
        #(1,1)
        if 0<=x<col-4 and 3<=y<row:
            p = 1
            for i in range(4):
                p*=int(dataList[y-i][x+i])
            if p >= maxProduct:
                maxProduct = p
print(maxProduct)
