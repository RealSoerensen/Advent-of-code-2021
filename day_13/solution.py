def part_one(data, points):
    for i, line in enumerate(data):
        (*_, dir), p = line.split("=")
        p = int(p)
        for x, y in tuple(points):
            if dir == "x":
                if x > p:
                    points.remove((x, y))
                    points.add((2 * p - x, y))
            elif y > p:
                points.remove((x, y))
                points.add((x, 2 * p - y))
        
        if i == 0:
            return len(points)

def part_two(data, points):
    for line in data:
        (*_, dir), p = line.split("=")
        p = int(p)
        for x, y in tuple(points):
            if dir == "x":
                if x > p:
                    points.remove((x, y))
                    points.add((2 * p - x, y))
            elif y > p:
                points.remove((x, y))
                points.add((x, 2 * p - y))
        
    x_max = max(x for x, _ in points)
    y_max = max(y for _, y in points)

    answer = []
    for y in range(y_max + 1):
        for x in range(x_max + 1):
            if (x, y) in points:
                answer.append("#")
            else:
                answer.append(" ")
        answer.append("\n")
    return "".join(answer)
                
if __name__ == "__main__":
    with open("day_13/input.txt") as f:
        points = set()
        data = iter(f.read().splitlines())
        for line in data:
            if not line:
                break
            points.add(tuple(map(int, line.split(","))))

    print(part_one(data, points))
    print(part_two(data, points))