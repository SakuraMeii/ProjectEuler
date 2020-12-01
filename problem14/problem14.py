def Colltz(n,count=1):
    if n == 1:
        return(count)
    if n % 2 == 0:
        return Colltz(n/2,count+1)
    else:
        return Colltz(n*3+1,count+1)
def main():
    maxSeq = 0
    for i in range(1,1000000):
        tmp = Colltz(i)
        if tmp > maxSeq:
            maxSeq = tmp
            print(i,':',maxSeq)

if __name__ == '__main__':
    main()
