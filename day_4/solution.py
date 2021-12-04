from typing import List
file = open("day_4/input.txt").read()

class BingoBoard:
    def __init__(self, input_string):
        self.is_bingo = False
        # storing rows and cols separately to easily check for BINGO
        self.rows = [set() for _ in range(5)]
        self.cols = [set() for _ in range(5)]

        lines = input_string.split("\n")
        for r in range(5):  # no error checking here, assuming 5
            nums = list(map(int, lines[r].split()))
            for c in range(5):
                self.rows[r].add(nums[c])
                self.cols[c].add(nums[c])

    def play(self, num):  # return true if BINGO
        for i in range(5):
            self.rows[i].discard(num)
            self.cols[i].discard(num)
            if len(self.rows[i]) == 0 or len(self.cols[i]) == 0:
                self.is_bingo = True
        return self.is_bingo

    def get_sum(self):
        return sum([sum(self.rows[i]) for i in range(5)])

def parse(file: str):
    boards = []
    parts = file.split("\n\n")
    nums = list(map(int, parts[0].split(",")))
    board_input = parts[1::]
    for bi in board_input:
        boards.append(BingoBoard(bi))
    return boards, nums

def part_1(file: str) -> int:
    boards, nums = parse(file)

    for num in nums:
        for board in boards:
            is_bingo = board.play(num)
            if is_bingo:
                return num * board.get_sum()

def part_2(file: str) -> int:
    boards, nums = parse(file)
    last_winner = None
    for num in nums:
        for board in boards:
            if board.is_bingo:
                continue
            is_bingo = board.play(num)
            if is_bingo:
                last_winner = board.get_sum() * num
    return last_winner

if __name__ == "__main__":
    print(part_1(file))
    print(part_2(file))