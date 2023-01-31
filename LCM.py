def lcm(a,b):
    if a>b:
        greater = a
    elif b>a :
        greater = b
    while (True):
        if (greater%a == 0) and (greater%b == 0):
            lcm = greater
            break
        greater+= 1
    return lcm
print(lcm(15,16))