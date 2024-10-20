import random

class CheckLine:
    """
    Class that encapsulates the methods used for line detection.
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
    """
    Print the matrix to the console.
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="    ")
        print("\n")
        


def add_score(figure, length = 0):
    """
    Input:
    -length (int): for the line figure only (3, 4 or 5) or 0 if the figure is not a line
    -figure (str): line, L or T
    
    Output:
    - an integer value, representing the score of a given figure
    """
    line = {3:5, 4:10, 5:50}
    if figure == "line":
        return line[length]
    elif figure == "L":
        return 20
    else:
        return 30


#############################################################
def crush_candies(matrix, position, mode, figure, length=3):
    """
    Input:
    -position (list): x and y position where the formation begins
    -mode (str): vertical or horizontal
    -figure (str): for now is line
    -length (int): the length of the line (3,4,5)
    
    Output:
    - the modified matrix
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


def check_figures(matrix):
    """
    Check if there are existing line figures in our matrix.
    Output:
    - position (list), i (int) and mode (str) of the found figure
    or
    - False (bool) if no figure was found.
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



def check_random_matrix(matrix, score):
    """
    Check a matrix if we have candies to crush, without making a move. Crush the candies untill we no longer have a figure (line/L/T).
    
    Output:
    - score (int) 
    and
    - the modified matrix
    """
    
    flag = True
    
    while flag:
        try:
            position, length, mode = check_figures(matrix)
            
            new_matrix = crush_candies(matrix, position, mode, length)
            matrix = new_matrix[:]
            score += add_score('line', length)
            # Stop the game if we reached the score of 10.000
            if score >= 10000:
                break
        
        except:
            # If the function returned False, it means we don't have any line that we could crush
            flag = False
    
    return score, matrix



class PlayGame:
    def __init__(self, score):
        #self.figures = [['line', 5], ['L'], ['T'], ['line', 4], ['line', 3]]
        self.figures = [['line']]
        self.score = score
        
        
    def find_possible(self, matrix):
        print(f"Trying to find a possible move")
        
        # Search for a possible move to make the figure
        found = False
        mode = None
        
        for length in [5,4,3]:
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    found, direction = self.try_candy(matrix, length, i, j, "horizontal")
                    mode = "horizontal"
                    
                    # If there was no possible horizontal move, try moving the candy vertical
                    if not found:
                        found, direction = self.try_candy(matrix, length, i, j, "vertical") #vertical
                        mode = "vertical"
                    
                    if found:
                        print(f"Move the candy[{i}][{j}] {mode}-{direction}.")
                        return (i, j), mode, direction
            print(f"Did not find a possible move to make a line of size {length}")
            
        return found
    
    
    
    def try_candy(self, matrix, length, row, column, mode):
        """
        Check if moving a candy will make a figure (line).
        """
        flag = False
        direction = None
        
        if mode == "horizontal":
            # If we are 'length' steps till the right border
            if column < len(matrix[0]) - length:
                direction = 'right'
                for j in range(column+2, column + length + 1):
                    if matrix[row][column] != matrix[row][j]:
                        flag = False
                        break
                    flag = True
            
            # If it is not possible to move to the right, try to the left
            if not flag and (column >= length):
                direction = 'left'
                for j in range(column - length, column - 1):
                    if matrix[row][column] != matrix[row][j]:
                        flag = False
                        break
                    flag = True
        
        
        elif mode == "vertical":
            # If we are 'length' steps till the bottom border
            if row < len(matrix) - length:
                direction = 'down'
                for i in range(row+2, row + length + 1):
                    if matrix[row][column] != matrix[i][column]:
                        flag = False
                        break
                    flag = True
            
            # If it is not possible to move down, try up
            if not flag and (row >= length):
                direction = 'up'
                for i in range(row - length, row - 1):
                    if matrix[row][column] != matrix[i][column]:
                        flag = False
                        break
                    flag = True
        
        return flag, direction
    
    
    def move_candy(self, matrix, positions, mode, direction):
        """
        Interchange candies.
        """
        row = positions[0]
        column = positions[1]
        temp = matrix[row][column]
        
        if mode == "horizontal":
            if direction == 'right':
                matrix[row][column] = matrix[row][column + 1]
                matrix[row][column + 1] = temp
            else:
                matrix[row][column] = matrix[row][column - 1]
                matrix[row][column - 1] = temp
        
        else:
            if direction == 'down':
                matrix[row][column] = matrix[row + 1][column]
                matrix[row + 1][column] = temp
            else:
                matrix[row][column] = matrix[row - 1][column]
                matrix[row - 1][column] = temp
        print("INTERCHANGED MATRIX")
        show_matrix(matrix)
        
        return matrix
    
    
    def start(self, matrix):
        
        try:
            # if we find a figure, we modify the matrix, crush the candies and add the score, then we start the search from the beggining
            positions, mode, direction = self.find_possible(matrix)
            
            matrix = self.move_candy(matrix, positions, mode, direction)
            
            new_score, new_matrix = check_random_matrix(matrix, self.score)
            
            return True, new_score, new_matrix
        except Exception as e:
            print(e)
            pass
        
        return False
    