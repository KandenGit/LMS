from random import randint
import sys


def draw_board(*, board):
    print('=======================')
    for b in board:
        print(game_board[b[0]-1], end='\n')if b[0] % 3 == 0 else print(game_board[b[0]-1], end=' ')
    print('=======================\n')


def user_motion(*, symbol):
    motion = int(input('Свободное число от 1 до 9: '))
    if motion < 1 or motion > 9:
        print('Играйте строго по правилам!')
        return user_motion(symbol=user_symbol)
    
    if not isinstance(game_board[motion-1][0], str): # если ячейка не строка
        game_board[motion-1][0] = symbol

        if symbol == "X":
            x_indexes.append(motion)
        elif symbol == "O":
            o_indexes.append(motion)

    else:
        print('Эта ячейка занята! Укажите другое число:')
        return user_motion(symbol=user_symbol)
        
    
def bot_motion(*, symbol):
    rand = randint(1, 9)
    if not isinstance(game_board[rand-1][0], str): # если ячейка не строка
        game_board[rand-1][0] = symbol
        if symbol == "X":
            x_indexes.append(rand)
        elif symbol == "O":
            o_indexes.append(rand)
    else:
        bot_motion(symbol=bot_symbol)
    

def get_player_move(*, symbol):
    for i in range(1, 10):
        if symbol == 'X':
                if i % 2 != 0:
                    user_motion(symbol=user_symbol)
                    draw_board(board=board)
                    check_win(x_ind=x_indexes, o_ind=o_indexes)
                if i % 2 == 0:
                    bot_motion(symbol=bot_symbol)
                    draw_board(board=board)
                    check_win(x_ind=x_indexes, o_ind=o_indexes)
        if symbol == 'O':
                if i % 2 == 0:
                    user_motion(symbol=user_symbol)
                    draw_board(board=board)
                    check_win(x_ind=x_indexes, o_ind=o_indexes)
                if i % 2 != 0:
                    bot_motion(symbol=bot_symbol)
                    draw_board(board=board)
                    check_win(x_ind=x_indexes, o_ind=o_indexes)
        
        
def check_win(*, x_ind, o_ind):
    wins_cell = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9], # горизонтальные
        [1, 4, 7], [2, 5, 8], [3, 6, 9], # вертикальные
        [1, 5, 9], [3, 5, 7], # диагональные
    ]

    for cells in wins_cell: # в сells массивы с wins_cell
        count_x = 0
        count_o = 0
        for i in range(0, len(cells)): # в i элементы массива c
            if cells[i] in x_ind:
                count_x += 1
                if count_x == 3:
                    print('Победа X')
                    sys.exit()
            if cells[i] in o_ind:
                count_o += 1
                if count_o == 3:
                    print('Победа O')
                    sys.exit()
            if i == 9 and count_o > 3 and count_x > 3:
                print('Ничья!')
                sys.exit()


def main():
    print("ПРИВЕТСТВУЮ В ИГРЕ КРЕСТИКИ-НОЛИКИ\nДЛЯ СОВЕРШЕНИЯ ХОДА НЕОБХОДИМО ВВОДИТЬ ЦИФРУ ОТ 1 ДО 9\n")

    global user_symbol, bot_symbol, board, game_board, x_indexes, o_indexes

    board = [[i] for i in range(1, 10)] # для итерации
    game_board = [[i] for i in range(1, 10)] # для отображения
    x_indexes = []
    o_indexes = []

    user_symbol = str(input('Введите символ X или O (ENG): ')).upper()
    if user_symbol == "x".upper():
        bot_symbol = "O"
    elif user_symbol == "o".upper():
        bot_symbol = "X"
    else:
        print("Введен некорректный символ!!")
    draw_board(board=board)
    get_player_move(symbol=user_symbol)


if __name__ == '__main__':
    main()