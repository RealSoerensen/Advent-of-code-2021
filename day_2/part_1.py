file = open("day_2/input.txt", "r")

def main(file):
    nums = file.readlines()
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

if __name__ == "__main__":
    print(main(file))
        