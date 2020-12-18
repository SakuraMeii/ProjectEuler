maxNum = 1000
for i in range(1,maxNum//3):
    for j in range(1,(maxNum-i)//2):
        k = maxNum - i - j
        if i*i + j*j == k*k:
            print("%d*%d*%d=%d" % (i,j,k,i*j*k))


