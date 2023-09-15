from queens import print_board, random_queens, check_queens

if __name__ == '__main__':
    print("проверка 1: (0,0), (2,3), (3,5), (1,6), (4,7), (5,1), (7,2), (6,4)", end=' -> ')
    print(check_queens([(0, 0), (2, 3), (3, 5), (1, 6), (4, 7), (5, 1), (7, 2), (6, 4)]))
    print_board()

    print("проверка 2: (0,1), (2,3), (3,5), (1,6), (4,7), (5,1), (7,2), (6,4)", end=' -> ')
    print(check_queens([(0, 1), (2, 3), (3, 5), (1, 6), (4, 7), (5, 1), (7, 2), (6, 4)]))
    print_board()

    count_ = 1
    attempt = 0
    while count_ < 5:
        attempt += 1
        if random_queens():
            print(f'случайная расстановка {count_} (попыток: {attempt}): ')
            print_board()
            count_ += 1
            attempt = 0
