with open("nums.txt", "r") as f:
    numbers = f.readlines()
    num = 150
    increased = 0
    for number in numbers:
        if int(number) > int(num):
            print(str(number) + "(increased)")
            increased += 1
        elif int(number) == int(num):
            print(str(number) + "(same)")
        else:
            print(str(number) + "(decreased)")
        num = number


    print("Number of increased numbers: " + str(increased))