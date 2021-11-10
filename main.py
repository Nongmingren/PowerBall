import random

print("What modes would you like to play in. [Real mode or Fixed win]")


while True:
    game_mode = input("> ")
    if game_mode.lower() == "real mode":
        print("""Powerball Lottery, by Al Sweigart al@inventwithpython.com
    
        Each powerball lottery ticket costs $2. The jackpot for this game
        is $1.586 billion! It doesn't matter what the jackpot is, though,
        because the odds are 1 in 292,201,338, so you won't win.
    
        This simulation gives you the thrill of playing without wasting money.""")

        # r1answer = True

        # while r1answer == True:
        # response1 = input("> ")
        # r1 = str(response1)
        # r1length = len(r1)
        # r1length = r1answer

        while True:
            print("Enter 5 different numbers from 1 to 69, with spaces between each numbers. (for example: 5 17 23 42 50)")
            response = input("> ")

            numbers = response.split()
            if len(numbers) != 5:
                print("Please enter 5 numbers, seperated by spaces")
                continue

            try:
                for i in range(5):
                    numbers[i] = int(numbers[i])
            except ValueError:
                print("Enter numbers like 56, 1, or 42")
                continue

            larges_number = False
            for i in range(5):
                if not (1 <= numbers[i] <= 69):
                    print("The number must be between 1 and 69")
                    larges_number = True
            if larges_number:
                continue

            if len(set(numbers)) != 5:
                print("Please enter 5 different numbers.")
                continue

            break

        while True:
            print("Enter the powerball number from 1 to 26.")
            response = input("> ")

            try:
                powerball = int(response)
            except ValueError:
                print("Please enter the powerball, like 2, 26, 9")
                continue

            if not (1 <= powerball <= 26):
                print("The number must be between 1 and 26")
                continue

            break

        while True:
            print("How many times do you want to play? Max: 1000000.")
            response = input("> ")

            try:
                num_plays = int(response)
            except ValueError:
                print("Please enter the powerball, like 2, 26, or 2000")
                continue

            if not (1 <= num_plays <= 10000000):
                print("The number must be between 1 and 1000000")
                continue

            break

        price = "S" + str(2 * num_plays)
        print(f"The costs is {price} to play {num_plays} times, but don't worry. Im sure you'll win it all back")
        input("Press enter to start")

        possible_number = list(range(1, 70))
        for i in range(num_plays):
            random.shuffle(possible_number)
            winning_number = possible_number[:5]
            winning_powerball = random.randint(1, 26)
            print(f"The winning numbers are: {winning_number} and winning powerball: {winning_powerball}")

            if numbers == winning_number and powerball == winning_powerball:
                print("you have won the Powerball Lottery! Congratulations")
                print("you would be a billionaire if this was real")
                break
            else:
                print("you lost haha")
                break
    elif game_mode.lower() == "fixed win":

        print("how many times are you going to play")
        response = input("> ")
        num_plays = int(response)

        possible_number = list(range(1, 70))
        for i in range(num_plays):
            random.shuffle(possible_number)
            winning_number = possible_number[:5]
            winning_powerball = random.randint(1, 26)
            print(f"The winning numbers are: {winning_number} and winning powerball: {winning_powerball}")

            print("""Powerball Lottery, by Al Sweigart al@inventwithpython.com
    
            Each powerball lottery ticket costs $2. The jackpot for this game
            is $1.586 billion! It doesn't matter what the jackpot is, though,
            because the odds are 1 in 292,201,338, so you won't win.
    
            This simulation gives you the thrill of playing without wasting money.""")

            while True:
                print(
                    "Enter 5 different numbers from 1 to 69, with spaces between each numbers. (for example: 5 17 23 42 50)")
                response = input("> ")

                numbers = response.split()
                if len(numbers) != 5:
                    print("Please enter 5 numbers, seperated by spaces")
                    continue

                try:
                    for i in range(5):
                        numbers[i] = int(numbers[i])
                except ValueError:
                    print("Enter numbers like 56, 1, or 42")
                    continue

                larges_number = False
                for i in range(5):
                    if not (1 <= numbers[i] <= 69):
                        print("The number must be between 1 and 69")
                        larges_number = True
                if larges_number:
                    continue

                if len(set(numbers)) != 5:
                    print("Please enter 5 different numbers.")
                    continue

                break

            while True:
                print("Enter the powerball number from 1 to 26.")
                response = input("> ")

                try:
                    powerball = int(response)
                except ValueError:
                    print("Please enter the powerball, like 2, 26, 9")
                    continue

                if not (1 <= powerball <= 26):
                    print("The number must be between 1 and 26")
                    continue

                break

            while True:
                print("How many times do you want to play? Max: 1000000.")
                response = input("> ")

                try:
                    num_plays = int(response)
                except ValueError:
                    print("Please enter the powerball, like 2, 26, or 2000")
                    continue

                if not (1 <= num_plays <= 10000000):
                    print("The number must be between 1 and 1000000")
                    continue

                print(f"The winning numbers are: {winning_number} and winning powerball: {winning_powerball}")
                if numbers == winning_number and powerball == winning_powerball:
                    print("you have won the Powerball Lottery! Congratulations")
                    print("you would be a billionaire if this was real")
                    break
                else:
                    print("you lost haha")
                    break
    else:
        print("Please type Real mode or Fixed win")
