# Úvodní hlavička.
"""
projekt_2a.py: druhý projekt (zadání 1) do Engeto Online Python Akademie

author: Jakub Nárožný
email: narozny.jakub@gmail.com
discord: Jakub N.
"""

# Import z knihoven.
import random
import time
from datetime import timedelta

# Pomocné proměnné.
lets_continue = None
guess_counter = 0
start = None
game_statistics = []
game_counter = 0
number = None


# Funkce pro správnou gramatiku při vyhodnocení.
def grammar(counter, singular, plural):
    if counter == 1:
        return singular
    else:
        return plural


# Pozdrav uživatele a vypsání úvodního textu.
print('''Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------''')

while lets_continue != "no":
    # Vygenerování 4 místného čísla.
    if guess_counter == 0:
        start = time.time()
        number = str(random.randint(1, 9))
        while len(number) != 4:
            next_char = str(random.randint(0, 9))
            if (next_char in number) is False:
                number += next_char

# Kontrola vstupních dat dle zadaných parametrů.
    wrong_input = False

    # Hráčův tip
    player_guess = input(">>>")

    #  Kontrola typu vložených znaků.
    if player_guess.isnumeric() is False:
        print("Your guess must contain only numeric characters!")
        wrong_input = True

    # Kontrola duplicity vložených číslic.
    if len(player_guess) == 4:
        index_i = -1
        for i in player_guess:
            index_i += 1
            index_y = -1
            for y in player_guess:
                index_y += 1
                if i == y and index_i != index_y and (47 < ord(y) < 57):
                    print("There cannot be duplicity numeric characters!")
                    wrong_input = True
                    break
                else:
                    continue
            else:
                continue
            break

        # Kontrola splnění podmínky začátku čísla - nesmí obsahovat nulu.
        if player_guess[0] == "0":
            print("You cannot start with zero!")

    # Kontrola délky vloženého čísla.
    if len(player_guess) > 4:
        print("Your guess number is too long! It must have 4 characters only.")
        wrong_input = True
    elif len(player_guess) < 4:
        print("Your guess number is too short! It must have 4 characters.")
        wrong_input = True

    if wrong_input is False:
        # Součet Bulls/Cows.
        bull_counter = 0
        cow_counter = 0

        for _ in range(0, 4):
            if player_guess[_] == number[_]:
                bull_counter += 1
            elif player_guess[_] in number:
                cow_counter += 1

        # Počítadlo tipů.
        guess_counter += 1
        guess = grammar(guess_counter, "guess", "guesses")

        # Slovní ohodnocení hry.
        if player_guess == number:
            if guess_counter <= 10:
                result = "perfect"
            elif guess_counter > 10:
                result = "average"
            else:
                result = "not so good"

            print(f"Correct, you've guessed the right number\nin {guess_counter} guesses!\n"
                  f"-----------------------------------------------\n"
                  f"That's {result}")

            # Statistika počtu odhadů jednotlivých her.
            end = time.time()
            total_time = timedelta(seconds=round(end-start))

            game_counter += 1
            game_statistics.append(
                f"Game number: {game_counter}\tScore: {guess_counter}\tTotal time: {total_time}.")
            print(*game_statistics, sep="\n")

            # Výběr možnosti ukončení hry.
            lets_continue = input("Would you like to play again? yes/no ").lower()
            while lets_continue != "yes" and lets_continue != "no":
                lets_continue = input(
                    "\nWrong input! Please, repeat your choice.\nWould you like to play again? yes/no ")

            guess_counter = 0

        else:
            # Vyhodnocení jednotlivých tipů hráče.
            bull = grammar(bull_counter, "bull", "bulls")
            cow = grammar(cow_counter, "cow", "cows")
            print(f"{bull_counter} {bull}, {cow_counter} {cow}")
            print(f"Your score is: {guess_counter} {guess}")
