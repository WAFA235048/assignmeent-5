print('"Your Password Generator"')
print('.')
print('.')
print('.')
print('Hey User!Lets generate some passwords for you....')
print('.')
print('.')
import random
Password_Characters="""1234567890abcdefghikjlmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ},".'-=_+!@#$%^&*(){|/<>?:;[]"""
No_of_passwords=int(input('Enter the number of passwords you want to generate: '))
print(".")
Password_length=int(input('Enter the length of Password(No. of charachters you want in your password): '))
print(".")
print('Suggested password/s for you:')
print(".")
for p in range(No_of_passwords):
 Generated_password=""
 for l in range(Password_length):
    Generated_password += random.choice(Password_Characters)
 print(f'Password:  {Generated_password}')

                    

