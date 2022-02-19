file = open('C:/ergasies_python/pogg.txt', 'r')
text = file.read()
file.close()

#MAKES CAPITAL LETTERS LOWER-CASE
text = text.lower()


#REMOVES ALL UNWANTED CHARACTERS
bad = '!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~0123456789\n\t\r'
for i in bad:
    text = text.replace(i, ' ')


#SEPERATES WORDS
words = text.split(' ')


#REMOVES EXTRA SPACES
words = [i for i in words if i != '']


#PRINTS THE 10 MOST POPULAR WORDS AND HOW MANY TIMES THEY APPEAR
from collections import Counter

countmc = Counter(words)
print('TEN MOST POPULAR WORDS:')
print(countmc.most_common(10), '\n')


letters = 'abcdefghijklmnopqrstuvwxyz'


#CALCULATES THE 3 MOST COMMON 2-LETTER COMBINATIONS THE WORDS START WITH
max = [0, 0, 0]
maxl = ['', '', '', '', '', '']

for i in letters:
    for j in letters:
        c = 0
        for k in range (0, len(words)):
            if words[k][:2] == i + j:
                c +=1

        if c > max[0]:
            max[0] =  c
            maxl[0] = 'words starting with:'
            maxl[1] = i+j
        elif c > max[1] and c <= max[0]:
            max[1] =  c
            maxl[2] = 'words starting with:'
            maxl[3] = i+j
        elif c > max[2] and c <= max[1]:
            max[2] =  c
            maxl[4] = 'words starting with:'
            maxl[5] = i+j

print(max[0], maxl[0], maxl[1])
print(max[1], maxl[2], maxl[3])
print(max[2], maxl[4], maxl[5], '\n')


#CALCULATES THE 3 MOST COMMON 3-LETTER COMBINATIONS THE WORDS START WITH
max2 = [0, 0, 0]
maxl2 = ['', '', '', '', '', '']

for i in letters:
    for j in letters:
        for l in letters:
            c = 0
            for k in range (0, len(words)):
                if words[k][:3] == i + j + l:
                    c +=1
            
            if c > max2[0]:
                max2[0] =  c
                maxl2[0] = 'words starting with:'
                maxl2[1] = i+j+l
            elif c > max2[1] and c <= max2[0]:
                max2[1] =  c
                maxl2[2] = 'words starting with:'
                maxl2[3] = i+j+l
            elif c > max2[2] and c <= max2[1]:
                max2[2] =  c
                maxl2[4] = 'words starting with:'
                maxl2[5] = i+j+l

print(max2[0], maxl2[0], maxl2[1])
print(max2[1], maxl2[2], maxl2[3])
print(max2[2], maxl2[4], maxl2[5])