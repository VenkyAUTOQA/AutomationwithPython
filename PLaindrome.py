def is_Palindrome(n):
    n=n.lower()
    if n.isalnum():

        for i in range(0, int(len(n) / 2)):
            if n[i] != n[len(n) - i - 1]:
                return False
        return True
    else:
        print('invalid input!!')
n= input('Enter value to check palindrome: ')
a= is_Palindrome(n)
if a:
    print(f'{n} is palindrome')
else:
    print(f'{n} is not palindrome')


