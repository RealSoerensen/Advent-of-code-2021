from collections import Counter

file = open("day_3/input.txt")


def main(file):
    nums = file.readlines()
    maxlen = len(max(nums, key=len))
    counters = [Counter() for _ in range(maxlen)]
    for num in nums:
        for i, v in enumerate(num):
            counters[i].update(v)
    gamma, epsilon = "", ""
    for c in counters:
        if c["0"] > c["1"]:
            gamma = gamma + "0"
            epsilon = epsilon + "1"
        else:
            gamma = gamma + "1"
            epsilon = epsilon + "0"
    return int(gamma, 2) * int(epsilon, 2)


if __name__ == "__main__":
    print(main(file))