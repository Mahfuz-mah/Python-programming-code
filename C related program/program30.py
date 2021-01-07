#Stack related
#push: stack ae data add kora;1st in last out
#pop: stack ae data  remove kora;last in 1st out
books=[]
books.append("learn in C") #push kora hoice
books.append("learn in C++")
books.append("learn in java")
books.append("learn in python")
print(books)

books.pop() #1st in last out python
print(books)
print("now the top book is:",books[-1])
books.pop()

print("now the last books is:",books[-1])
books.pop()

print("now the last books is:",books[-1])
books.pop()
if not books:
    print("no books list") #empty book check





