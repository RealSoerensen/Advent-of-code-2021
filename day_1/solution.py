def part_1(nums):
    start_num = nums[0]
    increased = 0
    for num in nums:
        if int(num) > int(start_num):
            increased += 1
        start_num = num

    return increased

def part_2(nums):
    start_num = nums[0] + nums[1] + nums[2]
    increased = 0
    for i, num in enumerate(nums):
        try:
            sum_numbers = sum([int(num),  int(nums[i + 1]), int(nums[i + 2])])
            if sum_numbers > int(start_num):
                increased += 1 
            start_num = sum_numbers
        except IndexError:
            break
    return increased

if __name__ == "__main__":
    with open("day_1/input.txt", "r") as f:
        nums = f.read().splitlines()

    print(part_1(nums))
    print(part_2(nums))