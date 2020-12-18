import math
    
def main():
    with open('data.txt','r') as file:
        data = []
        row = 0
        for line in file.readlines():
            tmp = line.split()
            for col in range(len(tmp)):
                tmp[col] = int(tmp[col])
            data.append(tmp)
            row += 1
        for x in range(row - 2, -1, -1):
            for y in range(len(data[x])):
                if data[x+1][y] > data[x+1][y+1]:
                    data[x][y] += data[x+1][y]
                else:
                    data[x][y] += data[x+1][y+1]
        print(data[0][0])
                
if __name__ == '__main__':
    main()
