

def load_bingo_data(input_file: str):
    with open(input_file) as input:
        numbers_called = next(input).strip().split(',')
        next(input) # skip the newline here

        # build boards
        bingo_boards = []
        board = []
        try:
            while line:=next(input):
                if line != '\n':
                    board.append(line.strip().split())
                else:
                    bingo_boards.append(board)
                    board = []
        except StopIteration:
            pass
    return (numbers_called, bingo_boards)

def bingo_win_points(numbers_called, bingo_boards) -> int:
    for numbers in numbers_called:
        for i in range(len(bingo_boards)):
            # boards
            for j in range(len(bingo_boards[i])):
                # rows
                for k in range(len(bingo_boards[i][j])):
                    # numbers
                    if numbers == bingo_boards[i][j][k]:
                        bingo_boards[i][j][k] = 'x'
                        if has_bingo(bingo_boards[i]):
                            print(f'Won on number {numbers} with board: ')
                            print_board(bingo_boards[i])
                            return int(numbers) * board_points(bingo_boards[i])

def bingo_lose_points(numbers_called, bingo_boards) -> int:
    won_boards = 0
    for numbers in numbers_called:
        for i in range(len(bingo_boards)):
            # boards
            for j in range(len(bingo_boards[i])):
                # rows
                for k in range(len(bingo_boards[i][j])):
                    # numbers
                    if numbers == bingo_boards[i][j][k]:
                        bingo_boards[i][j][k] = 'x'
                        if has_bingo(bingo_boards[i]):
                            print('A board won!')
                            won_boards += 1
                            if won_boards == len(bingo_boards):
                                return int(numbers) * board_points(bingo_boards[i])
                            blank_board(bingo_boards[i])
    

def has_bingo(board) -> bool:
    for row in board:
        if check_straight(row):
            return True
    for y in range(5):
        col_indices = zip(range(5),[y]*5)
        col = [board[col_index[0]][col_index[1]] for col_index in col_indices]
        if check_straight(col):
            return True
    # if board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4]:
    #     return True
    # if board[0][4] == board[1][3] == board[2][2] == board[3][1] == board[4][0]:
    #     return True
    return False
            
def check_straight(length) -> bool:
    x_count = 0
    for number in length:
        if number == 'x':
            x_count += 1
    if x_count == 5:
        return True
    # elif x_count == 4:
    #     print('A board is getting close!')
    return False

def board_points(board) -> int:
    total_points = 0
    for row in board:
        for number in row:
            if number != 'x':
                total_points += int(number)
    return total_points

def print_board(board):
    for row in board:
        print(row)
    print('\n')

def blank_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = -1


if __name__ == '__main__':
    numbers_called, bingo_boards = load_bingo_data('input.txt')
    print(bingo_win_points(numbers_called, bingo_boards))
    numbers_called, bingo_boards = load_bingo_data('input.txt')
    print(bingo_lose_points(numbers_called, bingo_boards))