from statistics import median

# Set constants
ERROR_SCORE_MAP = {')': 3, ']': 57, '}': 1197, '>': 25137}
COMPLETION_SCORE_MAP = {')': 1, ']': 2, '}': 3, '>': 4}
FORWARD = {'(': ')', '[': ']', '{': '}', '<': '>'}
REVERSE = {v: k for k, v in FORWARD.items()}

def part_one(lines):
    score = 0
    # Iterate over each line
    for line in lines:
        symbols = []
        # Iterate over each character in that line
        for char in line:
            # If the character is in the forward map, add it to the symbols list
            if char in FORWARD:
                symbols.append(char)
            # If the character is in the reverse map, 
            # and the last character in the symbols list is the reverse of the character, 
            # remove the last character from the symbols list
            elif REVERSE[char] != symbols.pop():
                # If the symbols list is empty, add the error score to the score
                score += ERROR_SCORE_MAP[char]
                break
    return score
    
def part_two(lines):
    scores = []
    # Iterate over each line
    for line in lines:
        line_score = 0
        symbols = []
        # Iterate over each character in that line
        for char in line:
            # If the character is in the forward map, add it to the symbols list
            if char in FORWARD:
                # Append the character to the symbols list
                symbols.append(char)
            # If the character is in the reverse map,
            # remove the last character from the symbols list,
            # and break
            elif REVERSE[char] != symbols.pop():
                break
        # If the symbols list is empty
        else:
            # Iterate over each character in the symbols list reversed
            for open_chunk in reversed(symbols):
                # Times the current line score by 5
                line_score *= 5
                # Add the completion score to the line score
                line_score += COMPLETION_SCORE_MAP[FORWARD[open_chunk]]
            # Append the line score to the scores list
            scores.append(line_score)

    # Return the median of the scores list
    return int(median(scores))

        
if __name__ == '__main__':
    with open('day_10/input.txt', 'r') as f:
        data = f.read().splitlines()
        
    print(part_one(data))
    print(part_two(data))
    
