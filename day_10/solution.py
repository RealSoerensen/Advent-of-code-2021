import sys
from statistics import median

ERROR_SCORE_MAP = {')': 3, ']': 57, '}': 1197, '>': 25137}
COMPLETION_SCORE_MAP = {')': 1, ']': 2, '}': 3, '>': 4}
FORWARD = {'(': ')', '[': ']', '{': '}', '<': '>'}
REVERSE = {v: k for k, v in FORWARD.items()}

def part_one(lines):
    score = 0
    for line in lines:
        symbols = []
        for char in line:
            if char in FORWARD:
                symbols.append(char)
            elif REVERSE[char] != symbols.pop():
                score += ERROR_SCORE_MAP[char]
                break
    return score
    
def part_two(lines):
    scores = []
    for line in lines:
        line_score = 0
        symbols = []
        for char in line:
            if char in FORWARD:
                symbols.append(char)
            elif REVERSE[char] != symbols.pop():
                break
        else:
            for open_chunk in reversed(symbols):
                line_score *= 5
                line_score += COMPLETION_SCORE_MAP[FORWARD[open_chunk]]
            scores.append(line_score)

    return int(median(scores))

        
if __name__ == '__main__':
    with open('day_10/input.txt', 'r') as f:
        data = f.read().splitlines()
        
    print(part_one(data))
    print(part_two(data))
    
