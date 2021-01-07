#meta character

#dot(.) meta char
import re
pattern=r"colo..r"
if re.match(pattern,"colouar"):
    print("matched")


#(^) meta chac main starting ae colo thakte hbe
#($) meta char main last ae r thakte hbe
import re
pattern=r"^colo..r$"
if re.match(pattern,"colouar"):
    print("matched")

#(*) meta char main 0 or more
import re
pattern=r"o*"  #o  ta zero or ar besi thakte pare
if re.match(pattern,"colouar"):
    print("matched")

#(+)meta char 1 or more

import re
pattern=r"c+"  #ontoto akbr c thakte hbe na thakle kaj korbe na
if re.match(pattern,"colouar"):
    print("matched")

#(?) meta char
import re
pattern=r"ice(-)?cram"  # ? main hifen(-) zero or one bar thakbe
if re.match(pattern,"ice-cram"):
    print("matched")
#{} meta char
import re
pattern=r"a{1,3}$"
if re.match(pattern,"aaa"):
    print("matched")
