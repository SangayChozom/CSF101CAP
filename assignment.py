def read_input_file(file_path):
    
    #Initialize empty list to store number of rounds played
    num_rounds = []
    with open(file_path, 'r') as file: #opening input file
        for line in file:
            shape, outcome = line.strip().split() #split each line and extract
            num_rounds.append((shape, outcome)) #append shape, outcome
    return num_rounds

def calculate_score(num_rounds):

    #Compute the total score based on the number of rounds played.
    total_score = 0
    for shape, outcome in num_rounds:
        shape_score = {"A": 1, "B": 2, "C": 3}.get(shape, 0)
        outcome_score = {"X": 0, "Y": 3, "Z": 6}.get(outcome, 0)
        total_score += shape_score + outcome_score  

    return total_score

# calling read_input functions to read file extracting number of rounds assigned to new variable.
file_path =  "input_6_cap1.txt"  # Replace with the path to your input file
num_rounds = read_input_file(file_path)
sum_score = calculate_score(num_rounds)
#print total score
print("Total Score:", sum_score)