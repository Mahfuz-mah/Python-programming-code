# Queue related
#1st in 1st out
from _collections import  deque
banks=deque(["mahfuz","riya","alam","rafsan"])
print(banks)
banks.popleft()
print(banks)
banks.popleft()
banks.popleft()
banks.popleft()
if not banks:
    print("no person left")

