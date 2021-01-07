#map function

"""
def square(x):
    return x * x
num=[1,2,3,4]

result=list(map(square,num))
print(result)
"""

#filter function

num=[1,2,3,4,5,6]
result=list(filter(lambda x:x%2==0,num)) # lamda=function,x=parameter
print(result)