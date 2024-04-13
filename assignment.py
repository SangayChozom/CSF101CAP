def read_input_file(file_path):
    
    #Initialize empty list to store number of rounds played
    num_rounds = []
    with open(file_path, 'r') as file: #opening input file
        for line in file:
            player_opt, outcome = line.strip().split() #split each line and extract
            num_rounds.append((player_opt, outcome)) #append player_opt, outcome
    return num_rounds

def calculate_score(num_rounds):

    #Compute the total score based on the number of rounds played.
    total_score = 0
    for player_opt, outcome in num_rounds:
        player_opt_score = {"A": 1, "B": 2, "C": 3}.get(player_opt, 0)
        outcome_score = {"X": 0, "Y": 3, "Z": 6}.get(outcome, 0)
        
        total_score += player_opt_score + outcome_score  
    return total_score

# calling read_input functions to read file extracting number of rounds assigned to new variable.
file_path =  "input_6_cap1.txt"  # Replace with the path to your input file
num_rounds = read_input_file(file_path)
final_score = calculate_score(num_rounds)
#print total score
print("Total Score:", final_score)