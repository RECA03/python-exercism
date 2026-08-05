def convert(input_grid):
    
    if len(input_grid)%4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    for char_line in input_grid:
        if len(char_line)%3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")

    #separate cell lines
    cell_lines = []
    for ind in range(0,len(input_grid),4):
        cell_line = input_grid[ind:ind+4]
        
        number_line = ""
        for index in range(0,len(cell_line[0]),3):
            top, middle, bottom, blank = cell_line[0][index:index+3], cell_line[1][index:index+3], cell_line[2][index:index+3], cell_line[3][index:index+3]

            if blank == "   ":
                #0
                if top == " _ " and middle == "| |" and bottom == "|_|":
                    number_line += "0"
                #1
                elif top == "   " and middle == "  |" and bottom == "  |":
                    number_line += "1"
                #2
                elif top == " _ " and middle == " _|" and bottom == "|_ ":
                    number_line += "2"
                #3
                elif top == " _ " and middle == " _|" and bottom == " _|":
                    number_line += "3"
                #4
                elif top == "   " and middle == "|_|" and bottom == "  |":
                    number_line += "4"
                #5
                elif top == " _ " and middle == "|_ " and bottom == " _|":
                    number_line += "5"
                #6
                elif top == " _ " and middle == "|_ " and bottom == "|_|":
                    number_line += "6"
                #7
                elif top == " _ " and middle == "  |" and bottom == "  |":
                    number_line += "7"
                #8
                elif top == " _ " and middle == "|_|" and bottom == "|_|":
                    number_line += "8"
                #9
                elif top == " _ " and middle == "|_|" and bottom == " _|":
                    number_line += "9"
                #?
                else:
                    number_line += "?"
        
        cell_lines.append(number_line)

    return ",".join(cell_lines)