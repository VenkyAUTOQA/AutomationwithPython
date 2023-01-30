def average(*args):
    n=len(args)
    if n>=1:
        test_val_type = list(map(type,args))
        if test_val_type.count(int) + test_val_type.count(float) == n:
            return round(sum(args)/n, 2)
        return 'Value must be int or float'
    return 'Number of values must be > 0'
x =int(input("enter values : "))
print(average(x))