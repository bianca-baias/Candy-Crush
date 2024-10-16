import random
import utils


def create_matrix(size):
    """
    """
    matrix = []
    
    for i in range(size):
        matrix.append([])
        for j in range(size):
            matrix[i].append(random.randint(1, 4))
            
    return matrix


def show_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="    ")
        print("\n")


def main():
    dimension = 6
    games = 1
    score = 0
    
    for game in range(games):
        matrix = create_matrix(dimension)
        
        show_matrix(matrix)
        
        run = True
        
        # Check if we already have some figure line/L/T in the matrix newly created
        score += utils.check_random_matrix(matrix)
        print(score)
        """
        while run:
            
            # Play the game
            utils.check_lines(matrix)
            
            run = False
        """


if __name__ == "__main__":
    main()