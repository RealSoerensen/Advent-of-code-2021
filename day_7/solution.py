import statistics

def part_one(data):
    median = statistics.median(data)
    # Return the median which is the answer for what is closest for each crab
    return int(sum(abs(median - place) for place in data))

def part_two(data):
    # Return the cheapest outcome
    return min(sum(abs(i - x) * (abs(i - x) + 1) // 2 for i in data) for x in range(max(data)))


if __name__ == '__main__':
    with open('day_7/input.txt', 'r') as f:
        lines = f.read().split(",")
        lines = [int(line) for line in lines]
    print(part_one(lines))
    print(part_two(lines))