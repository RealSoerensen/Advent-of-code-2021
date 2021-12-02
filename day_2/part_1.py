with open("nums.txt", "r") as f:
    nums = f.readlines()
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

    print(str(depth*horizontal))
        