from typing import List
from collections import Counter

file = open("day_3/input.txt").read()

def find_bit_criteria(nums: list, i: int, is_co2: bool):
    counter = Counter()
    for num in nums:
        counter.update(num[i])
    c0, c1 = counter["0"], counter["1"]
    if not is_co2:
        return "1" if c1 >= c0 else "0"
    else:
        return "0" if c0 <= c1 else "1"


def eliminate_nums(nums: list, i: int, criteria: str) -> list:
    return [n for n in nums if n[i] == criteria]


def main(file):
    nums = file.readlines()
    maxlen = len(max(nums, key=len))
    res = 1
    for is_co2 in [False, True]:
        new_list = nums.copy()
        for i in range(maxlen):
            criteria = find_bit_criteria(new_list, i, is_co2)
            new_list = eliminate_nums(new_list, i, criteria)
            if len(new_list) == 1:
                break
        res = res * int(new_list[0], 2)
    return res

if __name__ == "__main__":
    print(main(file))