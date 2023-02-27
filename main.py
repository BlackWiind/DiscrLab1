def is_reflective(matrx: list) -> bool:
    """"
    Проверка на рефлексивность.
    Возвращает False, если хоть одно отношение
    вида xx(т.е. диагональ) равно 0.
    """
    for x in range(len(matrx)):
        if not matrx[x][x]:
            return False
    return True


def is_antireflectiv(matrx: list) -> bool:
    """"
      Проверка на антирефлексивность.
      Возвращает False, если хоть одно отношение
      вида xx(т.е. диагональ) равно 1.
      """
    for x in range(len(matrx)):
        if matrx[x][x]:
            return False
    return True


def is_symmetric(matrx: list) -> bool:
    """"
         Проверка на симметричность.
         Возвращает False, если не выполняется хотя бы
         одно xy=>yx(т.е если в ячейке xy стоит 1,
         в yx тоже должен стоять 1. Так же и для нулей)
    """
    for x in range(len(matrx)):
        for y in range(x, len(matrx)):
            if not matrx[x][y] == matrx[y][x]:
                return False
    return True


def is_antisymmetric(matrx: list) -> bool:
    """"
            Проверка на ансимметричность.
            Возвращает False,если вне главной диагонали A*At
             не все элементы равны 0
       """
    for x in range(len(matrx)):
        for y in range(x, len(matrx)):
            if matrx[x][y] and matrx[y][x]:
                if x != y:
                    return False
    return True


def is_transitive(matrx: list) -> bool:
    """"
            Проверка на транзитивность.
            Возвращает False, A*A!= A
       """
    for x in range(len(matrx)):
        for y in range(len(matrx)):
            for z in range(len(matrx)):
                if matrx[x][y] and matrx[y][z]:
                    if not matrx[x][z]:
                        return False
    return True


def input_set() -> list:
    """"
    Функция ввода множества, list(set()) преобразует строку
    в множество, что убирает повторы, далее множество преобразуется
    в список.
    Возвращает отсортированный список.
    """
    user_input = input('Введите набор элементов множества:\n')
    input_set = list(set(user_input))
    input_set.sort()

    return input_set


def input_pairs() -> list:
    """
    Функция ввода пар отношений. Введённые символы разбиваются по пробелам(split()).
    Далее с преобразуются в список кортежей символов. Неверно введённые данные
    будут проигнорированны.
    """
    pairs_input = input('Введите пары символов, разделённые пробелом.\nВнимание!'
                        ' Некоректно введённые данные будут проигнорированы:\n').split()
    pairs_list = list(map(tuple, pairs_input))
    return pairs_list


def print_matrix(set_a: list, pairs: list):
    """

    :param set_a: множество
    :param pairs: пары отношений
    :return: None

    Создаёт и выводит матрицу отношений на основе введённого множества
    и пар отношений. Запускает проверки для матрицы.
    """
    matrix = [[1 if (i, j) in pairs else 0 for j in set_a] for i in set_a]
    print("! " + ' '.join(set_a))
    for index in range(len(set_a)):
        print(f"{set_a[index]} " + ' '.join(list(map(str, matrix[index]))))
    print(f"Отношение {'рефлексивно' if is_reflective(matrix) else 'не рефлексивно'}")
    print(f"Отношение {'антирефлексивно' if is_antireflectiv(matrix) else 'не антирефлексивно'}")
    print(f"Отношение {'симметрично' if is_symmetric(matrix) else 'не симметрично'}")
    print(f"Отношение {'антисимметрично' if is_antisymmetric(matrix) else 'не антисимметрично'}")
    print(f"Отношение {'транзитивно' if is_transitive(matrix) else 'не транзитивно'}")


def main():
    set_a = input_set()
    pairs = input_pairs()
    print_matrix(set_a, pairs)
    while True:
        user_input = input("1. Ввести новый набор элементов.\n"
                           "2. Ввести новые пары символов.\n"
                           "3. Выход.\n")
        match user_input:
            case "1":
                set_a = input_set()
            case "2":
                pairs = input_pairs()
            case "3":
                exit()
            case _:
                print("Неверная команда")
        print_matrix(set_a, pairs)


if __name__ == '__main__':
    main()
