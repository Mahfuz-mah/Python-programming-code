#multiple inheritance
class A:
    def display(self):

       print("I am inside in class A")

class B:

    def display(self):
               print("I am inside in class B")


class C(A,B):# je class age thakbe sta parity besi pabe jemon cls A age ashe sta parity besi pabe
    pass
    # cls A  display1 method  cole asbe
    #cls B display2 method cole asbe

ob1=C()
ob1.display()