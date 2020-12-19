#Amicable numbers
def d(n):
    sum = 0
    tmp = int(pow(n,0.5))
    for i in range(1, tmp + 1, 1):
        if n % i == 0:
            if i * i != n:
                sum += i + n // i
            else:
                sum += i
    sum -= n
    return(sum)

def main():
    sum = 0
    for i in range(1, 10001, 1):
        tmp = d(i)
        if i == d(tmp) and i != tmp:
            sum += i
    print(sum)
if __name__ == '__main__':
    main()
