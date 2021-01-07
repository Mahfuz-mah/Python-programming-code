#exercise
class Triangle:


    def __init__(self,base,height):
        self.base=base
        self.height=height

    def calculate_area(self):
        area=.5*self.base*self.height
        print("area is:",area)

t1=Triangle(10,20)
t1.calculate_area()
t2=Triangle(25,35)
t2.calculate_area() 