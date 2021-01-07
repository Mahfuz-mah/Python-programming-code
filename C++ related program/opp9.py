#Abstraction related
from abc import  ABC,abstractmethod
class shape(ABC):
    def __init__(self,dim1,dim2):
        self.dim1=dim1                   #abstact class ta banie nite hbe
        self.dim2=dim2
    @abstractmethod

    def area(self):   #ai khane je kono cls ae jodi shape cls use korte cai tahole abstact method ta  use kortre hbe must
        pass
class triangle(shape):
    def area(self):
        area=.5*self.dim1*self.dim2
        print("area of triangle:",area)

class rectangular(shape):
    def area(self):
        area=self.dim1*self.dim2
        print("area of rectangular:",area)
t1=triangle(10,20)
t1.area()
r1=rectangular(10,20)
r1.area()

