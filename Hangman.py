
import random

def hangman():
    wordList = ["MANTRA", "SYNTAX", "DIVINE", "MECHANISM", "MACCHIATO", "EXECUTE", "CRESCENT", "CAFFEINE", "NOSTALGIA", "DESTINY", "VIBRATION", "DIVERGENT", "DELUSIONAL", "MELANCHOLY", "DESIRE", "EROTIC", "MOUTHBREATHER", "SELENOPHILE"]
    word = random.choice(wordList)
    turns = 6
    letters = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    letters_attempt = ''
    error_message = ''
    
    while len(word) > 0:
        main_word = ''

        for letter in word:
            if letter in letters_attempt:
                main_word = main_word + letter
            else:
                main_word = main_word + "_"
        
        if main_word == word:
            print(main_word)
            print("\nYay! You guessed it right!")
            print('''
            ─────────▄──────────────▄
            ────────▌▒█───────────▄▀▒▌
            ────────▌▒▒▀▄───────▄▀▒▒▒▐
            ───────▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐
            ─────▄▄▀▒▒▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐
            ───▄▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀██▀▒▌wow
            ──▐▒▒▒▄▄▄▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄▒▒▌
            ──▌▒▒▐▄█▀▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐
            ─▐▒▒▒▒▒▒▒▒▒▒▒▌██▀▒▒▒▒▒▒▒▒▀▄▌amaze
            ─▌▒▀▄██▄▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▌ balls
            ─▌▀▐▄█▄█▌▄▒▀▒▒▒▒▒▒░░░░░░▒▒▒▐ 
            ▐▒▀▐▀▐▀▒▒▄▄▒▄▒▒▒▒▒░░░░░░▒▒▒▒▌
            ▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒░░░░░░▒▒▒▐ such 
            ─▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒▒▒░░░░▒▒▒▒▌wordsmith
            ─▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐
            ──▀▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▒▒▒▒▌
            ────▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀ very
            ───▐▀▒▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀ impressed
            ──▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▀
            ''')
            break

        if error_message != "":
            print("\n"+error_message)
            error_message = ""

        print("\nGuess the word.\n", main_word)
        guess = input("\n▶ ▶    ")
        guess = guess.upper()

        if guess in letters:
            letters_attempt = letters_attempt + guess
        else:
            error_message = "Please input one letter at a time."
            continue
                
        if guess not in word:
            turns = turns - 1
            error_message = "INCORRECT GUESS"

            if turns == 6:
                print('''
                 _____________
                |____________|_
                ||          || | 
                ||          || *
                ||          ||     
                ||          ||        
                ||          || 
                ||          ||      
                ||          ||       
                ||          ||       
                ||          ||      
                ||          ||    
                ||          ||  
                ||          || 
                ||          ||     
                ||          ||     
                ||          ||     
                ||          ||      
                 ----------------     
                /________________\------------\ 
                |                  |-----------|
                | ░█░█░█▀█░█▀█░█▀▀░█▄█░█▀█░█▀█ |
                | ░█▀█░█▀█░█░█░█░█░█░█░█▀█░█░█ |
                | ░▀░▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀░▀░▀░▀ |                           
                |______________________________|
                --------------------------------
                     LIVES LEFT  ♥ ♥ ♥ ♥ ♥ ♥ 
                --------------------------------            
                ''')
            if turns == 5:
                print('''
                 _____________
                |____________|_
                ||          || | 
                ||          || | 
                ||          || *    
                ||          ||        
                ||          || 
                ||          ||      
                ||          ||        __
                ||          ||       (..)
                ||          ||      _|  |_
                ||          ||    //  \/  )
                ||          ||   // :    :|
                ||          ||  //  :    :|
                ||          || o/   :====:O
                ||          ||      (    )
                ||          ||      | `' |
                ||          ||      | || |
                ||          ||      | || |
                ||          ||      |_||_|
                -------------------  '_'`_`
                /__________________\----------\.
                |                  |-----------|
                | ░█░█░█▀█░█▀█░█▀▀░█▄█░█▀█░█▀█ |
                | ░█▀█░█▀█░█░█░█░█░█░█░█▀█░█░█ |
                | ░▀░▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀░▀░▀░▀ |                           
                |______________________________|
                --------------------------------
                    LIVES LEFT  ♥ ♥ ♥ ♥ ♥ ♡
                --------------------------------   
                ''')
            if turns == 4:
                print('''   
                 _______________
                 |______________|_
                ||             || |
                ||             || |
                ||             || |
                ||    @@@@     || |
                ||   (. .)     || *    
                ||   \ - /     ||      __
                ||     `'      ||     (..)
                ||             ||    _|  |_
                ||             ||   // \/  )
                ||             ||  //:    :|
                ||             || // :    :|
                ||             ||o/  :====:O
                ||             ||    (    )
                ||             ||    | `' |
                ||             ||    | || |
                ||             ||    | || |
                ||             ||    |_||_|
                ----------------     '_'`_`
                /__________________\----------\ 
                |                  |-----------|
                | ░█░█░█▀█░█▀█░█▀▀░█▄█░█▀█░█▀█ |
                | ░█▀█░█▀█░█░█░█░█░█░█░█▀█░█░█ |
                | ░▀░▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀░▀░▀░▀ |                           
                |______________________________|
                --------------------------------
                    LIVES LEFT  ♥ ♥ ♥ ♥ ♡ ♡
                --------------------------------  
                ''')
            if turns == 3:
                print('''    
                  _______________
                 |______________|_
                ||      |      || | 
                ||             || |
                ||             || |
                ||    @@@@ ?   || |     pft.
                ||   (. .)  ?  || |     
                ||   \ - /_    || |     __
                ||   |'|'|     || *    (..)
                ||   | : |     ||     _|  |_
                ||   |___|     ||    // \/  )
                ||             ||   //:    :|
                ||             ||  // :    :|
                ||             || o/  :====:O
                ||             ||     (    )
                ||             ||     | `' |
                ||             ||     | || |
                ||             ||     | || |
                ||             ||     |_||_|
                -----------------     '_'`_`
                /__________________\----------\ 
                |                  |-----------|
                | ░█░█░█▀█░█▀█░█▀▀░█▄█░█▀█░█▀█ |
                | ░█▀█░█▀█░█░█░█░█░█░█░█▀█░█░█ |
                | ░▀░▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀░▀░▀░▀ |                           
                |______________________________|
                --------------------------------
                    LIVES LEFT  ♥ ♥ ♥ ♡ ♡ ♡
                --------------------------------                
                ''')
            if turns == 2:
                print(''' 
                  _______________
                 |______________|_
                ||      |      || | 
                ||      |      || |  
                ||             || |  
                ||  ¿ @@@@ ?   || | I don't want
                ||   (. .)  ?  || | to do this.
                || ¿ \ o /_    || |    __
                ||  /|' ' |\   || *   (..)
                || / |  : | \  || o  _|  |_
                || \ |____| /  || \ // \/ )
                ||  \(    )/   ||  \/:    :|
                ||             ||  ` :    :|
                ||             ||    :====:O
                ||             ||    (    )
                ||             ||    | `' |
                ||             ||    | || |
                ||             ||    | || |
                ||             ||    |_||_|
                ----------------     '_'`_`
                /__________________\----------\  
                |                  |-----------|
                | ░█░█░█▀█░█▀█░█▀▀░█▄█░█▀█░█▀█ |
                | ░█▀█░█▀█░█░█░█░█░█░█░█▀█░█░█ |
                | ░▀░▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀░▀░▀░▀ |                           
                |______________________________|
                --------------------------------
                    LIVES LEFT  ♥ ♥ ♡ ♡ ♡ ♡
                --------------------------------   
                ''')
            if turns == 1:
                print(''' 
                  _______________
                 |______________|_  \ words
                ||   ¿  |     ?|| |  \ cannot 
                ||  ?   | ?    || |   \ express
                ||             || |    \ how 
                || o ¿@@@    o || |     \ limited 
                || \ (. .)  /  || |      \ your
                ||  \( O ) /   || *    __ \ vocabulary 
                ||   \ ' |/    || o   (..) \ is 
                ||   |  : |    || |  _| >|_
                ||   |____|    || \ // \/ )
                ||   (    )    ||  \/:    :|
                ||   | `' |    ||  ` :    :|
                ||   | || |    ||    :====:O
                ||   | || |    ||    (    )
                ||   | || |    ||    | `' |
                ||   |_||_|    ||    | || |
                ||   '_'`_`    ||    | || |
                ||             ||    |_||_|
                -----------------     '_'`_`
                /__________________\----------\ 
                |                  |-----------|
                | ░█░█░█▀█░█▀█░█▀▀░█▄█░█▀█░█▀█ |
                | ░█▀█░█▀█░█░█░█░█░█░█░█▀█░█░█ |
                | ░▀░▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀░▀░▀░▀ |                           
                |______________________________|
                --------------------------------
                    LIVES LEFT  ♥ ♡ ♡ ♡ ♡ ♡
                --------------------------------                 
                ''')
            if turns == 0:
                print('''
                  _______________
                 |______________|_
                ||      |      || |    muAhaHaHa!
                ||      |      || |    YOU LOST! :P
                ||    @@@@     || |   
                ||   (X  X)    || |  
                ||   ( ╭╮ )    || O    __  better luck 
                ||   /|' '|\   || \\\\   (..)  next time!
                ||  / | : | \  ||  \\\\  | >|   /¯
                || /  |___|  \ ||   \\\\_\/ )_/
                ||O  (     )  O||    :    :|
                ||   / /w\ \   ||    :    :|
                ||  / /   \ \  ||    :====:O
                || / /     \ \ ||    (    )
                ||/ /       \ \ |    | `' |
                |'_'         `_`|    | || |
                ||             ||    | || |
                ||             ||    |_||_|
                ------------------   '_'`_`
                /__________________\----------\ 
                |                  |-----------|
                | ░█░█░█▀█░█▀█░█▀▀░█▄█░█▀█░█▀█ |
                | ░█▀█░█▀█░█░█░█░█░█░█░█▀█░█░█ |
                | ░▀░▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀░▀░▀░▀ |                           
                |______________________________|
                --------------------------------
                    YOU ARE DEAD  ♡ ♡ ♡ ♡ ♡ ♡
                --------------------------------  
                ''') 
                choice = input("Wanna try again? (Y)/(N) \n▶ ▶   ")
                if choice.upper() == "Y":
                    hangman()
                elif choice.upper() == "N":
                    print("\nThanks for playing.")
                    break
                
                
