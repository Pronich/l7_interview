from stack import Stack, BalanceStr

if __name__ == '__main__':
    check_dic = {'{':'}', '(':')', '[':']'}
    balance = BalanceStr(check_dic)
    while True:
        br_str = input('Введите последовательность скобок: ')
        if len(br_str) == 0:
            quit()
        balance.balance_braked(br_str)