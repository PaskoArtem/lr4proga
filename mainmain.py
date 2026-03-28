def zagruzka_file(put_file):
    try:
        with open(put_file, 'r') as file:
            return set(map(int, file.read().split()))
    except Exception as e:
        print(f'ошибка чтения: {e}')
        return set()

def union(set1, set2):
    return set1 | set2

def intersection(set1, set2):
    return set1 & set2


def difference(set1, set2):
    return set1 - set2

def symmetric_difference(set1, set2):
    return set1 ^ set2

def dekartovo_proizvedenie(set1, set2):
    return {(a, b) for a in set1 for b in set2}

def selection(set1, set2):
    return {x for x in set1 if x %  2 == 0} and {x for x in set2 if x %  2 == 0}

def projection(set1, set2, condition):
    projected_set1 = {x for x in set1 if condition(x)}
    projected_set2 = {x for x in set2 if condition(x)}
    return projected_set1, projected_set2

def division(set1, set2):
    return {a for a in set1 if a in set2}


def main():
    file1 = input('ввести путь к первому файлу:')
    file2 = input('ввести путь ко второму файлу:')

    set1 = zagruzka_file(file1)
    set2 = zagruzka_file(file2)



    while True:
        print('\nвыбрать операцию:')
        print('1 - объединение двух мн-в')
        print('2 - пересечение двух мн-в')
        print('3 - разность двух мн-в')
        print('4 - симметричная разность двух мн-в')
        print('5 - декартово прлизведение двух мн-в')
        print('6 - выборка двух мн-в')
        print('7 - проекция')
        print('8 - деление')
        print('0 - выход')
        choice = input()

        if choice == '1':
            result = union(set1, set2)
            print(result)

        elif choice == '2':
            result = intersection(set1, set2)
            print(result)

        elif choice == '3':
            result = difference(set1, set2)
            print(result)

        elif choice == '4':
            result = symmetric_difference(set1, set2)
            print(result)

        elif choice == '5':
            result = dekartovo_proizvedenie(set1, set2)
            print(result)

        elif choice == '6':
            result = selection(set1, set2)
            print(result)

        elif choice == '7':
            condition = lambda x: x % 2 != 0
            result = projection(set1, set2, condition)
            print(result)

        elif choice == '8':
            result = division(set1, set2)
            print(result)

        elif choice == '0' or choice.lower() == 'exit':
            print('выход')
            break
        else:
            print('неверный выбор')

if __name__ == '__main__':
    main()