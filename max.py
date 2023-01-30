def MaxNum(*args):
    n= list(args)
    maximum = n[0]
    print('Start max : ', maximum)
    for i in n:
        print("Checking :", i)
        if i> maximum:
            maximum= i
            print('New Max Value: ',i)
    return maximum
print(MaxNum(1,3,'a',7,8,9))