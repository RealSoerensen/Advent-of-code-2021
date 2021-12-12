from collections import defaultdict, deque

def searching(skip_duplicates):
    count = 0
    # Search until we have no more children to search
    search = deque((child, set(), False) for child in caves["start"])
    while search:
        # Pop parent, lowers and duplicate to the left and search it
        parent, lowers, duplicate = search.popleft()

        # If the parent is == the end, we found a path
        if parent == "end":
            count += 1
            continue
        # If the parent is already in the lowers, we have a duplicate
        elif parent.islower():
            if parent in lowers:
                if skip_duplicates or duplicate:
                    continue
                else:
                    duplicate = True
            lowers.add(parent)

        # Add children to the search queue
        search.extend((child, set(lowers), duplicate) for child in caves[parent] if child != "start")
    return count

def part_one():
    for skip_duplicates in True, False:
        count = 0
        count += searching(skip_duplicates)
        return count

def part_two():
    for skip_duplicates in True, False:
        count = 0 
        count += searching(skip_duplicates)
    return count


if __name__ == "__main__":
    with open('day_12/input.txt') as f:
        caves = defaultdict(list)
        for line in f:
            a, b = line.strip().split("-")
            caves[a].append(b)
            caves[b].append(a)
    print(part_one())
    print(part_two())
