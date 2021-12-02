with open("nums.txt", "r") as f:
    numbers = f.readlines()
    num = 457
    increased = 0
    for i, number in enumerate(numbers):
        number = int(number)
        try:
            sum_numbers = number + int(numbers[i + 1]) + int(numbers[i + 2])
            
            if int(sum_numbers) > int(num):
                print(str(sum_numbers) + "(increased)")
                increased += 1
                
            elif int(sum_numbers) == int(num):
                print(str(sum_numbers) + "(no change)")

            else:
                print(str(sum_numbers) + "(decreased)")

            num = sum_numbers
        except IndexError:
            print("End of list")
            break

    print("Number of increased numbers: " + str(increased))