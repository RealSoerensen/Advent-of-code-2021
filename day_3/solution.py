from collections import Counter

def part_1(nums):
    # Get the max length of the number
    maxlen = len(max(nums, key=len))
    # Get the number of digits in the number
    counters = [Counter() for _ in range(maxlen)]
    # Iterate over the digits
    for num in nums:
        # Iterate over the digits in num
        for i, v in enumerate(num):
            # Update the counter for the digit
            counters[i].update(v)
            
    gamma, epsilon = "", ""
    # Iterate over the counters
    for c in counters:
        # Get the most common digit
        if c["0"] > c["1"]:
            gamma = gamma + "0"
            epsilon = epsilon + "1"
        else:
            gamma = gamma + "1"
            epsilon = epsilon + "0"
    # Return the product of the two numbers timed by each other
    return int(gamma, 2) * int(epsilon, 2)

def part_2(nums):
    maxlen = len(max(nums, key=len))
    res = 1
    for is_co2 in [False, True]:
        new_list = nums.copy()
        for i in range(maxlen):
            counter = Counter()
            # Iterate over the digits
            for num in nums:
                # Get the digit at the given index
                counter.update(num[i])
            # Get the most common digit and return it
            c0, c1 = counter["0"], counter["1"]
            if not is_co2:
                criteria = ["1" if c1 >= c0 else "0"]
            else:
                criteria = ["0" if c0 <= c1 else "1"]
            
            # Iterate over the digits
            new_list = [n for n in nums if n[i] == criteria]
            # If len is 1, break
            if len(new_list) == 1:
                break
        # Multiply the result by the number
        res = res * int(new_list[0], 2)

    return res


if __name__ == "__main__":
    with open("day_3/input.txt") as f:
        nums = f.read().splitlines()
    print(part_1(nums))
    print(part_2(nums))