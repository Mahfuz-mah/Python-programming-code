#constuctor related
class Student:
    roll=""
    gpa=""

    def __init__(self,roll,gpa):   #constructor method:-init- special method jeta ke xtra vabe call dite hoi na
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"roll:{self.roll},gpa:{self.gpa}")

rahim=Student(1659,3.50)
rahim.display()

mahfuz=Student(1660,3.70)
mahfuz.display()

chamak=Student(1663,3.40)
chamak.display()



