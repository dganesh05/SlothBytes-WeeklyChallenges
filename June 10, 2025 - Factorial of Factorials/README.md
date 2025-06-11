# Factorial of Factorials (June 10, 2025)

This repository contains a Python solution for the "Factorial of Factorials" challenge.
Link to post: https://slothbytes.beehiiv.com/p/federated-learning

## Problem Description

Create a function that takes an integer `n` and returns the **factorial of factorials**.
For example, for `n = 4`, the result is `4! * 3! * 2! * 1! = 288`.

## How the Code Works

The function `fact_of_fact(n)` calculates the factorial of factorials efficiently by recognizing that each integer `i` from `n` down to `1` appears in the product a specific number of times.

### Example

For `n = 4`:
- 4 appears once (in 4!)
- 3 appears twice (in 4! and 3!)
- 2 appears three times (in 4!, 3!, and 2!)
- 1 appears four times (in 4!, 3!, 2!, and 1!)

The code multiplies each `i` raised to the power of its number of appearances.

## Usage

```python
def fact_of_fact(n):
    result = 1
    for i in range(n, 1, -1):
        result *= i ** (n - i + 1)
    return result

print(fact_of_fact(4)) # Output: 288
print(fact_of_fact(5)) # Output: 34560
print(fact_of_fact(6)) # Output: 24883200
```

## Running the Code

1. Save the code in `main.py`.
2. Run it using Python 3:
   ```sh
   python main.py
   ```

## Output

```
288
34560
24883200
```

## License

This project is licensed under the MIT License.