#list related function

subjects=["C","C++","Java","Python","Android","swift","Javascipt","Larabel"]
print(len(subjects))

subjects.append("Toc")  # add kora list ae new element:append
print(subjects)

subjects.insert(3,"OS") #fixed index ae element add kora:insert
print(subjects)

subjects.remove("swift") # element remove kore fela
print(subjects)


# sazie laka hoi sort function ar dara
items=[500,540,200,100,180,1000,890,788,350]
items.sort()
print(items)

#reverse function
items.reverse()
print(items)

#pop funciton ,pop main last element ke vinish kore dibe
items.pop()
print(items)

#clear function
items.clear()
print(items)

#copy kora
item0=[1,2,3,5,89,80]

item2=item0.copy()

print(item2)

#index ar position

item4=[1,5,4,6,8,9]
pos=item4.index(4)
print(pos)

# count function ,kono element koto bar ashe sta ber kora jabe

item5=[1,2,3,4,8,9,7,4,6,4,5,4,8,6,4,]
papi=item5.count(4)
print(papi)