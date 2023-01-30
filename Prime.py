def is_prime(n):
   if n <= 1:
      print("Please enter greater than 0 values")
   else:
      for i in range(2, n):
         # checking for factor
         if n % i == 0:
            # return False
            return False
      # returning True
   return True
def check_prime():
    n=input("Enter Value to check : ")
    if n.isnumeric():
       n= int(n)
       a= is_prime(n)
       if a:
         print(f'{n} is prime')
       else:
            print(f'{n} is not prime')
    else:
       print("Invalid input")
check_prime()


PrimeList=[]
for i in range(1,1000):
    a = is_prime(i)
    if a:
        PrimeList.append(i)
for p in PrimeList:
    print(p)