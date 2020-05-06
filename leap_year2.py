leap_year=input("please enter your year data:")
leap_year=int(leap_year)
if leap_year % 100 !=0 and leap_year % 4 ==0:
    print("YES")
elif leap_year % 100 ==0 or leap_year % 400 == 0:
    print("YES")
else:
    print("NO")
