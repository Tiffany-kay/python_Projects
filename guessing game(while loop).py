# Guessing game using while loop
import random

games_played = 0
# limit player to play five times
while games_played < 5:
    try:
        win_num = random.randint(1, 100)
        num = int(input("let's test your guessing skills🤔....You have to guess a number bruh: "))
    except ValueError:

        print("Be serious😤😤😤😤")
        continue

    if num == win_num:
        print("Damn you are good😎")
    elif num < win_num:
        print("Too low😪😪😪🥱... try harder bruh")
    else:
        print("Lower your ambitions.. Too high😛😛😛")

    games_played += 1

print("You've played five times. Hope you had fun!")
