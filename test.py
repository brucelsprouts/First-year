def isMultiple(n):
    if  n%7==0:
        return n
    elif n%3==0:
        return -1
    elif n%2==1: 
        return True
    else:
        return False

print(isMultiple(41))
