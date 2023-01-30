def Even(n):
    if n<1:
        print('enter positive number')
    else:
        if (n%2)== 0 :
            return True
    return False
def is_even():
    n= (input('Enter number : '))
    if n.isnumeric():
        n =int(n)
        a = Even(n)
        if a:
            print(f'{n} is Even')
        else:
            print(f'{n} is odd number')
    else:
        print("invalid input")
is_even()

for i in range(1000):
    s= Even(i)
    if s:
        print(i)