import random
caps = ['s', 'm', 'l']

table = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
round = 0
finished = False
totalrounds = 0


for i in range(1,101):
    while not finished:
        '''ASSIGNS RANDOM SIZE CAP TO RANDOM SQUARE:
        if a square is empty any size cap can be assigned,
        if a square is occupied by a small cap only medium and large caps can be assigned on top of it,
        if a square is occupied by a medium cap, only large caps can be assigned on top of it,
        lastly, if a square is occupied by a large cap, no cap can be assigned in that square so it looks for another'''
        c = random.randrange(9)
        if table[c] == ' ':
            cap = random.choice(caps)
            table[c] = cap
            round += 1
        elif table[c] == 's':
            cap = random.choice(caps[1:2])
            table[c] = cap
            round += 1
        elif table[c] == 'm':
            cap = caps[2]
            table[c] = cap
            round += 1
        elif table[c] == 'l':
            continue

        '''STOPS LOOP WHEN ONE OF THE WINNING CONDITIONS IS SATISFIED:
        three of a kind in a row, column or diagonal,
        from small to large from left to right in a row or diagonal, from top to bottom in a column'''
        if (
                (table[0] == 'l' and table[1] == 'l' and table[2] == 'l') or 
                (table[0] == 'm' and table[1] == 'm' and table[2] == 'm') or 
                (table[0] == 's' and table[1] == 's' and table[2] == 's') or
                (table[0] == 's' and table[1] == 'm' and table[2] == 'l') or
                (table[3] == 'l' and table[4] == 'l' and table[5] == 'l') or 
                (table[3] == 'm' and table[4] == 'm' and table[5] == 'm') or 
                (table[3] == 's' and table[4] == 's' and table[5] == 's') or
                (table[3] == 's' and table[4] == 'm' and table[5] == 'l') or
                (table[6] == 'l' and table[7] == 'l' and table[8] == 'l') or 
                (table[6] == 'm' and table[7] == 'm' and table[8] == 'm') or 
                (table[6] == 's' and table[7] == 's' and table[8] == 's') or
                (table[6] == 's' and table[7] == 'm' and table[8] == 'l') or
                (table[0] == 'l' and table[3] == 'l' and table[6] == 'l') or 
                (table[0] == 'm' and table[3] == 'm' and table[6] == 'm') or 
                (table[0] == 's' and table[3] == 's' and table[6] == 's') or
                (table[0] == 's' and table[3] == 'm' and table[6] == 'l') or
                (table[1] == 'l' and table[4] == 'l' and table[7] == 'l') or 
                (table[1] == 'm' and table[4] == 'm' and table[7] == 'm') or 
                (table[1] == 's' and table[4] == 's' and table[7] == 's') or
                (table[1] == 's' and table[4] == 'm' and table[7] == 'l') or
                (table[2] == 'l' and table[5] == 'l' and table[8] == 'l') or 
                (table[2] == 'm' and table[5] == 'm' and table[8] == 'm') or 
                (table[2] == 's' and table[5] == 's' and table[8] == 's') or
                (table[2] == 's' and table[5] == 'm' and table[8] == 'l') or
                (table[0] == 'l' and table[4] == 'l' and table[8] == 'l') or 
                (table[0] == 'm' and table[4] == 'm' and table[8] == 'm') or 
                (table[0] == 's' and table[4] == 's' and table[8] == 's') or
                (table[0] == 's' and table[4] == 'm' and table[8] == 'l') or
                (table[6] == 'l' and table[4] == 'l' and table[2] == 'l') or 
                (table[6] == 'm' and table[4] == 'm' and table[2] == 'm') or 
                (table[6] == 's' and table[4] == 's' and table[2] == 's') or
                (table[6] == 's' and table[4] == 'm' and table[2] == 'l')
            ):
            finished = True
            
            #PRINTS VISUAL REPRESENTATION OF THE WINNING TABLE IN EACH GAME
            print('GAME', i, '\n')
            print('Winning Table :')
            print(table[:3])
            print('---------------')
            print(table[3:6])
            print('---------------')
            print(table[6:9])
            print('Rounds to Win:', round, '\n\n~~~~~~~~~~~~~~~~~~~~\n')
            
            #CALCULATES THE SUM OF ALL GAMES' ROUNDS
            totalrounds = totalrounds + round
            
        #RESETS TABLE
        if finished == True:
            table = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
     
    #RESETS VALUES
    finished = False
    round = 0


#CALCULATES AVERAGE ROUNDS IN 100 GAMES
average = totalrounds / 100
print('AVERAGE ROUNDS:', average)