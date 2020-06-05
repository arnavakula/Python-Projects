statements = []
questions = ['How', 'Why', 'What', 'Where', 'When', 'Which', 'Who', 'Whom']

def capitalize(user_input):
    words = user_input.split(' ')
    words[0] = words[0].title()
    return words

def punctuate(words):
    if(words[0] in questions): 
        words[-1] += '?'
    else:
        words[-1] += '.'
    return words

while(True):
    user_input = input("Say something: ")
    if(user_input.lower() == '\end'): 
        break
    else:
        words = capitalize(user_input)
        statements.append(' '.join(punctuate(words)))

for s in statements:
    print(s)

