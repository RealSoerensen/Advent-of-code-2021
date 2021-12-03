file = open("day_2/input.txt", "r")

def main(file):
    nums = file.readlines()
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
        
    return horizontal*depth

if __name__ == "__main__":
    print(main(file))