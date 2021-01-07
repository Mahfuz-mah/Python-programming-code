#multilevel inheritance
class A:
    def display1(self):

       print("I am inside in class A")

class B(A):
    #display1 element cole ashe main cls A ashe
    def display2(self):
               print("I am inside in class B")


class C(B):
    #display1=class A and display2=class B ar element ashe main 2 ta cls akste aikahe attend ashe
    def display3(self):
        super().display1() #cls A call korchi super() ar dara
        super().display2() #cls B ke call kora hoice
        print("I am inside in class C")

ob1=C()
ob1.display3()
