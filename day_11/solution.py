def main(data):
    flashes = 0
    stack = []
    # Create 10x10 grid
    for x in range(len(data)):
        for y in range(len(data[x])):
            data[x][y] += 1
            # If coord is over 9, add 1 to flash, reset to 0 and add to stack
            if data[x][y] > 9:
                flashes += 1
                data[x][y] = 0
                stack.append((x,y))
    # Loop through stack
    while stack:
        # Pop coord from stack assign to x and y
        x, y = stack.pop()
        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 10 and 0 <= ny < 10 and data[nx][ny] > 0:
                data[nx][ny] += 1
                # if data[nx][ny] is greater than 9, add 1 to flash, reset to 0 and add to stack
                if data[nx][ny] > 9:
                    flashes += 1
                    data[nx][ny] = 0
                    stack.append((nx, ny))
    return flashes

def part_one(data):
    flashes = 0
    # Iterate 100 times
    for _ in range(100):
        # Add amount of flashes to total flashes
        flashes += main(data)
    return flashes

def part_two(data):
    steps = 0
    # FOr each iteration add 1 step to steps
    while sum(map(sum, data)) > 0:
        main(data)
        steps += 1
    return steps

if __name__ == '__main__':
    with open('day_11/input.txt', 'r') as f:
        file = f.read().splitlines()
        # For row in the file, convert to a map of int and row and then into a list
        data = [list(map(int, row)) for row in file]

    print(part_one([row[:] for row in data]))
    print(part_two([row[:] for row in data]))