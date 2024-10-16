import random

class CheckLine:
    """
    """
    
    def __init__(self):
        pass
    
    
    def check_horizontal(self, matrix, line_size):
            flag = False
            
            for i in range(len(matrix)):
                for j in range(len(matrix[i]) - line_size + 1):
                    # Take the line_size (3, 4 or 5) elements from the current position
                    my_line = matrix[i][j:j+line_size]
                    
                    if my_line.count(my_line[0]) == len(my_line):
                        print(f"Matching {line_size} horizontal at position: line {i+1}, column {j+1} and the next {line_size - 1}")
                        flag = True
                        return (i, j)
            
            if not flag:
                print(f"Could not find {line_size} candies to match horizontally...")
                return flag
        
        
    def check_vertical(self, matrix, line_size):
                flag = False

                # i is the column, j is the line
                for i in range(len(matrix)):
                    for j in range(len(matrix[i]) - line_size + 1):
                        # Take the line_size (3, 4 or 5) elements from the current position
                        my_line = [matrix[x][i] for x in range(j, j + line_size)]
                        if my_line.count(my_line[0]) == len(my_line):
                            print(f"Matching {line_size} vertical at position: line {j+1}, column {i+1} and the next {line_size - 1}")
                            flag = True
                            return (j, i)
                
                if not flag:
                    print(f"Could not find {line_size} candies to match vertically...")
                    return flag


#############################################################

class CheckL:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def check_horizontal():
        pass
    
    def check_vertical():
        pass

#############################################################

class CheckT:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def check_horizontal():
        pass
    
    def check_vertical():
        pass


#############################################################

def show_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="    ")
        print("\n")
        


def add_score(figure, length = 0):
    """
    length: for line figure only (3, 4 or 5) or 0 if the figure is not a line
    figure: line, L or T
    """
    line = {3:5, 4:10, 5:50}
    if figure == "line":
        return line[length]
    elif figure == "L":
        return 20
    else:
        return 30


#############################################################
def crush_candies(matrix, position, mode, length):
    """
    Position: list 0-x position starting with 0, 1-y position starting with 0;
    length: int the length of the line (3,4,5)
    """
    if mode == "horizontal":
        for i in range(position[0], 0, -1):
            for j in range(position[1], position[1] + length):
                matrix[i][j] = matrix[i-1][j]
        
        for column in range(position[1], position[1] + length):
            matrix[0][column] = random.randint(1,4)
    
    elif mode == "vertical":
        for i in range(position[0] + length - 1, 0, -1):
            if i >= length:
                matrix[i][position[1]] = matrix[i - length][position[1]]
            else:
                matrix[i][position[1]] = random.randint(1,4)
        matrix[0][position[1]] = random.randint(1,4)
    
    print("Crushed matrix:")
    show_matrix(matrix)
    
    return matrix


def check_line_figures(matrix):
    """
    Check if there are existing line figures in our matrix.
    """
    check_line = CheckLine()
    length = 5
    
    for i in range(length, 2, -1):
        position = check_line.check_horizontal(matrix, i)
        mode = "horizontal"
        
        # If there was no line found horizontal, try vertical
        if not position:
            position = check_line.check_vertical(matrix, i)
            mode = "vertical"
        
        if position:
            return position, i, mode
    
    return False



def check_random_matrix(matrix):
    """
    Check a matrix if we have candies to crush, without making a move. Crush the candies untill we no longer have a figure (line/L/T).
    """
    score = 0
    
    flag = True
    
    while flag:
        try:
            position, length, mode = check_line_figures(matrix)
            
            new_matrix = crush_candies(matrix, position, mode, length)
            matrix = new_matrix[:]
            score += add_score("line", length)
        
        except:
            # If the function returned False, it means we don't have any line that we could crush
            flag = False
    
    return score