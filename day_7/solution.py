import statistics

def part_one(input_):
    median = statistics.median(input_)
    return int(sum(abs(median - place) for place in input_))

def part_two(input):
    return min(sum(abs(i - x) * (abs(i - x) + 1) // 2 for i in input) for x in range(max(input)))


if __name__ == '__main__':
    with open('day_7/input.txt', 'r') as f:
        lines = f.read().split(",")
        lines = [int(line) for line in lines]
        
    print(part_one(lines))
    print(part_two(lines))