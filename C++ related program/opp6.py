#inheritance example
class shape:
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2
    def area(self):
        print("i am area method of shape class")
class triangle(shape):
    def area(self):
        area=.5*self.dim1*self.dim2
        print("area of triangle:",area)

class rectangle(shape):
    def area(self):
        area=self.dim1*self.dim2
        print("area of rectangle:",area)
t=triangle(10,20)
t.area()
r=rectangle(10,20)
r.area()
