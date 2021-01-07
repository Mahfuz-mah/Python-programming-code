#List as input from user

nubofwords=0
nubofleters=0
nubofdigits=0
text=input("plz enter your text of numbers:")
for x in text:
 x=x.lower()
 if x >='a' and x<='z':
  nubofwords=nubofwords+1
 elif x >= '0' and x <= '9':
  nubofdigits = nubofdigits+1
 elif x ==' ':
  nubofleters = nubofleters+1
print("nub of letters is:",nubofleters)
print("nub of digits is:",nubofdigits)
print("nub of words is:",nubofwords)





