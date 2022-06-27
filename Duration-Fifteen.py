import random
import time

class colors:
    reset='\033[0m'
    bold='\033[01m'
    class fg:
        red='\033[31m'
        orange='\033[33m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        yellow='\033[93m'

def intro():    
    print(f"""{colors.fg.orange}
     ___  __  _____  ___ ______________  _  __  _   _______
    / _ \/ / / / _ \/ _ /_  __/  _/ __ \/ |/ / (_) <  / __/
   / // / /_/ / , _/ __ |/ / _/ // /_/ /    / _    / /__ \ 
  /____/\____/_/|_/_/ |_/_/ /___/\____/_/|_/ (_)  /_/____/\n
    {colors.reset}  """)

    print(input(f"{colors.fg.red}            【  𝙋𝙍𝙀𝙎𝙎 𝘼𝙉𝙔 𝙆𝙀𝙔 𝙏𝙊 𝘾𝙊𝙉𝙏𝙄𝙉𝙐𝙀  】 {colors.reset}\n"))

    name = input(f"{colors.fg.red}𝙀𝙉𝙏𝙀𝙍 𝙔𝙊𝙐𝙍 𝙉𝘼𝙈𝙀\n» {colors.reset}")
    print(f"{colors.fg.darkgrey}Hello there, {colors.fg.orange}{name}{colors.reset}{colors.fg.darkgrey}.{colors.reset}{colors.fg.darkgrey} Would you like to know the rules? (Y/N) {colors.reset}")
    choice = input()
    if choice.upper() == "Y":
        print(f"{colors.fg.lightred}Solve 10 math problems using basic operations ( +, x, - )\nin less than{colors.fg.orange} 15 seconds{colors.fg.lightred} and be a certified mathe-magician!{colors.reset}\n\nYou only have 5 lives!")

intro()

def game():
    choice = input(f"{colors.fg.darkgrey}\n\nDo you want to play? (Y/N)\n>> {colors.reset}")
    while(1):
        if (choice.upper() != "Y"):
            break

        correct = 0
        lives = 5
        duration = time.time()

        while(correct < 10 and lives > 0):

            num1 = random.randint(0, 10)
            num2 = random.randint(0, 10)
            operation = random.randint(0, 2)
            answer = 0
            if(operation==0):
                answer = num1+num2
                print(f"{num1} + {num2} = ")
            elif(operation==1):
                answer = num1-num2
                print(f"{num1} - {num2} = ")
            elif(operation==2):
                answer = num1*num2
                print(f"{num1} x {num2} = ")

            guess = input()

            if(guess != str(answer)):
                lives -= 1
                print(f"{colors.fg.red}{colors.bold}\nYou are wrong.{colors.reset}")
            else:
                correct += 1
                print(f"\n{colors.fg.orange}You are correct.{colors.reset}")

            print(f"\n{colors.fg.darkgrey}Correct answers:{colors.reset}{colors.fg.yellow} {correct}{colors.reset}  |  {colors.fg.darkgrey}Lives left:{colors.reset}{colors.fg.red} {lives}{colors.reset}\n")

        
        if(correct==10):
            duration = time.time() - duration
            print(f"\nGive yourself a pat on the back!\nYou just solved 10 problems in {colors.fg.yellow}{duration:.2f}{colors.reset} seconds!\n\nA little more practice and you'll be a mathe-magician in no time!")

            if (duration <= 15.00):
                print(f"""
                    That was fast! You just solved 10 problems in {colors.fg.yellow}{duration:.2f}{colors.reset} seconds!
                {colors.fg.yellow}
                                         You are a certified
                                        ๑  mathe-magician! ๑ {colors.reset}
               
                                             1+1=2 /\\
                                                \ c")
                                                ;-/\>
                                                  ||

                                """)
        elif(lives==0):
            print(f"\n𝙱𝚛𝚞𝚜𝚑 𝚞𝚙 𝚘𝚗 𝚢𝚘𝚞𝚛 𝚖𝚊𝚝𝚑 𝚜𝚔𝚒𝚕𝚕𝚜! 𝚈𝚘𝚞 𝚌𝚊𝚗 𝚍𝚘 𝚒𝚝!")
            
        choice = input(f"\n{colors.fg.darkgrey}Do you want to play again? Y/N")

game()