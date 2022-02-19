text = input()

#REMOVES ALL UNWANTED CHARACTERS
bad = '!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~0123456789\n\t\r'
for i in bad:
    text = text.replace(i, ' ')
    
    
#SEPERATES WORDS
words = text.split(' ')


#REMOVES EXTRA SPACES
words = [i for i in words if i != '']


#CALCULATES HOW MANY N-LENGHT WORDS EXIST
def counter(words, n):
    c = 0 
    for i in words:
        if len(i) == n:
            c += 1
    return c

for i in range(1, len(max(words, key=len))+1):
    if counter(words, i) != 1:
        print('There Are', counter(words, i), 'Words With:', i, 'Letters')
    else:
        print('There Is', counter(words, i), 'Word With', i, 'Letters')