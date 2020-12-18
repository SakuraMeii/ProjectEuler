import math

max = -math.inf

def function(data, row = 0, col = 0, sum = 0, maxN = 0):
    if row == maxN:
        global max
        if max < sum:
            max = sum
        return
    function(data, row + 1, col, sum + data[row][col], maxN)
    function(data, row + 1, col +1, sum + data[row][col], maxN)
    
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
        function(data = data, maxN = row)
        print(max)
                
if __name__ == '__main__':
    main()
