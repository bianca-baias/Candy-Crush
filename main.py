import random
import play


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
    
    play.show_matrix(matrix)
    
    # Check if we already have some figure line/L/T in the matrix newly created
    extra_score, new_matrix =  play.check_random_matrix(matrix, score)
    score += extra_score
    matrix = new_matrix[:]
    return score, matrix



def main():
    dimension = 11
    games = 10
    average_score = 0
    counter = 0
    #figures = [['line', 5], ['L'], ['T'], ['line', 4], ['line', 3]]
    
    for game in range(games):
        # Create and check matrix for initial figures
        score = 0
        extra_score, matrix = prepare_matrix(dimension)
        score += extra_score
        
        # Now we can begin the game
        print("STARTING GAME")
        
        run = True
        while run:
            round = play.PlayGame(score)
            
            # Play the game
            try:
                # Try to find a figure
                run, new_score, new_matrix, new_counter = round.start(matrix)
                matrix = new_matrix[:]
                score = new_score
                counter += new_counter
                
                if score >= 10000:
                    run = False
                    average_score += score
                    print(f"Stopping game, score is greater than 10.000 for game {game + 1}: score {score}, moves {counter}")
            
            except Exception as e:
                # If we did not find a figure, game over
                print(e)
                run = False
                average_score += score
                print(f"No possible move for game {game}: score {score}, moves {counter}")
    
    print("-----------------------------------------------------")
    print(f"Played {games} games \nAverage score: {average_score / games} \nAverage moves: {counter / games}")

if __name__ == "__main__":
    main()