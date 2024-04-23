#Word Guessing Game Consolidation Project

import random
player = "variable"
self = "player one"
self_confidential_word = "math"
self_guessed_letters = "h, i, m, s, "


class BassWordGuessingGame:
    words_bank= ["english", "mathematics", "science", "social studies", "physical education"]
    self_words_bank = words_bank
    self_confidential_word = random.choice(words_bank).lower()
    self_guessed_letters = []
    self_letter_guesses = 0
    self_word_guesses = 0 

    def __init__(): 
        self_words_bank = words_bank
        self_confidential_word = random.choice(words_bank).lower()
        self_guessed_letters = []
        self_letter_guesses = 0
        self_word_guesses = 0 
    
    def show_word_state():
        show_word = input("Guess the letter please:") 
        for letter in self_confidential_word:
            if letter.lower() in self_guessed_letters:
               display_word = letter
            else:
                show_word
            return show_word
    show_word_state()
    
    def play(self):
        print("Welcome to Bass Word Guessing Game.")
        input("The confidential word has {} letters".format(len(self.secret_word)))
        while True: 
            print("\nWord:" , self.show_word_state)
        guess = input("Guess a letter or the whole word: "). lower()
        if guess in self.guessed_letters:
         print("You already guessed that letter.")
        show_word_state()
    
    
        
        if len(guess): BassWordGuessingGame
        self_guessed_letters.append(guess)
        self.letter_guesses = 1
        repeated = self.confidential_word.count(guess)
        if repeated > 0:
            print("There are {} repeated of '{}' in the word.". format(repeated, guess))
        else:
            print("Sorry, '{}' is not in the word.". format(guess))

        if "" not in  self.display_word_state():
            print("\n Great Job! You guessed the word '{}' in {} letter guesses!")
            format(self.secret_word, self.letter_guesses)
        
        #Guessing the whole word
        self.word_guesses = 1
        if guess == self.secret_word:
            print("\n Great Job! You guessed the word '{}' correctly in {} guesses!")
            format(self.confidential_word, self.letter_guesses + 1)

        else:
            print("Incorrect, that is not the correct word.")
        if self_word_guesses == 3:
            print("\You have used all your word guesses. The confidential word '{}'.")
            (format(self.secret_word))
    play(player)
words_bank= ["english", "mathematics", "science", "social studies", "physical education"]
game = BassWordGuessingGame
game.play()


            
                  
    


            


                                                            


