def spiralOrder(matrix):
    spiral = []
    if not matrix or not matrix[0]:
        return []
    # We can use a four-corners approach and slowly close in on the matrix
    top, left, bottom, right = (0, 0, len(matrix)-1, len(matrix[0])-1)
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

print(spiralOrder([
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
])) # output = [1, 2, 3, 6, 9, 8, 7, 4, 5]

print(spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
])) # output = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]