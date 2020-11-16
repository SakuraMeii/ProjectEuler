import math

def isPrime(n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
        return True

def nextPrime(n):
    count = 1
    while True:
        if isPrime(n+count):
            return n+count
        else:
            count+=1

def factor(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        factorCount = {}
        quotient = n
        prime = 2
        index = 0
        while quotient != 1:
            if quotient % prime == 0:
                if str(prime) in factorCount:
                    factorCount[str(prime)]+=1
                else:
                    factorCount[str(prime)] = 1
                quotient/=prime
            else:
                prime = nextPrime(prime)
        factorNumber = 1
        for each in factorCount:
            factorNumber*=(factorCount[each]+1)
        return factorNumber

if __name__ == '__main__':
    for i in range(100):
        if isPrime(i):
            print("%d:prime" % (i))
        else:
            print("%d:not prime" % (i))
    for i in range(1,100):
        print(i,":",factor(i))
    print(factor(100000000000001))
