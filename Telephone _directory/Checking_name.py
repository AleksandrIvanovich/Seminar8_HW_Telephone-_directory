
import re
from typing import List

def checking_the_encoding_and_lenght(arg1: str, arg2_lenght: int):
    while True:
        try:  
            arg1 = input(f'Введите {name_str} (используте кириллицу и цифры):\n')
            if bool(re.match("^[А-Яа-я0-9_-]*$", arg1)) != True:
                print ('Это не кириллица или вы ввели недопустимый символ.') 
            elif len(arg1) > arg2_lenght:
                print('Вы вели слишком много символов') 
            else:   
                return (''.join(arg1)).capitalize()  
        except:
            print('Вы ввели не строку!')  
            
arg2_lengh = 4 # Для облегчени прверки стоит 4, а так 20              
name_str = 'имя'          
name = (checking_the_encoding_and_lenght(name_str,arg2_lengh))
print(name)

arg2_lengh = 5 # Для облегчени прверки стоит 5, а так 40 
name_str = 'фамилию'
surname = (checking_the_encoding_and_lenght(name_str,arg2_lengh))
print(surname)

print(f'{name} {surname}')