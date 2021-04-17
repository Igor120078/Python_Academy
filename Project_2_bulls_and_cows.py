import random
import time
import json
import os

# BULLS AND COWS GAME

STATISTICS = 'statistics.json'
SEP = '-' * 60


# Hlavni funkce, která řídí hru
def main():
    player_name = get_player_name()
    greet(player_name)
    secret_num = make_secret_num()
    tries = 0
    start = time.time()
    game = True
    while game:
        guess = make_a_guess()
        tries += 1
        bulls, cows = check_guess(guess, secret_num)
        if bulls == 4:
            delta = round((time.time() - start))
            print(f"Correct! You've guessed the right number in {tries} guesses!")
            print(f"Your guessing time: {delta // 60}min {delta % 60}sec")
            print(SEP)
            check_result(player_name, delta)
            print(SEP)
            play_again()
        show_result(bulls, cows)


# Funkce vytiskne pozdrav a úvodní zprávu pro hráče
def greet(player_name):
    print(f'Hi {player_name}!')
    print(SEP)
    print('''I've generated a random 4 digit number for you. 
Let's play a bulls and cows game.''')
    print(SEP)


# Funkce požádá hráče o jméno
def get_player_name():
    return input("To start the game enter your name: ")


# Funkce vytvoří tajné číslo
def make_secret_num():
    secret_num = random.sample(range(1, 10), 4)
    return secret_num


# Funkce umožní hráči tipnout číslo, zkontroluje správnost zadání
# a umožní také opustit hru
def make_a_guess():
    guessing = True
    while guessing:
        guess_inp = input("Enter a number ('q' for exit): ")
        if guess_inp.lower() == 'q':
            print("See you next time!")
            exit()
        elif len(set(guess_inp)) != 4 or not guess_inp.isdigit() or guess_inp[0] == '0':
            print("You must enter a four-digit number that doesn't start with '0'!")
            print(SEP)
            continue
        else:
            guess = [int(n) for n in guess_inp]
            guessing = False
    return guess


# Funkce vyhodnotí tipnuté číslo a vrátí počet uhodnutých čísel celkem a pozičně
def check_guess(guess, secret_num):
    bulls = 0
    cows = 0
    for i, num in enumerate(guess):
        if num in secret_num:
            if secret_num[i] == num:
                bulls += 1
            else:
                cows += 1
    return bulls, cows


# Funkce vytiskne výsledek vyhodnocení tipu
def show_result(bulls, cows):
    if bulls == 1:
        text_bull = 'bull'
    else:
        text_bull = 'bulls'
    if cows == 1:
        text_cow = 'cow'
    else:
        text_cow = 'cows'

    print(f"{bulls} {text_bull}, {cows} {text_cow}")
    print(SEP)


# Funkce nabídne zahrát hru ještě jednou
def play_again():
    while True:
        pl_again = input("Do you want to play again? (Y/N)")
        pl_again_clear = pl_again.upper().strip()
        if pl_again_clear not in ('Y', 'N'):
            print("Please enter Y or N to confirm you want to play again ")
            continue
        elif pl_again_clear == 'Y':
            break
        else:
            print("See you next time!")
            exit()
    main()


# Funkce srovná výsledek hry hráče s jeho nejlepším dosažením
def check_result(player_name, delta):
    stat_data, delta_prev = get_statistics(STATISTICS, player_name)
    if delta_prev == 0:
        print(f"Dear {player_name}, your first game result was saved.")
        write_result(player_name, stat_data, delta)
    elif delta_prev <= delta:
        print(f"Dear {player_name}, your best result was {delta_prev//60 }min {delta_prev%60}sec, try again.")
    else:
        print(f"Dear {player_name}, you've just improved your achievement in this game!")
        write_result(player_name, stat_data, delta)


# Funkce získá nejlepší výsledek hry pro daného hráče
def get_statistics(statistics, player_name):
    if statistics in os.listdir():
        with open(statistics) as f:
            stat_data = json.load(f)
            delta_prev = stat_data.get(player_name, 0)
    else:
        stat_data = {}
        delta_prev = 0
    return stat_data, delta_prev


# Funkce zapíše výsledek hry do souboru s výsledky
def write_result(player_name, stat_data, delta):
    stat_data[player_name] = delta
    with open(STATISTICS, 'w') as f:
        json.dump(stat_data, f, indent=4)


main()
