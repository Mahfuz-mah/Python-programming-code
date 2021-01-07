#Magic methods related
class Bike:
    def __init__(self,name,color):               #magic method init
        self.name=name
        self.color=color

    def __eq__(self, other):                     #magic method equal
          return  self.name==other.name and self.color==other.color

    def __str__(self):                           #magic method string
        return (f"name:{self.name},color:{self.color}")

    def display(self):
        print(f"name:{self.name},color:{self.color}")
bike1=Bike("yahama R15","blue")
bike2=Bike("yahama R15","blue")
print(bike1==bike2)