from collections import Counter
import functools

@functools.lru_cache(maxsize=None)
def count(poly, n):
    if n == 0:
        return Counter(poly)

    if len(poly) > 2:
        return sum(
            (count(poly[i : i + 2], n) for i in range(len(poly) - 1)), Counter()
        ) - Counter(poly[1:-1])

    new = rules[poly]
    return count(poly[0] + new, n - 1) + count(new + poly[1], n - 1) - Counter(new)


def main(n):
    c = count(poly, n)
    most_common = c.most_common()
    return most_common[0][1] - most_common[-1][1]

def part_one():
    return main(10)

def part_two():
    return main(40)

if __name__ == '__main__':
    with open('day_14/input.txt') as f:
        data = f.read().splitlines()
        poly = data[0]
        rules = dict(rule.split(" -> ") for rule in data[2:])
    print(part_one())
    print(part_two())