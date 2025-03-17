print('"Guess the Number Game(by Computer)"')
print('.')
print('.')
print('.')
print('.')
print("Dear User, I'm your computer, I'm gonna play a game with you.Hope you are excited for the game!")
User_Name:str=input('Enter your Name plz: ')
import random
def Number_Game():
 Computer_number=random.randint(1,25)
 print("I'm thinking of a Random number between 1 to 25.....")
 while True:
       try:
          User_guess=int(input('Guess a number: '))
       except ValueError:
               print('invalid input..Plz ebter a valid number')
       if(User_guess>Computer_number): 
                   print(f'Your guess is too High! Try Again {User_Name}, I know you will guess the right number.')
       elif(User_guess<Computer_number):
                   print(f'Your guess is too Low! Try Again {User_Name}, I know you will guess the right number.')
       else:
                   print('.')
                   print('.')
                   print('.')
                   print(f'Congrats! {User_Name} on your correct guess. I knew that you will guess the right number.')
                   print('.')
                   print('.')
                   print('.')
                   print("well...not praising my-self but, It's interesting when two intelligent minds play a game together.")
                   print(f"{User_Name}, we will meet again next time. Have a nice day, champ!")
                   break
Number_Game()

 