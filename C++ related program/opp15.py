#character class
import re
pattern=r"[A-Z][a-z][0-9]"
if re.match(pattern,"Ab5"):
    print("matched")