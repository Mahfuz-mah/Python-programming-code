"""
#xargs argument used

def add(*numbers):
    sum=0
    for num in numbers:
        sum=sum+num
    print("reuslt is:",sum)
add(20,30)
add(30,80)
add(50,100)
"""

#xxargs argument

def student(**details):
 print(details)
student(id=10001,name="mahfuz")
