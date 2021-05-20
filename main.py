

class Hangman:
    possible_words = ['becode', 'learning', 'mathematics', 'sessions']
    word_to_find = []
    lives = 5
    #contains a list of strings
    #To be CORRECTED
    correctly_guessed_letters = ['_'*4]
    wrongly_guessed_letters = []
    turn_count = 0
    error_count = 0
    def play(self):
        bool = 0

        letter = input('Enter a letter please')
        #Here is how i verified if it is a letter or not (using isalpha.. It helps to know if the characters are alphabet letters)
        #and Also if there only one Character by using the lenght of the word
        while(bool == 0):

            while len(letter) !=1:
                letter = input('Only one letter Please')

            if not letter.isalpha():
                letter = input('Please enter a letter')
            else:
                print('it is a letter')
                bool = 1
        print(letter)

        for x in self.word_to_find()



Hangman.play()