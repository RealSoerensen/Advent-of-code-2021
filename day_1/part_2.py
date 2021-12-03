file = open("day_1/input.txt", "r")

def main(file):
    numbers = file.readlines()
    num = 457
    increased = 0
    for i, number in enumerate(numbers):
        try:
            sum_numbers = sum([int(number),  int(numbers[i + 1]), int(numbers[i + 2])])
            
            if sum_numbers > num:
                increased += 1
                
            num = sum_numbers

        except IndexError:
            break

    return increased

if __name__ == "__main__":
    print(main(file), "measurements were larger than the previous measurement")