file = open("day_1/input.txt", "r")
nums = file.readlines()

def part_1(nums):
    start_num = 150
    increased = 0
    for num in nums:
        if int(num) > int(start_num):
            increased += 1
        start_num = num

    return increased

def part_2(nums):
    start_num = 457
    increased = 0
    for i, num in enumerate(nums):
        try:
            sum_numbers = sum([int(num),  int(nums[i + 1]), int(nums[i + 2])])
            if sum_numbers > start_num:
                increased += 1 
            start_num = sum_numbers
        except IndexError:
            break
    return increased

if __name__ == "__main__":
    print(part_1(nums), "measurements were larger than the previous measurement")
    print(part_2(nums), "measurements were larger than the previous measurement")