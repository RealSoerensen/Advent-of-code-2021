def part_1(nums):
    start_num = nums[0]
    increased = 0
    # Iterate through the list
    for num in nums:
        # If the number is greater than the start number, increase the counter
        if int(num) > int(start_num):
            increased += 1
        start_num = num

    return increased

def part_2(nums):
    # Set the start number to be the sum of the first 3 numbers
    start_num = sum([nums[0], nums[1], nums[2]])
    increased = 0
    # Iterate through the list one at a time
    for i, num in enumerate(nums):
        # Get the next 3 num and get the sum
        try:
            sum_numbers = sum([int(num),  int(nums[i + 1]), int(nums[i + 2])])
            if sum_numbers > int(start_num):
                increased += 1 
            start_num = sum_numbers
        # If the list is less than 3 which causes an IndexError, break
        except IndexError:
            break
    return increased

if __name__ == "__main__":
    with open("day_1/input.txt", "r") as f:
        nums = f.read().splitlines()

    print(part_1(nums))
    print(part_2(nums))