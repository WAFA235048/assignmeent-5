print('Madlib  Project')
print('.')
print('.')
print('.')
print('Instuction: Give all the asked information correctly, Your data will not be shared with anyone!' )
User_name:str=input('Enter your Name:')
#print(f'Attention, {User_name}!')
adjective_option1=('Highly operative')
adjective_option2=('Hghly organized')
adjective_option3=('Most regulated')
print('Following is a list of "Adjectives":')
adjectiveDict1:dict={'a':adjective_option1,'b':adjective_option2,'c':adjective_option3}
for key,value in adjectiveDict1.items():
    print(f'{key}:{value}')
Choose_adverb=input('Choose one "Adjective" from the above listed options and write it here:')
Selected_option=adjectiveDict1[Choose_adverb]
#print(f'This msg is from {Selected_option} secret agency of the country.')
print('.')
print('.')
print('.')
colour_option1=('Black')
colour_option2=('All Black')
colour_option3=('Full Black')
print('Following is a list of "Adverbs":')
adverbdict1:dict={'a':colour_option1,'b':colour_option2,'c':colour_option3}
for key,value in adverbdict1.items():
    print(f'{key}:{value}')
Choose_colour=input('Choose one "Adverb" from the above listed options and write it here:')
Selected_option=adverbdict1[Choose_colour]
#print(f'This msg is from {Selected_option} secret agency of the country.')


 





