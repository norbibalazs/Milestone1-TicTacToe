import os

def main():

    def clear():
        os.system( 'cls' )

    def restart():
        restart = input('Do you want to play again? Y/N').lower()
        if restart == 'y':
            main()
        else:
            exit()

    def trow(rownum):
        if rownum == 1:
            print('-----------------')
        if rownum == 2:
            print('     |     |     ')
        if rownum == 3:
            print(' ', d[7], ' | ', d[8], ' | ', d[9], ' ')
        if rownum == 4:
            print(' ', d[4], ' | ', d[5], ' | ', d[6], ' ')
        if rownum == 5:
            print(' ', d[1], ' | ', d[2], ' | ', d[3], ' ')

    def play1(player):
        print('P1, Its your turn(1-9):')
        try:
            h = int(input())
            if 0 < h < 10:
                if d[h] != ' ':
                    print('That was previously reserved, choose another one')
                    play1(p1)
                else:
                    d[h] = player
            else:
                print('Please give a number between 1 and 9!')
                play1(p1)
        except ValueError:
            print('Please give a number between 1 and 9!')
            play1(p1)


    def play2(player):
        print('P2, Its your turn(1-9):')
        try:
            h = int(input())
            if 0 < h < 10:
                if d[h] != ' ':
                    print('That was previously reserved, choose another one')
                    play2(p2)
                else:
                    d[h] = player
            else:
                print('Please give a number between 1 and 9!')
                play2(p2)
        except ValueError:
            print('Please give a number between 1 and 9!')
            play2(p2)

### winning combinations jkl ###

    j = (1, 4, 7, 1, 3, 1, 2, 3)
    k = (2, 5, 8, 5, 5, 4, 5, 6)
    l = (3, 6, 9, 9, 7, 7, 8, 9)

#### list for saving the steps ###

    d = ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

### choose side ###

    print('Lets play Tic Tac Toe!')
    while True:
        p1 = input('P1, please choose: X or O:').upper()
        if p1 == 'X':
            p2 = 'O'
            break
        elif p1 == 'O':
            p2 = 'X'
            break
        else:
            continue

### creating the table ###

    table1 = [2, 3, 2, 1, 2, 4, 2, 1, 2, 5, 2]
    clear()
    list(map(trow, table1))

### Game loop ###

    while True:
        for x in range(1, 10):
            for y in range(0, len(j)):
                if d[j[y]] == d[k[y]] == d[l[y]] == p1:
                    print('Congratulations P1, You Won!!!')
                    restart()
                elif d[j[y]] == d[k[y]] == d[l[y]] == p2:
                    print('Congratulations P2, You Won!!!')
                    restart()
            if ' ' in d:
                if x % 2 != 0:
                    print('Player 1 is {}'.format(p1))
                    print('Player 2 is {}'.format(p2))
                    play1(p1)
                    clear()
                    list(map(trow, table1))
                else:
                    print('Player 1 is {}'.format(p1))
                    print('Player 2 is {}'.format(p2))
                    play2(p2)
                    clear()
                    list(map(trow, table1))
            else:
                print('Table is full. Its a tie.')
                restart()


main()