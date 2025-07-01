import math

def digits(num):
    if num < 1:
        raise ValueError("Input must be >= 1")
    num_digits = 0
    num_len = math.floor(math.log10(num)) + 1
    for d in range(1, num_len+1):
        if d != num_len:
            num_digits += d * (10**d - 10**(d-1))
        else:
            num_digits += d * (num - 10**(d-1))
    return num_digits

print(digits(1)) # output = 0
print(digits(10)) # output = 9
print(digits(100)) # output = 189
print(digits(2020)) # output = 6969