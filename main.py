import random
import utils


def create_matrix(size):
    """
    Create a new square matrix of given size.
    """
    matrix = []
    
    for i in range(size):
        matrix.append([])
        for j in range(size):
            matrix[i].append(random.randint(1, 4))
            
    return matrix


def prepare_matrix(dimension):
    """
    Create a new matrix and crush all the possible lines. Return a matrix without any figures, ready to be played.
    """
    score = 0
    matrix = create_matrix(dimension)
    
    show_matrix(matrix)
    
    # Check if we already have some figure line/L/T in the matrix newly created
    extra_score, new_matrix =  utils.check_random_matrix(matrix)
    score += extra_score
    matrix = new_matrix[:]
    return score, matrix


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
        extra_score, matrix = prepare_matrix(dimension)
        score += extra_score
        print(score)
        # Now we can begin the game
        
        """
        while run:
            
            # Play the game
            utils.check_lines(matrix)
            
            run = False
        """


if __name__ == "__main__":
    main()