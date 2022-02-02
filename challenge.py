def plus(a,b):
    return(float(a) + float(b))

def minus(a,b):
    return(float(a) - float(b))

def times(a,b):
    return(float(a) * float(b))

def division(a,b):
    return(float(a) / float(b))

def negation(a):
    return(-float(a))

def power(a,b):
    return(float(a) ** float(b))

def remainder(a,b):
    return(float(a) % float(b))

print(plus(1,"3"))
print(minus("2",5))
print(times("3",6))
print(division("5","2"))
print(negation("6"))
print(power("4",4))
print(remainder("3","7"))