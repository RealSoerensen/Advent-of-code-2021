def part_1(nums):
    # Set starting position
    depth = 0
    horizontal = 0
    # Iterate through instructions
    for num in nums:
        num = num.strip()
        num = num.split(" ")
        # If the instruction is up, down or forward. Move accordingly
        if num[0] == "up":
            depth -= int(num[1])
        elif num[0] == "down":
            depth += int(num[1])
        elif num[0] == "forward":
            horizontal += int(num[1])

    # Return depth times horizontal
    return depth*horizontal

def part_2(nums):
    # Set starting position
    depth = 0
    horizontal = 0
    aim = 0
    # Iterate through instructions
    for num in nums:
        num = num.strip()
        num = num.split(" ")
        # If the instruction is up or down move the aim accordingly
        if num[0] == "up":
            aim -= int(num[1])
        elif num[0] == "down":
            aim += int(num[1])
        # If the instruction is forward, add the aim to the depth and times that with the horizontal
        elif num[0] == "forward":
            horizontal += int(num[1])
            depth = int(num[1])*aim+depth
            
    return depth*horizontal

if __name__ == "__main__":
    with open("day_2/input.txt", "r") as f:
        nums = f.read().splitlines()
    print(part_1(nums))
    print(part_2(nums))
        