name = (input("Please enter your name \n▶ ▶   "))
(print(f'''
         
       o/ Welcome, {name}. Let's play...
      /v  ──────────────────────────────────────────╗                     
     />                                             ║     
     o     _     __   _     __   _      __   _     <o>    
    <|>   | |_| / /\ | |\ |/ /`_| |\/| / /\ | |\ |  ║  
    / \   |_| |/_/--\|_| \|\_\_/|_|  |/_/--\|_| \|  ║  
     o                                             _o/     
    <|>                                             |     
    / \ ────────────────────────────────────────────╝
 '''))
print(f"Howdy, challenger. Are you ready to play?")

choice = (input('Press "Y" if YES or "N" if NO \n▶ ▶  '))
if choice.upper() == 'Y':
    print(" ")
    print("What a brave fella!")


    print('''\n
    W A R N I N G !

        ═════════  Everytime you fail   +---+
        █╬█ ███ █╬╬█ ███ █╬█ ███ █╬╬█   |   |
        █▄█ █▄█ ██▄█ █╬▄ █V█ █▄█ ██▄█   O   |
        █╬█ █╬█ █╬██ █▄█ █╬█ █╬█ █╬██  /|\  |
                    a stickman family  / \  |
            is left without a father.       |   
    \n''')

    print("    Guess the word before your 6 lives run out!")
    print(input("\n      [ PRESS ANY KEY TO CONTINUE ]   "))
    hangman()


elif choice.upper() == 'N':
    print(f"\nCome back when you are ready, {name}.")                   