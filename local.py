board={
    'T1':' ','T2':' ','T3':' ',
    'A1':' ','A2':' ','A3':' ',
    'C1':' ','C2':' ','C3':' '

}
player = 1       #first player
total_moves = 0  #count the moves

print('T1|T2|T3')
print('- +- +-')
print('A1|A2|A3')
print('- +- +-')
print('C1|C2|C3')
print('====================')

while True:
    print(board['T1']+'|'+board['T2']+'|'+board['T3'])
    print('-+-+-')
    print(board['A1']+'|'+board['A2']+'|'+board['A3'])
    print('-+-+-')
    print(board['C1']+'|'+board['C2']+'|'+board['C3'])
    if total_moves == 9:
        break
    while True:     #input from player
        if player == 1:     #choose player
            p1_input = input('player one')
            if p1_input.upper() in board and board[p1_input.upper()] == '':
                board[p1_input.upper()] = 'X'
                player = 2
                break
            else:
                print('Invalid Input')
                continue

        else:
            p2_input = input('player two')
            if p2_input.upper() in board and board[p2_input.upper()] =='':
                board[p2_input.uppper()] = 'O'
                player = 1
                break
            else:
                print('Invalid input')
                continue
    total_moves += 1
    print('=================')
    
