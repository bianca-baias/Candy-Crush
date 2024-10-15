import random


def create_matrix(size):
    """
    """
    matrix = []
    
    for i in range(size):
        matrix.append([])
        for j in range(size):
            matrix[i].append(random.randint(1, 4))
            
    return matrix


class CheckLine:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def check_horizontal(self, line_size):
            flag = False
            
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i]) - line_size + 1):
                    # Take the line_size (3, 4 or 5) elements from the current position
                    my_line = self.matrix[i][j:j+line_size]
                    
                    if my_line.count(my_line[0]) == len(my_line):
                        print(f"Matching {line_size} horizontal at position: line {i+1}, column {j+1} and the next {line_size - 1}")
                        flag = True
                        return (i, j)
            
            if not flag:
                print(f"Could not find {line_size} candies to match horizontally...")
                return flag
        
        
    def check_vertical(self, line_size):
                flag = False

                # i is the column, j is the line
                for i in range(len(self.matrix)):
                    for j in range(len(self.matrix[i]) - line_size + 1):
                        # Take the line_size (3, 4 or 5) elements from the current position
                        my_line = [self.matrix[x][i] for x in range(j, j + line_size)]
                        if my_line.count(my_line[0]) == len(my_line):
                            print(f"Matching {line_size} vertical at position: line {j+1}, column {i+1} and the next {line_size - 1}")
                            flag = True
                            return (j, i)
                
                if not flag:
                    print(f"Could not find {line_size} candies to match vertically...")
                    return flag
    
    

class CheckL:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def check_horizontal():
        pass
    
    def check_vertical():
        pass



class CheckT:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def check_horizontal():
        pass
    
    def check_vertical():
        pass


def check_lines(matrix):
    check_line = CheckLine(matrix)
    
    if check_line.check_horizontal(5):
        # crush
        pass
        
    elif check_line.check_vertical(5):
        # crush
        pass
    elif check_line.check_horizontal(4):
        # crush
        pass
        
    elif check_line.check_vertical(4):
        # crush
        pass
        
    elif check_line.check_horizontal(3):
        #crush
        pass
        
    elif check_line.check_vertical(3):
        # crush
        pass
        
    else:
        # 
        pass


def check_L(matrix):
    L_formation = CheckL(matrix)


def check_T(matrix):
    T_formation = CheckT(matrix)


def show_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="    ")
        print("\n")


def main():
    dimension = 6
    games = 1
    
    for game in range(games):
        matrix = create_matrix(dimension)
        
        show_matrix(matrix)
        
        run = True
        
        while run:
            
            check_lines(matrix)
            
            run = False


if __name__ == "__main__":
    main()