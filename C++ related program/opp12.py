#search function
import re
pattern=r"colour"
text=("my favourite colour is blue ")
match=re.search(pattern,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())