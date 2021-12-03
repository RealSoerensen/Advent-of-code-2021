file = open("day_1/input.txt", "r")

def main(file):
    numbers = file.readlines()
    num = 150
    increased = 0
    for number in numbers:
        if int(number) > int(num):
            increased += 1
        num = number

    return increased

if __name__ == "__main__":
    print(main(file), "measurements were larger than the previous measurement")