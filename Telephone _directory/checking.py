

tel_number = list(input('Введите номер телефона в формате +|Код страны|xxx|xxxxxxx|:\n'))

def checking_for_correctness_of_input(arg: str) -> str:
    lenght_tel = len(arg)
    plus = arg[:1:lenght_tel-1]
    body_number = ''.join(arg[1:])
    result_str = ''
    if plus[0] != '+':
        print("Ошибка ввода! Начните вводить с '+'")  
    elif body_number.isdigit() != True:
        print("Ошибка ввода! Вы ввели не цифру!")
    elif len(body_number) > 17:
        print('Вы ввели слишком много цифр')
    else:
        result_str = ''.join(arg) 
    return result_str
 
print(checking_for_correctness_of_input(tel_number))

