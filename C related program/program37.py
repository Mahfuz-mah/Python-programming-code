#file read related

"""
file=open("student.txt","r")
print(file.readable())
file.close()
"""
"""
file=open("student.txt","w")
print(file.writable())
file.close()
"""
"""
file=open("student.txt","r")
text=file.read()
print(text)
file.close()
"""

#file write

"""
file=open("student.txt","a") # a main append age ja file ae ashe tr ste new kicu add hbe
text=file.write("\n mahfuz someone miss you")
print(text)
file.close()

"""
file=open("../student.txt", "w") #  ager line remove hoie ai line only thakbe
text=file.write("\n mahfuz someone miss you")
print(text)
file.close()


