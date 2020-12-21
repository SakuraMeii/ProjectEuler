def calValue(name):
    sum = 0
    for char in name:
        sum += ord(char) - ord('A') + 1
    return(sum)

def main():
    with open('p022_names.txt','r') as nameFile:
        for line in nameFile:
            nameList = line.split(',')
            nameList = [name[1:-1] for name in nameList]
            nameList.sort()
        sum = 0
        for i in range(len(nameList)):
            sum += (i + 1) * calValue(nameList[i])
        print(sum)
if __name__ == '__main__':
    main()
