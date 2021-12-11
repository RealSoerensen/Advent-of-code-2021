from collections import Counter
from typing import Counter as typedCounter

def get_lowest_points(data):
    # Make a list for potiential points
    potential = []

    # Iterate over the data
    for i, row in enumerate(data):
        # Iterate over the row
        positions = sorted(range(len(row)), key=lambda x: row[x])
        reserved = []
        # Iterate over the positions
        for pos in positions:
            # If pos + 1 or pos - 1 is in the reserved list, skip
            if pos + 1 in reserved or pos - 1 in reserved:
                continue
            
            # If the current position - 1 is 0 or higher, and the current position - 1 is higher than the current position, set as True otherwise set as False
            cond1 = row[pos - 1] > row[pos] if pos - 1 >= 0 else True
            # If the current position + 1 is smaller than the lenght of row, 
            # and the current position + 1 is higher than the current position, 
            # set as True otherwise set as False
            cond2 = row[pos + 1] > row[pos] if pos + 1 < len(row) else True

            # If both conditions are True, add the current position to the potential list and reserved list
            if cond1 and cond2:
                reserved.append(pos)
                potential.append((i, pos))

    coords = []
    # Iterate over the potential list
    for x, y in potential:
        value = data[x][y]
        # If the x value is 0 or higher, 
        # and the value of data[x][y] is lower than the value of data[x - 1][y], 
        # set as True otherwise set as False
        cond1 = data[x-1][y] > value if x - 1 >= 0 else True
        # If the x value is smaller than the lenght of data,
        # and the value of data[x][y] is lower than the value of data[x + 1][y],
        # set as True otherwise set as False
        cond2 = data[x+1][y] > value if x + 1 < len(data) else True
        # If both conditions are True, add the current position to the coords list
        if cond1 and cond2:
            coords.append((x, y))

    return coords


def part_one(data):
    total = 0
    # Iterate received from x and y in function get_lowest_points
    for x, y in get_lowest_points(data):
        # Add the value of the current position to the total
        total += data[x][y] + 1
    return total


def part_two(data):
    # Get lenght of data's first index
    row_size = len(data[0])
    # Get lenght of data
    col_size = len(data)

    def fill(x, y, value):
        # If either x is smaller than 0 or x is equal or higher than col_size, return
        if x < 0 or x >= col_size:
            return

        # If either y is smaller than 0 or y is equal or higher than row_size, return
        if y < 0 or y >= row_size:
            return

        # If data[x][y] is equal value, 9 or lower than 0, return
        if data[x][y] == value or data[x][y] == 9 or data[x][y] < 0:
            return

        # Set value to data[x][y]
        data[x][y] = value
        
        fill(x-1, y, value)
        fill(x+1, y, value)
        fill(x, y-1, value)
        fill(x, y+1, value)

    coords = get_lowest_points(data)
    # Iterate over the coords list
    for i, (x, y) in enumerate(coords):
        fill(x, y, (i + 1) * -1)

    c: typedCounter[int] = Counter()
    # Iterate over the data
    for row in data:
        # Update the counter with the values of the current row
        c.update(row)

    del c[9]
    total = 1
    # Iterate over mosat common in c
    for _, s in c.most_common(3):
        # Time the total by the value of s
        total *= s

    return total


if __name__ == "__main__":
    with open("day_9/input.txt") as file:
        data = file.readlines()
        matrix = []
        # Iterate over the lines in data
        for row in data:
            line = []
            # Iterate over each item in the row
            for item in row.strip():
                line.append(int(item))
            # Add the row to the matrix
            matrix.append(line)

    print(part_one(matrix))
    print(part_two(matrix))