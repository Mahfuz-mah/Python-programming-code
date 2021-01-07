#method crated related

class Student:
    roll=""
    gpa=""
    sec=""


    def set_value(self,roll,gpa,sec):
        self.roll=roll
        self.gpa=gpa
        self.sec=sec

    def display(self):
        print(f"roll:{self.roll},gpa:{self.gpa},sec:{self.sec}")




rahim=Student()
rahim.set_value(101, 3.50," A")
rahim.display()
karim=Student()
karim.set_value(102, 3.60," B")
karim.display()


rafsan=Student()
rafsan.set_value(103, 3.70," C")
rafsan.display()
