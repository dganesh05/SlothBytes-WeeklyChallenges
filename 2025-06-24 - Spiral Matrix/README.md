# Spiral Matrix Traversal (June 24, 2025)
This repository contains a Python solution to the "Spiral Matrix Traversal" problem.
Link to post: [https://slothbytes.beehiiv.com/p/save-systems](https://slothbytes.beehiiv.com/p/save-systems)

## Problem Description
Given an `m x n` matrix, return all elements of the matrix in **spiral order**, starting from the top-left corner and looping inward in a clockwise pattern.
### Objective
Create a function that returns a **list of numbers** in spiral order from the given matrix.

## Understand
Break the problem into I/O, constraints, and edge cases:
* **Input**: A list of lists representing the matrix (e.g., `[[1,2,3],[4,5,6],[7,8,9]]`)
* **Output**: A flat list of numbers in spiral order (e.g., `[1,2,3,6,9,8,7,4,5]`)
* **Constraints**:
  * Each inner list (row) is the same length
  * Matrix may be rectangular or square
* **Edge Cases**:
  * Empty matrix (`[]` or `[[]]`) → return `[]`
  * Single element matrix (`[[x]]`) → return `[x]`
  * Single row or column → return as-is

## Match
This is a form of **matrix traversal**, specifically a **layer-by-layer simulation** pattern. The problem matches techniques involving:
* Boundary tracking (`top`, `bottom`, `left`, `right`)
* Loop control using shrinking dimensions
* Directional sweeps (→ ↓ ← ↑)

## Plan
Use four boundary pointers: `top`, `bottom`, `left`, and `right` to simulate a spiral.
At each step:
1. Traverse from left to right along the top row
2. Traverse down the rightmost column
3. Traverse from right to left along the bottom row (if still within bounds)
4. Traverse up the leftmost column (if still within bounds)

**Pseudocode**:
```
Initialize spiral = []
Initialize top = 0, bottom = number of rows - 1
Initialize left = 0, right = number of columns - 1
While top <= bottom and left <= right:
    Traverse top row → spiral.append each element
    Move top boundary down
    Traverse right column ↓
    Move right boundary left
    If still within vertical bounds:
        Traverse bottom row ←
        Move bottom boundary up
    If still within horizontal bounds:
        Traverse left column ↑
        Move left boundary right
Return spiral
```

## Implement
```
def spiralOrder(matrix):
    spiral = []
    if not matrix or not matrix[0]:
        return spiral

    top, left, bottom, right = 0, 0, len(matrix)-1, len(matrix[0])-1

    while top <= bottom and left <= right:
        for lr in range(left, right+1):
            spiral.append(matrix[top][lr])
        top += 1

        for tb in range(top, bottom+1):
            spiral.append(matrix[tb][right])
        right -= 1

        if top <= bottom:
            for rl in range(right, left-1, -1):
                spiral.append(matrix[bottom][rl])
            bottom -= 1

        if left <= right:
            for bt in range(bottom, top-1, -1):
                spiral.append(matrix[bt][left])
            left += 1

    return spiral
```

## Review

Run test cases to ensure correctness:

```
print(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

print(spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
# Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

print(spiralOrder([[42]]))                # Output: [42]
print(spiralOrder([[1], [2], [3], [4]]))  # Output: [1, 2, 3, 4]
print(spiralOrder([[]]))                  # Output: []
```

## Evaluate

* **Time Complexity**: O(m × n) – Each element is visited exactly once
* **Space Complexity**:
  * O(m × n) for the output list
  * O(1) auxiliary space for boundary variables
* **Trade-offs**: This approach avoids recursion or extra memory and handles all edge cases with simple loop control

## Running the Code
1. Save the code in `main.py`
2. Run it using Python 3:

```
python main.py
```

## Output
```
[1, 2, 3, 6, 9, 8, 7, 4, 5]
[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
[42]
[1, 2, 3, 4]
[]
```

## License
This project is licensed under the MIT License.