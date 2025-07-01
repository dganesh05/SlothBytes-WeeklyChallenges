# How Many Digits Between 1 and N (July 1, 2025)

This repository contains a Python solution to the **"How Many Digits Between 1 and N"** problem.

## Problem Description

Imagine concatenating all the numbers from 1 up to (but not including) `n` into one long string. Your task is to calculate **how many digits** appear in that concatenation.

### Objective

Write a function that returns the total count of digits used when writing out all numbers from 1 up to `n - 1`.

## Understand

Break down the problem into inputs, outputs, constraints, and edge cases:

- **Input**: An integer `n` ≥ 1  
- **Output**: An integer representing the total number of digits in numbers `1` through `n-1`  
- **Constraints**:  
  - Counting excludes 0 and `n` itself  
  - Large inputs possible (up to billions or more)  
- **Edge Cases**:  
  - `n = 1` → zero digits, as there are no numbers before 1  
  - Very large `n` → must be efficient  
  - Invalid inputs (`n < 1`) → should raise errors  

## Match

This problem is a form of **digit counting by ranges** and relates to:

- Understanding number ranges by digit length:  
  - 1-digit numbers: 1–9  
  - 2-digit numbers: 10–99  
  - 3-digit numbers: 100–999  
  - and so forth  
- Summing counts over these digit-length ranges  
- Handling the final partial range when `n` lies inside a digit group  

## Plan

1. Calculate the number of digits in `n` (call this `num_len`)  
2. For each digit length `d` from 1 up to `num_len - 1`:  
   - Add the total digits for all numbers with `d` digits:  
     `9 × 10^(d-1) × d`  
3. For the final digit length `num_len`:  
   - Add digits for numbers from `10^(num_len-1)` up to `n - 1`:  
     `(n - 10^(num_len - 1)) × num_len`  
4. Return the sum  

## Implement

```
def digits(num):
    if num < 1:
        raise ValueError("Input must be >= 1")
    num_digits = 0
    num_len = len(str(num))
    for d in range(1, num_len):
        num_digits += d * (9 * 10**(d - 1))
    num_digits += num_len * (num - 10**(num_len - 1))
    return num_digits
```

## Review

Test cases from the prompt:

```
print(digits(1))     # Output: 0
print(digits(10))    # Output: 9
print(digits(100))   # Output: 189
print(digits(2020))  # Output: 6969
```

## Evaluate

Time Complexity: O(log₁₀(n)) — iterates once per digit length

Space Complexity: O(1) — uses only fixed variables

Trade-offs: Efficient for very large inputs; relies on mathematical properties of digit counts

## Running the Code
Save the code in main.py

Run using Python 3:
```
python main.py
```

### To Run Test Cases

Save the code in main.py

Save the test cases in test_main.py

Run using Python 3:
```
pytest
```

## Output

```
0
9
189
6969
```

## License
This project is licensed under the MIT License.