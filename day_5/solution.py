file = "day_5/input.txt"

def parse(input):
    for start, stop in [line.split(" -> ") for line in input.splitlines()]:
        x, y = map(int, start.split(','))
        x1, y1 = map(int, stop.split(','))
    return x, x1, y, y1

def part_one(file):
    with open(file, 'r') as f:
        coords_dict = {}
        for j in f:
            x1, x2, y1, y2 = parse(j)

            # Horizontal line
            if y1 == y2:  # Horizontal line
                for i in range(min(x1, x2), max(x1, x2)+1):
                    coords_dict[(y1, i)] = coords_dict.get((y1, i), 0) + 1
            
            # Vertical line
            if x1 == x2:
                for i in range(min(y1, y2), max(y1, y2)+1):
                    coords_dict[(i, x1)] = coords_dict.get((i, x1), 0) + 1
        
        overlap_count = 0
        for j in coords_dict.items():
            if j[1] >= 2:
                overlap_count += 1
        return overlap_count

def part_two(file):
    with open(file, 'r') as f:
        coords_dict = {}
        for j in f:
            x1, x2, y1, y2 = parse(j)

            # Horizontal line
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2)+1):
                    coords_dict[(y, x1)] = coords_dict.get((y, x1), 0) + 1
            
            # Vertical line
            if y1 == y2:
                for x in range(min(x1, x2), max(x1, x2)+1):
                    coords_dict[(y1, x)] = coords_dict.get((y1, x), 0) + 1

            # Diagonal lines
            if not (x1 == x2 or y1 == y2):
                dx = x2 - x1
                dy = y2 - y1
                coords_dict[(y1, x1)] = coords_dict.get((y1, x1), 0) + 1

                while not x1 == x2:
                    x1 = x1 + (dx // abs(dx))
                    y1 = y1 + (dy // abs(dy))
                    coords_dict[(y1, x1)] = coords_dict.get((y1, x1), 0) + 1

        overlap_count = 0
        for i in coords_dict.items():
            if i[1] >= 2:
                overlap_count += 1
        return overlap_count

if __name__ == "__main__":
    print(part_one(file))
    print(part_two(file))