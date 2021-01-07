#Regular expressions related
#match pattern
import re
pattern=r"color"
if re.match(pattern,"color is my fav red,red color is my fav"):
 print("match")
else:
    print("not match")
#search pattern
import re
pattern=r"color"
if re.search(pattern,"color is my fav red,red color is my fav"):
 print("match")
else:
    print("not match")
#find all pattern

import re
pattern=r"color"
print(re.findall(pattern,"color is my fav red,red color is my fav"))
