
def leiadinheiro(text = ''):
    user_input = input(text)
    
    user_input = user_input.lower()
    user_input = user_input.replace('r$', '')
    user_input = user_input.replace(',', '.')
    
    if len(user_input) == 0:
        return 'invalid'

    if user_input.count('.') > 1:
        return 'invalid'

    if not user_input.replace('.','').isnumeric():
        return 'invalid'

    return user_input


