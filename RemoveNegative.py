def Remove_negative(n):
    return n >= 0
nums=[1,-2,-3,8,-6,-8,9,8,6]
filtered= list(filter(Remove_negative, nums))
print(filtered)

#  another method
x= [i for i in nums if i>= 0]
print(x)