#letter grand select
#relational operator or comparation operator


marks=int(input("plz enter your input:"))
if 80<=marks<=100:
    print("A+")
    if 70 <= marks <= 79:
        print("A")
elif 60<=marks<=69:
    print("A-")

elif 50<=marks<=59:
    print("B")
elif 40<=marks<=49:
    print("C")
elif 33<=marks<=39:
    print("D")
else:
    print("Fail")
    print("Next year better try it")


