user_money: float = 1000
dispossession_threshold = 5_000_000
dispossession_interest = 10     #налог на богатство
count_operations = 0            #счетчик операций
multiplicity = 50               #кратность
transactions_interest = 3       #процент за 3-ю операцию
withdrawal_interest = 1.5       #процент за снятие
withdrawal_min = 30             #минимальный процент за снятие
withdrawal_max = 600            #максимальный процент за снятие


def show_menu():
    print('show_menu...')


def top_up(money):
    print('top_up...')
    global user_money
    dispossession()
    user_money += money
    interest_on_transactions()


def take_off(money):
    print('take_off...')
    global user_money, withdrawal_interest, withdrawal_min, withdrawal_max
    dispossession()
    percent = money * withdrawal_interest / 100
    if percent < withdrawal_min: percent = withdrawal_min
    if percent > withdrawal_max: percent = withdrawal_max
    if user_money < money + percent:
        print('денег не достаточно на счете')
        return
    print(f'процент за снятие: -{percent}, итого снимается: {money + percent}')
    user_money -= (money + percent)
    interest_on_transactions()


def interest_on_transactions():
    global user_money, transactions_interest, count_operations
    count_operations += 1
    if count_operations == 3:
        percent = user_money * transactions_interest / 100
        print(f'начислен процент за каждую 3 операцию: {round(percent, 2)}')
        user_money += percent
        count_operations = 0


def show_account():
    print(f'----------\nсостояние счета: {round(user_money, 2)}')


def round_money(money: float):
    global multiplicity
    res = int(money // multiplicity * multiplicity)
    return res if res != 0 else multiplicity


def dispossession():
    global user_money, dispossession_threshold, dispossession_interest
    if user_money >= dispossession_threshold:
        percent = user_money * dispossession_interest / 100
        print(f'вычитаем налог на богатство: -{percent}')
        user_money -= percent


while True:
    show_account()
    show_menu()
    user_input = input("input operation: ")
    if user_input == 'x':
        break
    if user_input == 'm':
        show_menu()
    if user_input == '1':
        user_sum = round_money(float(input("введите сумму пополнения: ")))
        print(f'сумма округлена: {user_sum}')
        top_up(user_sum)
    if user_input == '2':
        user_sum = round_money(float(input("введите сумму снятия: ")))
        print(f'сумма округлена: {user_sum}')
        take_off(user_sum)