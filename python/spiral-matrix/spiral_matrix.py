def spiral_matrix(size):
    
    if size == 0:
        return []

    matrix = [[0]*size for _ in range(size)] #make an empty matrix of 0s
    
    top, bottom = 0, size-1
    left, right = 0, size-1
    num = 1

    while num <= size**2:
        #top row
        for i in range(left,right+1):
            matrix[top][i] = num
            num += 1
        top += 1

        #right column
        for i in range(top,bottom+1):
            matrix[i][right] = num
            num += 1
        right -= 1

        #bottom row
        for i in range(right, left -1,-1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        #left column
        for i in range(bottom, top-1,-1):
            matrix[i][left] = num
            num += 1
        left += 1

    return matrix

print(spiral_matrix(5))