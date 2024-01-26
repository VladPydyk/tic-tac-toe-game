print('*' * 10, "Крестики нолики", '*' * 10)

field = list(range(1, 10))


def creat_field(field):
    print('-' * 13)
    for i in range(3):
        print('|', field[0 + i * 3], '|', field[1 + i * 3], '|', field[2 + i * 3], '|')
        print('-' * 13)


def take_input(player):
    valid = False
    while not valid:
        player_answer = input('Куда поставим ' + player + ' ? ')
        try:
            player_answer = int(player_answer)
        except:
            print('Некорректный ввод. Введите только число.')
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(field[player_answer - 1]) not in 'X или O'):
                field[player_answer - 1] = player
                valid = True
            else:
                print('Эта клетка уже занята')
        else:
            print('Введите только число от 1 до 9  куда будем ставить символ Х или O')


def check_win(field):
    winning_positions = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in winning_positions:
        if field[each[0]] == field[each[1]] == field[each[2]]:
            return field[each[0]]
    return False


def main(field):
    counter = 0
    win = False
    while not win:
        creat_field(field)
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        counter += 1
        if counter > 4:
            tmp = check_win(field)
            if tmp:
                print(tmp, 'Выйграл, поздравляем игрока.')
                win = True
                break
        if counter == 9:
            print('Ничья увы')
            break
    creat_field(field)


main(field)
input("Нажмите Enter  для выхода или новой игры")