class Madlib:
    User_Name:str
    Noun_dict:dict
    Adjective_dict:dict
    Colour_dict:dict
    Verb1_dict:dict
    Verb2_dict:dict
    User_home_adress:str
    User_Regularly_visited_place:str
    Verb3_dict:dict
    Verb4_dict:dict
    Dictionaries_Group:dict
    #.
    #.
    #.
    #>Constructor Function:
    #>
    #>
    def __init__(self,
    User_Name:str,
    Noun_dict:dict,
    Adjective_dict:dict,
    Colour_dict:dict,
    Verb1_dict:dict,
    Verb2_dict:dict,
    User_home_adress:str,
    User_Regularly_visited_place:str,
    Verb3_dict:dict,
    Verb4_dict:dict,
    Dictionaries_Group:dict):
        self.User_Name=User_Name
        self.Noun_dict=Noun_dict
        self.Adjective_dict=Adjective_dict
        self.Colour_dict=Colour_dict
        self.Verb1_dict=Verb1_dict
        self.Verb2_dict=Verb2_dict
        self.User_home_adress=User_home_adress
        self.User_Regularly_visited_place=User_Regularly_visited_place
        self.Verb3_dict=Verb3_dict
        self.Verb4_dict=Verb4_dict
        self.Dictionaries_Group=Dictionaries_Group
    #.
    #.
    #.
    #>Method:
    #>
    #>
    def Madlib_Project(self):
        for everyDictionary in self.Dictionaries_Group.values():
            for key,value in everyDictionary.items():
                print(everyDictionary.items())
                print(f'{key},{value}')
                break
        Choose_option=input('Choose one Option from the above list & write the chosen option a/b/c here:')
        Selected_option=everyDictionary[Choose_option]
        print(f'Your Selected option:{Selected_option}')
    #.
    #.
    #.
    #>Objects:
    #>
    #>
Paragraph=Madlib(
                 input('Enter your Name: '),
                 {'a':'Tech','b':'Cyber','c':'I.T.'},
                 {'a':'Highly operative','b':'Hghly organized','c':'Most regulated'},
                 {'a':'All Black','b':'Black','c':'Full Black'},
                 {'a':'Watching','b':'Viewing','c':'Engaging with'},
                 {'a':'tracked','b':'analyzed','c':'reviewed'},
                 input('Enter your Home adress: '),
                 input('Enter a place or Location where you Regularly Visit: '),
                 {'a':'Warn','b':'notify','c':'advise'},
                 {'a':'wish','b':'plan','c':'intend'},
                 {
                   'Dict1': {'a': 'Tech', 'b': 'Cyber', 'c': 'I.T.'},
                   'Dict2': {'a': 'Highly operative','b': 'Highly organized', 'c': 'Most regulated'},
                   'Dict3': {'a': 'All Black', 'b': 'Black', 'c': 'Full Black'},
                   'Dict4': {'a': 'Watching', 'b': 'Viewing', 'c': 'Engaging with'},
                   'Dict5': {'a': 'tracked', 'b': 'analyzed', 'c': 'reviewed'},
                   'Dict6': {'a': 'Warn', 'b': 'notify', 'c': 'advise'},
                   'Dict7': {'a': 'wish', 'b': 'plan', 'c': 'intend'}
                 })
Paragraph.User_Name
Paragraph.Noun_dict
print('Dont write the complete option just write a/b/c.')
Paragraph.Madlib_Project()
Paragraph.Adjective_dict
Paragraph.Madlib_Project()
Paragraph.Colour_dict
Paragraph.Madlib_Project()
Paragraph.Verb1_dict
Paragraph.Madlib_Project()
Paragraph.Verb2_dict
Paragraph.Madlib_Project()
Paragraph.User_home_adress
Paragraph.User_Regularly_visited_place
Paragraph.Verb3_dict
Paragraph.Madlib_Project()
Paragraph.Verb4_dict
Paragraph.Madlib_Project()
Paragraph.Dictionaries_Group
Paragraph.Madlib_Project()
print('Read this msg completely and carefully otherwise You will responsible for your own circuimstaces')
print(f' OFFICIAL NOTICE')
print(f'Attention:{Paragraph.User_Name}!')
print(f'This is an official transmission from The {Paragraph.Noun_dict} Secret Agency popularly known as "The ones with The {Paragraph.Colour_dict} Vigo".') 
print(f'This is to inform you that Our {Paragraph.Noun_dict} department has been monitoring social media platforms  and has identified certain unusual patterns. Reports indicate that some individuals have been {Paragraph.Verb1_dict} content such as videos criticizing our agency, post against our agency,etc.on social media platform  like YouTube, Facebook, X, etc. Additionally, some haveliked, shared or commented  on such vedios, posts,etc. against our agency.')
print(f'After some weeks of data collection , our {Paragraph.Noun_dict} department has {Paragraph.Verb2_dict} the data and interenet acitivity of those involved. Your ID has been flagged as one of the individuals engaged in the suspicious content consumption.')
print(f'This is our first and last message to you. If you do not stop engaging with such content, we will take necessary measures right at 2:30 A.M., any day in the next few weeks. We have your complete personal details, including your current home address that is {Paragraph.User_home_adress} and also about {Paragraph.User_Regularly_visited_place} where you regularly go.')
print(f'We {Paragraph.Verb3_dict} you to stop such activity if you {Paragraph.Verb4_dict} to spend the upcoming holidays with your family.')
print(f'This is your only & final warning.')
print('We are watching.......')



                   
    
     
    