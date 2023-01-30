def SumOf_N(n):
    if (n>=1):
        sum= 0
        num= 1
        while (num<= n):
            sum+=num
            num+=1
        return sum
    else:
        print("n must be >=1")
n=int(input("Enter n : "))
a= SumOf_N(n)
print(f' sum of first {n} natural numbers: {a}')