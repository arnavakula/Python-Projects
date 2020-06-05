

statements = []
questions = ['How', 'Why', 'What', 'Where', 'When', 'Which', 'Who', 'Whom']

while(True):
    user_input = input("Say something: ")
    if(user_input.lower() == '\end'): 
        break
    else:
        words = user_input.split(' ')
        words[0] = words[0].title()
        if(words[0] in questions): 
            words[-1] += '?'
        else:
            words[-1] += '.'
        statements.append(' '.join(words))

for s in statements:
    print(s)