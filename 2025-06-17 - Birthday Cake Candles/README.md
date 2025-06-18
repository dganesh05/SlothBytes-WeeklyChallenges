# Birthday Cake Candles (June 17, 2025)

This repository contains a Python solution to the "Birthday Cake Candles" problem.

Link to post: https://slothbytes.beehiiv.com/p/geohashing

## Problem Description

You are in charge of the birthday cake for a child’s party. The cake will have one candle for each year of the child’s age. The child can only blow out the tallest candles.

### Objective

Create a function that returns the number of **tallest** candles.

## Understand

Break the problem into I/O, constraints, and edge cases:

- **Input**: A list of integers representing candle heights (e.g., `[4, 4, 1, 3]`)
- **Output**: An integer representing how many candles are the tallest
- **Constraints**:
  - 0 ≤ number of candles ≤ 100
  - Candle heights are non-negative integers
- **Edge Cases**:
  - Empty list (`[]`) → return `0`
  - All candles same height → return length of list
  - Single candle → return `1`

## Match

This is a variation of the **maximum tracking** problem. You're finding the **max value** and **counting occurrences** — both common list-processing patterns.

## Plan

Because we have to check every element of the list to find the maximum, the best time complexity we can achieve is O(n), which is a single pass. 
Use a single-pass linear approach with two variables:
1. `current_max` – to track the tallest candle height
2. `counter` – to count how many times this height occurs

**Pseudocode**:
if list is empty:
    return 0
initialize current_max as first candle
initialize counter as 0
for each candle in list:
    if candle > current_max:
        update current_max
        reset counter to 0
    if candle == current_max: # Which counts the newly switched to max
        increment counter
return counter

## Implement
```
def birthdayCakeCandles(candles):
    counter = 0
    if len(candles) > 0:
        current_max = candles[0]
        for candle in candles:
            if candle > current_max:
                current_max = candle
                counter = 0
            if current_max == candle:
                counter += 1
    return counter
```

## Review

Run test cases to ensure correctness:

```
print(birthdayCakeCandles([4, 4, 1, 3]))  # Output: 2
print(birthdayCakeCandles([1, 1, 1, 1]))  # Output: 4
print(birthdayCakeCandles([]))           # Output: 0
print(birthdayCakeCandles([5]))          # Output: 1
```

## Evaluate

- Time Complexity: O(n) – Each element is visited once
- Space Complexity: O(1) – Only two variables used
- Trade-offs: Optimal in both speed and memory usage; handles all edge cases without extra data structures

## Running the Code

1. Save the code in main.py.
2. Run it using Python 3:
```
python main.py
```

## Output
```
2
4
0
1
```

## License

This project is licensed under the MIT License.