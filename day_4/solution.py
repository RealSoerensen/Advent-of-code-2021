# Create bingo board
class BingoBoard:
    # Initialize bingo board
    def __init__(self, input_string):
        self.is_bingo = False
        # Initialize rows and cols
        self.rows = [set() for _ in range(5)]
        self.cols = [set() for _ in range(5)]

        lines = input_string.split("\n")
        # Make board 5x5
        for r in range(5):
            nums = list(map(int, lines[r].split()))
            for c in range(5):
                # Add num to rows and cols
                self.rows[r].add(nums[c])
                self.cols[c].add(nums[c])

    # Check if bingo
    def play(self, num):
        for i in range(5):
            # Check if num in row
            self.rows[i].discard(num)
            self.cols[i].discard(num)
            # If either row or col is empty, bingo
            if len(self.rows[i]) == 0 or len(self.cols[i]) == 0:
                self.is_bingo = True
        # return result of bingo
        return self.is_bingo

    def get_sum(self):
        # Get sum of rows and cols
        return sum([sum(self.rows[i]) for i in range(5)])

def part_1(boards, nums):
    for num in nums:
        for board in boards:
            is_bingo = board.play(num)
            # If bingo, return sum of board times num
            if is_bingo:
                return num * board.get_sum()

def part_2(boards, nums):
    last_winner = None
    for num in nums:
        for board in boards:
            # If bingo and not last winner, continue
            if board.is_bingo:
                continue
            # If bingo and last winner, return sum of board times num
            is_bingo = board.play(num)
            if is_bingo:
                last_winner = board.get_sum() * num
    return last_winner

if __name__ == "__main__":
    with open("day_4/input.txt") as f:
        boards = []
        parts = f.read().split("\n\n")
        nums = list(map(int, parts[0].split(",")))
        board_input = parts[1::]
        for bi in board_input:
            boards.append(BingoBoard(bi))

    print(part_1(boards, nums))
    print(part_2(boards, nums))