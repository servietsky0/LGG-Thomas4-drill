import streamlit as st
from streamlit_extras.let_it_rain import rain
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


    def play(self):
        unique_value = 0
        l = st.text_input('fhfhfh')
        while True:               
            letter : str = input("enter a letter: ", key=unique_value).lower()
                    
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
                self.lives -= 1 
                break

    def start_game(self):
        st.set_page_config(
        page_title="Hangman",
        page_icon="knot",
    )
    
        languages = {"en": "English", "fr": "French"}

        language = st.sidebar.selectbox(
            "🌍 Language",
            list(languages.keys()),
            format_func=lambda lang: languages[lang],
        )

        source_link = {
            "en": "Show link to source code repository",
            "fr": "montrer le lien du repository",
        }

        repo_url = "https://github.com/servietsky0/LGG-Thomas4-drill/tree/main/projects/hangman"

        info_hosting = {
            "en": f"Host your own Hangman interface using <{repo_url}>",
            "fr": f"Hébergez votre propre interface Hangman en utilisant <{repo_url}>",
        }

        if st.sidebar.checkbox(source_link[language]):
            st.info(info_hosting[language])

        title_lang = {"en": "Hangman Game 🎯", "fr": "Jeu du pendu 🎯"}

        st.title(title_lang[language])

        instruction = {
            "en": (
                "1. Clic on the button new game.\n"
                "2. Make your first a guess .\n"
                "3. Enjoy my game!"
            ),
            "fr": (
                "1. cliquez sur le bouton new game.\n"
                "2. N'oubliez pas de masquer la barre latérale avant de jouer.\n"
                "3. Amusez vous bien!"
            ),
        }

        st.write(instruction[language])

        if st.button("new game"):
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
        st.subheader('U losseee !!!')
        rain(emoji='💀', font_size=54, falling_speed=10, animation_length='infinite')



    def well_played(self):
        print(f'You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!')
        st.subheader(f'You won with only {self.error_count} error (s)')
        st.balloons()
        with st.expander("GET YOUR GIFT"):
            st.image("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.F3bkgjbhmNNDPbwbDxAwKAAAAA%26pid%3DApi&f=1&ipt=1a57a25d2e9428e95a23d61f9a9424fc9231b4ca1961d2444bad565c3e3c2678&ipo=images")    
                



