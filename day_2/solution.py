def part_1(nums):
    depth = 0
    horizontal = 0
    for num in nums:
        num = num.strip()
        num = num.split(" ")
        if num[0] == "up":
            depth -= int(num[1])
        elif num[0] == "down":
            depth += int(num[1])
        elif num[0] == "forward":
            horizontal += int(num[1])

    return depth*horizontal

def part_2(nums):
    depth = 0
    horizontal = 0
    aim = 0
    for num in nums:
        num = num.strip()
        num = num.split(" ")
        if num[0] == "up":
            aim -= int(num[1])
        elif num[0] == "down":
            aim += int(num[1])
        elif num[0] == "forward":
            horizontal += int(num[1])
            depth = int(num[1])*aim+depth
    return depth*horizontal

if __name__ == "__main__":
    with open("day_2/input.txt", "r") as f:
        nums = f.read().splitlines()
    print(part_1(nums))
    print(part_2(nums))
        