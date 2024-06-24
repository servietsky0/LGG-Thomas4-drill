import random
import re

class Hangman:
    def __init__(self) -> None:
        self.possible_words : list [str] = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find : list [str] = list(random.choice(self.possible_words))
        self.correctly_guessed_letters : list [str] =  ['_' for i in range(len(self.word_to_find))]
        self.wrongly_guessed_letters : list [str] = []
        self.error_count : int = 0
        self.turn_count : int = 0
        self.lives : int = 5
        self.pattern : str = r'[a-z]{1}'

    # str methode
    
    
    def play(self):
        while True:               
            letter : str = input("enter a letter: ").lower()
                    
            if not re.match(self.pattern, letter):
                print('are u dumb or whoot')
                continue

            elif letter in self.word_to_find:
                for i in range(len(self.word_to_find)):
                    if letter == self.word_to_find[i]:
                        self.correctly_guessed_letters[i] = letter
                break
            
            elif letter in self.wrongly_guessed_letters or letter in self.correctly_guessed_letters:
                print('letter already given')
                continue

            else:
                self.wrongly_guessed_letters.append(letter)
                self.error_count += 1
                self.lives -= 1 # vous etes au courant que ca sert a rien?
                break

    def start_game(self):
        while True:   
            self.turn_count += 1

            print(f'error count : {self.error_count} - turn count : {self.turn_count} - lives left : {self.lives}')
            print(f'correct word : {self.correctly_guessed_letters}')
            print(f'bad guess letter : {self.wrongly_guessed_letters}')
            self.play()
            
            if self.lives == 0:
                self.game_over()
                break
            elif self.correctly_guessed_letters == self.word_to_find:
                self.well_played()
                break
            

    def game_over(self):
        print('chhheeeeeeeeeee, you lost')

    def well_played(self):
        print(f'You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!')


            
                



