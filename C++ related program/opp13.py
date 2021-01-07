#sub(pattern,replace,string) function
import re
pattern=r"colour"
text1=("my fav colour is red and another fav colour is blue")
text2=re.sub(pattern,"color",text1,count=2)
print(text2)