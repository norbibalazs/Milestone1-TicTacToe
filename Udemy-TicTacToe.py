def main():

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

    def play(p1xo):
        print('P1, Its your turn(1-9):')
        print(d)
        h = int(input())
        if 0 < h < 10:
            if d[h] != ' ':
                print('That was previously reserved, choose another one')

            else:
                d[h] = p1xo
                list(map(trow, table1))
        else:
            print('Please give a number between 1 and 9!')

    def play2(p2xo):
        print('P2, Its your turn(1-9):')
        print(d)
        h = int(input())
        if 0 < h < 10:
            if d[h] != ' ':
                print('That was previously reserved, choose another one')
            else:
                d[h] = p2xo
                list(map(trow, table1))
        else:
            print('Please give a number between 1 and 9!')

### winning combinations jkl ###

    j = (1, 4, 7, 1, 3, 1, 2, 3)
    k = (2, 5, 8, 5, 5, 4, 5, 6)
    l = (3, 6, 9, 9, 7, 7, 8, 9)

#### list for saving the steps ###

    d = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

### choose side ###

    print('Lets play Tic Tac Toe!')

    while p1xo != 'X' or p1xo != 'O':
        p1xo = input('P1, please choose: X or O:').upper()
        if p1xo == 'X':
            p2xo = 'O'
            break
        else:
            p2xo = 'X'
            break

### creating the table ###

    table1 = [2, 3, 2, 1, 2, 4, 2, 1, 2, 5, 2]
    list(map(trow, table1))

### Game loop ###

    for x in range(0, len(j), 2):
        if d[j[x]] == d[k[x]] == d[l[x]] == p1xo:
            print('Congratulations P1, You Won!!!')
            restart()
        elif d[j[x]] == d[k[x]] == d[l[x]] == p2xo:
            print('Congratulations P2, You Won!!!')
            restart()
        else:
            if ' ' in d:
                play(p1xo)
            elif ' ' in d:
                play(p2xo)
            else:
                print('Table is full.Game over.')
                restart()


    restart()

main()
