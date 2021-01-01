while True:
    
    result = input('Enter number:')

    try:
        result = float(result)

    except ValueError or TypeError:
        print (f'{result} is not a number')

    else:
        break

while True:
    
    user_operator = input('Enter operator:')

    if user_operator == '=':
        print (result)
        break

    user_item_1 = input('Enter number:')

    if user_item_1 == '=':
        print (result)
        break

    try:
        user_item_1 = float(user_item_1)
        
    except (ValueError, TypeError):
        print (f'{user_item_1} is not a number')
        user_item_1 = input('Enter number again:')
        user_item_1 = float(user_item_1)
        
    if user_operator == '+':
        result += user_item_1
            
    elif user_operator == '-':
        result -= user_item_1
            
    elif user_operator == '*':
        result *= user_item_1

    elif user_operator == '/':
        result /= user_item_1
            
    else:
        print ('Please try again')
