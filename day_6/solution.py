import time
start_time = time.perf_counter ()

file = "day_6/input.txt"

def make_age_map(lanternfish):
	fish_age = {key: 0 for key in range(0, 9)}
	for age in lanternfish:
		fish_age[age] += 1
	return fish_age

def calculate_population(fish_list, days):
	fish_age = make_age_map(fish_list)
	for day in range(0, days):
		new_fish = fish_age[0]
		fish_age = {key - 1: value for (key, value) in fish_age.items() if key > 0}
		fish_age[6] += new_fish
		fish_age[8] = new_fish
	return sum(fish_age.values())

def part_one(data):
    return calculate_population(data, 80)


def part_two(data):
    return calculate_population(data, 256)


if __name__ == "__main__":
    input = list(open(file).readlines())
    data = [int(age) for age in input.split(',')]
    print(part_one(data))
    print(part_two(data))
    end_time = time.perf_counter ()
    print(end_time - start_time, "seconds")