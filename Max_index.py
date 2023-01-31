# Getting the index of max number in the List
def Maximum(x):
    max_index = 0
    current_index = 1
    while current_index < len(x):
        # if x[current_index] < x[max_index]:  ''' for getting the least value index in the list'''
        if x[current_index] > x[max_index]:
            max_index = current_index
        current_index =  current_index+1
    # return x[max_index]    " for getting the maximum value in the list
    return max_index
a = [2,3,4,1,-8,77,88,9,10]
print(Maximum(a))