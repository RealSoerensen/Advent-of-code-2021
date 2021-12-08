def part_one(file):
    final = 0
    uniq = [2, 3, 4, 7]  # 1, 7, 4, 8
    for _, line in file:
        final += len([i for i in line if len(i) in uniq])
    return final


def part_two(file): 
    answer = 0
    for line, out in file:
        line = [set(i) for i in line]
        one = [i for i in line if len(i) == 2][0]
        seven = [i for i in line if len(i) == 3][0]
        four = [i for i in line if len(i) == 4][0]
        eight = [i for i in line if len(i) == 7][0]
        three = [i for i in line if len(i) == 5 and len(i - one) == 3][0]
        two_five = [i for i in line if len(i) == 5 and len(i - three) == 1]
        five = [i for i in two_five if len(i & (four - one)) == 2][0]
        two = [i for i in two_five if len(i & (four - one)) == 1][0]
        six = [i for i in line if len(i) == 6 and len(i & one) == 1][0]
        nine = [i for i in line if len(i) == 6 and len(i & three) == 5][0]
        digits = [one, two, three, four, five, six, seven, eight, nine]
        zero = [i for i in line if i not in digits][0]
        digits = [zero] + digits
        res = 0
        for num in out:
            res *= 10
            res += digits.index(set(num))
        answer += res
    return answer


if __name__ == '__main__':
    teststr = ""
    lmap = lambda *a: list(map(*a))
    with open('day_8/input.txt') as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
        file = lmap(lambda r: lmap(lambda i: i.split(" "), r.split(" | ")), s)
    
    print(part_one(file))
    print(part_two(file))