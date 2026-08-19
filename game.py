import random
while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            continue
        else:
#Generating a value between 1 and the input
            rand_int = random.randint(1,level)
            while True:
                try:
                    guess = int(input("Guess: "))
                    won = False
                    if guess < 1:
                        continue
                    else:
                        if guess < rand_int:
                            print("Too small!")
                            continue
                        elif guess > rand_int:
                            print("Too large!")
                            continue
                        else:
                            print("Just right!")
                            won = True
                            break
                except ValueError:
                    continue
            if won:
                break
    except ValueError:
        continue
