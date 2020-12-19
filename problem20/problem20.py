#Factorial digit sum
import math
def addBit(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    return(sum)

def main():
    value = addBit(math.factorial(100))    
    print(value)
if __name__ == '__main__':
    main()
