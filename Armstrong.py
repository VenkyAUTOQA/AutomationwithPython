def findArmStrongSum(no):
    currentNo = no
    length = len(str(currentNo))
    sum = 0
    while currentNo > 0:
        lastDigit = currentNo % 10
        sum += lastDigit ** length

        currentNo = int(currentNo/10)

    return sum
def GetPalindrome():
    no = input("Enter a positive number :")
    if no.isnumeric():
        no = int(no)
        if (no > 0):
           armStrongSum = findArmStrongSum(no)
           if (armStrongSum == no):
               print(f"Given number {no} is an Armstrong Number")
           else:
               print(f"{no} is not an Armstrong Number")
    else:

      print ("Please enter a valid number")
GetPalindrome()


''' Getting Palindrome numbers from the Given range'''

# ArmList=[]
# for i in range(1,1000):
#     armStrongSum = findArmStrongSum(i)
#     if (armStrongSum == i):
#         ArmList.append(i)
#
# for no in ArmList:
#     print(no)