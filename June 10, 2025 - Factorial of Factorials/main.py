# In case of 4! * 3! * 2! * 1!
# 4 is multiplied once, 3 is multiplied twice, and so on, until 1 is multiplied 4 times

def fact_of_fact(n):
    result = 1
    for i in range(n, 1, -1): # We can stop at 1 since multiplying by 1 n times isn't going to change the result
        result *= i ** (n-i+1)
    return result

print(fact_of_fact(4)) # Expected output: 288
# 4! * 3! * 2! * 1! = 24 * 6 * 2 * 1 = 288
print(fact_of_fact(5)) # Expected output: 34560
print(fact_of_fact(6)) # Expected output: 24883200