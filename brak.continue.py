terminate_program=False
while not terminate_program:
    number1=input("plz enter your number:")
    number1=int(number1)
    number2=input("plz enter your another number:")
    number2=int(number2)
    while True:
        operation=input("please enter add/sub or quit to exit:")
        if operation=="quit":
            terminate_program=True
            break
        if operation not in ["add","sub"]:
              print("unknown operation!:")
              continue
        if operation=="add":
                print("result is",number1+number2)
                break
        if operation=="sub":
                print("result is",number1-number2)
                break
