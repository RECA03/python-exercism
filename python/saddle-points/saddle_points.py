def saddle_points(matrix):

    if matrix == []:
        return []

    test_row = len(matrix[0])

    candidate_trees = []
    tallest_hor, shortest_ver = True, True  #default values, in case single rows or columns cases happen
    for row_num, row in enumerate(matrix):
        #validate rows have equal length
        if len(row) != test_row:
            raise ValueError("irregular matrix")
        
        #validate if it is the tallest tree horizontally
        for col_num, tree in enumerate(row):
            for number in range(len(row)):
                if col_num == number:
                    continue
                if tree < row[number]:
                    tallest_hor = False
                    break
                tallest_hor = True
            if tallest_hor == False:
                continue

            #validate if it is the smallest tree vertically
            for number in range(len(matrix)):
                if row_num == number:
                    continue
                if tree > matrix[number][col_num]:
                    shortest_ver = False
                    break
                shortest_ver = True
            if shortest_ver == False:
                continue

            if shortest_ver and tallest_hor:
                coords = {"row":row_num+1,"column":col_num+1}
                candidate_trees.append(coords)

    return candidate_trees