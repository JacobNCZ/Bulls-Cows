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
final_number = None


# Funkce na vygenerování 4-místného čísla.
def number_generator():
    first_number = random.randint(1, 9)
    rest_numbers = list(range(10))
    rest_numbers.remove(first_number)
    last_three = (random.sample(rest_numbers, 3))
    last_three.insert(0, first_number)
    number = ''.join(map(str, last_three))
    return number


# Funkce kontroly duplicity vložených číslic.
def duplicity_check(number):
    return bool(len(list(number)) != len(set(number)))


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
    if guess_counter == 0:
        # Spouštění funkce na vygenerování 4-místného čísla.
        final_number = number_generator()
        print(final_number)

        # Měření času
        start = time.time()

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
        if duplicity_check(player_guess):
            print("There cannot be duplicity numeric characters!")
            wrong_input = True

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

        for pozice in range(0, 4):
            if player_guess[pozice] == final_number[pozice]:
                bull_counter += 1
            elif player_guess[pozice] in final_number:
                cow_counter += 1

        # Počítadlo tipů.
        guess_counter += 1
        guess = grammar(guess_counter, "guess", "guesses")

        # Slovní ohodnocení hry.
        if player_guess == final_number:
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
