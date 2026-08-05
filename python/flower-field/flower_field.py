def annotate(garden):
    # Function body starts here

    if len(garden) == 0:
        return []

    #possible (row, col) pairs
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    total_rows = len(garden)
    total_columns = len(garden[0])

    #convert the rows from str to lists
    for i, garden_row in enumerate(garden):
        #break if flower field isnt even
        if len(garden_row) != total_columns:
            raise ValueError("The board is invalid with current input.")
        for space in garden_row:
            if space not in " *":
                raise ValueError("The board is invalid with current input.")

        garden[i] = list(garden_row)
    print(garden)


    #flower counter
    for row_num, garden_row in enumerate(garden):
        for space_num, space in enumerate(garden_row):
            flower_counter = 0
            if space == "*":
                continue
            for offset in offsets:
                row, col = offset
                neighbor_row = row + row_num 
                neighbor_col = col + space_num
                if neighbor_row not in range(total_rows):
                    continue
                elif neighbor_col not in range(total_columns):
                    continue

                if garden[neighbor_row][neighbor_col] == "*":
                    flower_counter += 1
            if flower_counter > 0:
                garden_row[space_num] = str(flower_counter)
            else:
                garden_row[space_num] = " "

    for row_num, garden_row in enumerate(garden):
        garden[row_num] = "".join(garden_row)

    return garden