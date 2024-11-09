import random

class CheckLine:
    """
    Class that encapsulates the methods used for line detection.
    """
    
    def check_horizontal(self, matrix, line_size):
        flag = False
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i]) - line_size + 1):
                # Take the line_size (3, 4 or 5) elements right from the current position
                my_line = matrix[i][j:j+line_size]
                
                if my_line.count(my_line[0]) == len(my_line):
                    #print(f"Matching {line_size} horizontal at position: line {i+1}, column {j+1} and the next {line_size - 1}")
                    flag = True
                    return (i, j)
        
        return flag
    
        
    def check_vertical(self, matrix, line_size):
        flag = False
        
        # i is the column, j is the line
        for i in range(len(matrix)):
            for j in range(len(matrix[i]) - line_size + 1):
                # Take the line_size (3, 4 or 5) elements from the current position
                my_line = [matrix[x][i] for x in range(j, j + line_size)]
                if my_line.count(my_line[0]) == len(my_line):
                    flag = True
                    return (j, i)
        
        return flag


    def check_line_3(self, matrix):
        """
        """
        directions = [["vertical", "down"], ["vertical", "up"], ["horizontal", "left"], ["horizontal", "right"]]
        flag = False
        length = 3
        
        for row in range(len(matrix)):
            for column in range(len(matrix)):
                positions = (row, column)
                for direction in directions:
                    ##########################################################################################
                    if direction[1]== "right":
                        
                        # Check if there is a horizontal line forming to the right
                        if column < (len(matrix[0]) - length):
                            #print("Checking right")
                            if matrix[row][column] == matrix[row][column+2]==matrix[row][column+3]:
                                flag = True
                                break
                        
                        if column < len(matrix[0]) - 1:
                            if row <= (len(matrix) - length):
                                #print("Checking right-down")
                                # Check if there is a vertical line forming down
                                if matrix[row][column] == matrix[row+1][column+1] == matrix[row+2][column+1]:
                                    flag = True
                                    break
                            
                            # Check if there is a vertical line forming up
                            if row >= length - 1:
                                #print("Checking right-up")
                                if matrix[row][column] == matrix[row-1][column+1] == matrix[row-2][column+1]:
                                    flag = True
                                    break
                            
                            if row in range(1, len(matrix)-1) and matrix[row][column] == matrix[row-1][column+1] == matrix[row+1][column+1]:
                                flag = True
                                break
                    
                    ##########################################################################################
                    elif direction[1] == "left":
                        # Check if there is a horizontal line forming left
                        if column >= length:
                            #print("Checking left")
                            if matrix[row][column] == matrix[row][column-2]==matrix[row][column-3]:
                                flag = True
                                break
                        
                        if column > 0:
                            if row <= (len(matrix) - length):
                                #print("Checking left down")
                                if matrix[row][column] == matrix[row+1][column-1]==matrix[row+2][column-1]:
                                    flag = True
                                    break
                                
                            # Check if there is a vertical line forming up
                            if row >= length - 1:
                                #print("Checking left up")
                                if matrix[row][column] == matrix[row-1][column-1]==matrix[row-2][column-1]:
                                    flag = True
                                    break
                            
                            if row in range(1, len(matrix)) and matrix[row][column] == matrix[row-1][column-1] == matrix[row+1][column-1]:
                                flag = True
                                break
                    ##########################################################################################
                    elif direction[1] == "down":
                        if row <= (len(matrix) - length - 1):
                            #print("Checking down")
                            if matrix[row][column] == matrix[row+2][column]==matrix[row+3][column]:
                                flag = True
                                break
                        
                        if row < len(matrix) - 1:
                            if column >= length - 1:
                                #print("Checking down left")
                                if matrix[row][column] == matrix[row+1][column-1]==matrix[row+1][column-2]:
                                    flag = True
                                    break
                                
                            if column <= len(matrix[0]) - length:
                                #print("Checking down right")
                                if matrix[row][column] == matrix[row+1][column+1]==matrix[row+1][column+2]:
                                    flag = True
                                    break
                        
                            if column in range(1, len(matrix)-1) and matrix[row][column] == matrix[row+1][column - 1] == matrix[row+1][column+1]:
                                    flag = True
                                    break
                    ##########################################################################################
                    elif direction[1]  == "up":
                        if row >= length:
                            #print("Checking up")
                            if matrix[row][column] == matrix[row-2][column]==matrix[row-3][column]:
                                flag = True
                                break
                        
                        if row > 0:
                            if column >= length - 1:
                                #print("Checking up-left")
                                if matrix[row][column] == matrix[row-1][column-1]==matrix[row-1][column-2]:
                                    flag = True
                                    break
                                
                            if column <= len(matrix[0]) - length:
                                #print("Checking up-right")
                                if matrix[row][column] == matrix[row-1][column+1]==matrix[row-1][column+2]:
                                    flag = True
                                    break
                            
                            if column in range(1, len(matrix)-1) and matrix[row][column] == matrix[row-1][column-1] == matrix[row-1][column+1]:
                                flag = True
                                break
                if flag:
                    return direction, positions
        
        return False, None
    
    
    def check_line_4(self, matrix):
        """
        
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i < len(matrix)-3:
                    # check if there is a column of 4 elements possible
                    if matrix[i][j]==matrix[i+1][j] == matrix[i+3][j]:
                        if j < len(matrix)-1:
                            if matrix[i][j] == matrix[i+2][j+1]:
                                return ["horizontal","left"], (i+2, j+1) 
                        
                        if j > 0:
                            if matrix[i][j] == matrix[i+2][j-1]:
                                return ["horizontal","right"], (i+2, j-1)
                    
                    if matrix[i][j] == matrix[i+2][j] == matrix[i+3][j]:
                        if j< len(matrix)-1:
                            if matrix[i][j] == matrix[i+1][j+1]:
                                return ["horizontal","left"], (i+1, j+1) 
                        
                        if j > 0:
                            if matrix[i][j] == matrix[i+1][j-1]:
                                return ["horizontal","right"], (i+1, j-1)
                
                # check if there is a line of 4 elements possible
                if j < len(matrix)-3:
                    if matrix[i][j] == matrix[i][j+1] == matrix[i][j+3]:
                        if i > 0:
                            if matrix[i][j] == matrix[i-1][j+2]:
                                return ["vertical", "down"], (i-1, j+2)
                            
                        if i < len(matrix)-1:
                            if matrix[i][j] == matrix[i+1][j+2]:
                                return ["vertical", "up"], (i+1, j+2)
                    
                    if matrix[i][j] == matrix[i][j+2]== matrix[i][j+3]:
                        if i > 0:
                            if matrix[i][j] == matrix[i-1][j+1]:
                                return ["vertical", "down"], (i-1, j+1)
                        
                        if i < len(matrix) - 1:
                            if matrix[i][j] == matrix[i+1][j+1]:
                                return ["vertical", "up"], (i+1, j+1)
                    
        return False, None
    
    
    def check_line_5(self, matrix):
        """
        
        """
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                # check if there is a column of 5 elements possible
                if i < len(matrix)-4:
                    if matrix[i][j]==matrix[i+1][j] == matrix[i+3][j]==matrix[i+4][j]:
                        if j > 0:
                            if matrix[i][j]==matrix[i+2][j-1]:
                                return ["horizontal", "right"], (i+2, j-1)
                        
                        if j < len(matrix)-1:
                            if matrix[i][j]==matrix[i+2][j+1]:
                                return ["horizontal", "left"], (i+2, j+1)
                
                # check if there is a row of 5 elements possible
                if j < len(matrix)-4:
                    if matrix[i][j] == matrix[i][j+1] == matrix[i][j+3] == matrix[i][j+4]:
                        if i > 0:
                            if matrix[i][j]== matrix[i-1][j+2]:
                                return ["vertical", "down"], (i-1, j+2)
                        
                        if i < len(matrix)-1:
                            if matrix[i][j]== matrix[i+1][j+2]:
                                return ["vertical", "up"], (i+1, j+2)
        
        return False, None
#############################################################

class CheckL:
    def check_existing():
        pass
    
    def check_possible(self, matrix):
        pass

#############################################################

class CheckT:
    def check_existing():
        pass
    
    def check_possible(self, matrix):
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
        


def add_score(figure, length=0):
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
def crush_candies(matrix, position, mode, direction, length=3):
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
    
    #print("Crushed matrix:")
    #show_matrix(matrix)
    
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



def check_random_matrix(matrix):
    """
    Check a matrix if we have candies to crush, without making a move. Crush the candies untill we no longer have a figure (line/L/T).
    
    Output:
    - score (int) 
    and
    - the modified matrix
    """
    score = 0
    flag = True
    
    while flag:
        try:
            position, length, mode = check_figures(matrix)
            
            new_matrix = crush_candies(matrix, position, mode, length)
            matrix = new_matrix[:]
            score += add_score('line', length)
        
        except:
            # If the function returned False, it means we don't have any line that we could crush
            flag = False
    
    return score, matrix



class PlayGame:
    def __init__(self):
        #self.figures = [['line', 5], ['L'], ['T'], ['line', 4], ['line', 3]]
        self.figures = [['line']]
        
    
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
        
        return matrix
    
    
    
    def check_formations(self, matrix):
        check_line = CheckLine()
        check_L = CheckL()
        check_T = CheckT()
        
        direction, position = check_line.check_line_5(matrix)
        
        if not direction:
            direction, position = check_line.check_line_4(matrix)
        
        if not direction:
            direction, position = check_line.check_line_3(matrix) 
        
        # if not direction:
        #     direction, position = check_L.check_possible(matrix)
        
        # if not direction:
        #     direction, position = check_T.check_possible(matrix)    
        
        if direction:
            return direction, position
        
        return False
    
    
    def start(self, matrix):
        #figures = [['line', 5], ["line", 4], ["line", 3]]
        #directions = [["vertical", "down"], ["vertical", "up"], ["horizontal", "left"], ["horizontal", "right"]]
        counter = 0
        try:
            direction, positions = self.check_formations(matrix)
            if direction:
                counter += 1
                new_matrix = self.move_candy(matrix, positions, direction[0], direction[1])
                new_score, n_matrix = check_random_matrix(new_matrix)
                matrix = n_matrix[:]
                return True, new_score, matrix, counter
        except Exception as e:
            print(e)
            print("\nNo possible moves:")
            show_matrix(matrix)
        
        return False    
