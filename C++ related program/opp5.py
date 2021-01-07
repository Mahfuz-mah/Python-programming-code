#inheritance related:akta cls ar bosisto onno cls ae nie asa hoi
class phone: #parent cls,super cls,base cls
    def call(self):
        print("you can call now")
    def message(self):
        print("you can send now")

class samsung(phone): #samsung cls ar modhe phone cls ar bosisto pokas pewche
    #child cls,sub cls,derived cls
    def photo(self):
        print("you can see now")
    def video(self):
        print("you can watch now")
s=samsung()
s.photo()
s.video()
s.message()
s.call()
print(issubclass(samsung,phone))

