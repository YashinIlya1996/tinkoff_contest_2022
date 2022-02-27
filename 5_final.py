def find_min_jumps_iter(n, a, c):
    """ Будем хранить множество точек cer_set, в которых может остановться Линк после count прыжков.
        Также будем хранить множество точек prev_set, в которых Линк мог остановиться до того как сделал count прыжков.
        Очевидно, что если на прыжке с номером count он бы остановился в точке из prev_set, то это только увеличило бы
          колличество прыжков до вершины.
        На каждом прыжке проверяем, есть ли в cur_set точки, в которых можно допрыгнуть до вершины, если нет -
          создаем множество доступных новых точек для следующего прыжка и повторяем, пока есть новые точки"""

    cur_set = {n}
    count = 0
    prev_set = set()
    while cur_set:
        count += 1
        for el in cur_set:
            if a[el] >= el:
                return count
        else:
            prev_set |= cur_set
            next_list = []
            for el in cur_set:
                next_list += c[n - a[el]: el + 1]
            cur_set = set(next_list) - prev_set
    return -1


def check_possibility(c, a):
    """ Быстрая проверка на гипотетическую возможность добраться до вершины.
        set(c) - множество всех точек, в которых может оказаться Линк, если бы он мог приземлиться в любой из точек.
        Если ни из одной точки из set(c) нельзя допрыгнуть до вершины, то не стоит и пытаться """

    for el in set(c) - {0}:
        if a[el] >= el:
            return True
    return False


def main():
    """ Введем вспомогательный список c. c[i] = i + b[i] показывает, на какой высоте Линк окажется
        после того как после прыжка приземлился на расстоянии i от вершины и проскользил на b[i] вниз
        Для удобства обращения по индексу к a и b добавим слева [0] """

    n = int(input())
    a = [0] + [el for el in map(int, input().split())]
    b = [0] + [el for el in map(int, input().split())]
    c = [i + b[i] for i in range(n + 1)]
    answer = find_min_jumps_iter(n, a, c) if check_possibility(c, a) else -1
    print(answer)


if __name__ == '__main__':
    main()
