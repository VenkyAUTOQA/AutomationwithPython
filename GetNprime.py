def nPrime(n):
    count = 0
    num = 2
    li = []
    "if n>0:"

    while True:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            li.append(num)
        num += 1
        count += 1
        if (n == len(li)):
            break
    return li
    # '''else:
    #     print("enter positive number only !!!!")'''


def getNprime():
    # ''' getting the n prime numbers'''
    try:
        n = input("Enter number: ")
        if n.isnumeric():
            n = int(n)
            if (n > 0):
                a = nPrime(n)
                # return a
                print(f'total prime numbers : {len(a)}, \nList of prime numbers : \n{a}')
            else:
                print("Enter number greater then 0")

        else:
            print(" The Value must be integer !!!")
    except:
        print("Enter valid number")
getNprime()
