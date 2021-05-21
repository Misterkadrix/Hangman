import random


class Hangman:
    possible_words = ['becode', 'learning', 'mathematics', 'sessions']
    word_to_find = []
    correctly_guessed_letters = []
    wrongly_guessed_letters = []

    # Here i make a random choice of my list possible_words..
    # Then i take each character of the random word and i append it on the word_to_find.
    n = random.choice(possible_words)
    for x in n:
        word_to_find.append(x)
        correctly_guessed_letters.append("_")
    # End of my Loop
    print(word_to_find)
    print(correctly_guessed_letters)
    lives = 5
    # contains a list of strings
    # To be CORRECTED
    turn_count = 0
    error_count = 0

    def play():

        while Hangman.correctly_guessed_letters != Hangman.word_to_find and Hangman.lives > 0:
            bool = 0

            letter = input('Enter a letter please')
            # Here is how i verified if it is a letter or not (using isalpha.. It helps to know if the characters are alphabet letters)
            # and Also if there only one Character by using the lenght of the word
            while (bool == 0):

                while len(letter) != 1:
                    letter = input('Only one letter Please')

                if not letter.isalpha():
                    letter = input('Please enter a letter')
                else:
                    bool = 1

            # I create a variable -> findletter and i used it like a boolean to know if i find the letter with my loop
            findletter = 0
            for x in Hangman.word_to_find:
                if x == letter:
                    findletter = 1
                    break
            # I use a condition to know if i have find the letter then i loop on the word_to_find to know the index of the letter
            # and then i repalce the empty space with the letter find
            count = 0
            if findletter == 1:
                for x in Hangman.word_to_find:
                    if x == letter:
                        Hangman.correctly_guessed_letters[count] = x

                    count += 1
            else:
                Hangman.wrongly_guessed_letters.append(letter)
                Hangman.error_count += 1
                Hangman.lives -= 1

            print(Hangman.correctly_guessed_letters)
            print("Error letters : " + str(Hangman.wrongly_guessed_letters))
            print("Error Count " + str(Hangman.error_count))
            print("Remaining " + str(Hangman.lives))

    def game_over():
        print("game over")

    def well_played():
        print(f'You found the word: {Hangman.n} in {Hangman.turn_count} turn with {Hangman.error_count} errors')

    def start_game():

        Hangman.play()
        if Hangman.lives == 0:
            Hangman.game_over()
        else:
            Hangman.well_played()


