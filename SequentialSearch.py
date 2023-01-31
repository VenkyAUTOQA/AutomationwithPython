def Sequential_search(list_,n):
    found = False
    for i in list_:
        if i == n:
            found = True
            break
    return found
numbers = list(range(1,20))
print(Sequential_search(numbers,7))
