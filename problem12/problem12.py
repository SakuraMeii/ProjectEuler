import mathstrategy.prime as msp

n = 1

while msp.factor(n if n%2 else n//2)*\
      msp.factor(n+1 if (n+1)%2 else (n+1)//2) < 500:
    print(n)
    n+=1
print(n*(n+1)/2)
