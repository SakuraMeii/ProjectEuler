primeList = [2]
maxNum = 2000000
for n in range(3,maxNum,2):
    for i in range(len(primeList)):
        if n < pow(primeList[i],2):
            primeList.append(n)
            break;
        if n % primeList[i] == 0:
            break

sumValue = 0
for i in range(len(primeList)):
    sumValue+=primeList[i]
print(sumValue)
            
