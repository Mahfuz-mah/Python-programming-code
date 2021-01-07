#recursion function;   ai function nijey nijeke call korte parbe
#two think know that recursion call and base case always mone rakte hbe

def fact(n):
    if n==1:
        return 1 # base case main n==1 hole program ta stop korbe
    else:
        return n* fact(n-1)



print(fact(5))  #5! ar value ber korchi