print('"Hey User! Lets play a Rock, Paper,scissors game with your computer...."')
print('.')
print('.')
print('.')
import random 
def game():
    while True:
     game_options=('rock','paper','scissors')
     User_choice=input('Choose one option between rock/paper/scissors and write it here: ').lower()
     Computer_choice=random.choice(game_options)
     print(".")
     print(f'Your choice: {User_choice}')
     print(".")
     print(f"Computer's choice: {Computer_choice}")
     if(User_choice=='scissors' and Computer_choice=='rock'):
        print(".")
        print(".")
        print("Alas! You lost time. TRY AGAIN")
        print(".")
        print(".")
     elif(User_choice=='rock' and Computer_choice=='paper'):
        print(".")
        print(".")
        print('Alas! You lost time. TRY AGAIN')
        print(".")
        print(".")
     elif(User_choice=='paper' and Computer_choice=='scissors'):
        print(".")
        print(".")
        print("Alas! You lost time. TRY AGAIN")
        print(".")
        print(".")
     elif(User_choice==Computer_choice):
        print(".")
        print(".")
        print("It's a Tie.Let's play Again.")
        print(".")
        print(".")
     else:
        print(".")
        print(".")
        print('Hurray! You Won.')
        break
game() 