import math

def ceil(x):
    return math.ceil(x)
def floor(x):
    return math.floor(x)
def trunc(x):
    return math.trunc(x)

num = float(input("실수 :"))

print(num,":",ceil(num))
print(num,":",floor(num))
print(num,":",trunc(num))
