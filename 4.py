def find_count_bu(n, m):
    """  Заметим, что задача симметрична относительно главной диагонали доски, поэтому f(n, m) = f(m, n)
         Можно сделать быструю проверку, если доска слишком вытянутая, т.к. на линии i доски конь не может
        оказаться правее, чем в столбце 2 * i - 1 (каждый раз прыгая на 2 клетки вправо и 1 вверх)
         Применим дин. программирование снизу вверх. Если d[i][j] - количество вариантов, которыми можно добраться
        в клетку i, j, то d[i][j] = d[i - 2][j - 1] + d[i - 1][j - 2]
         Для оптимизации памяти можно хранить не всю доску d, а только 2 предыдущих линии """

    if n > m:
        n, m = m, n
    if m // n >= 2:         # слишком вытянутая доска
        return 0
    if n == 1:              # Крайние случаи для доски в 1 или 2 линию
        return 1 if m == 1 else 0
    elif n == 2:
        return 1 if m == 3 else 0
    else:
        prev = [0] * m
        pre_prev = prev.copy()
        pre_prev[0] = 1
        prev[2] = 1         # prev и pre_prev - линии на одну и две ниже текущей, задаем начальные значения
        for i in range(2, n):
            cur = [0] * m
            cur[1] += pre_prev[0]
            for j in range(2, m):
                cur[j] += prev[j - 2] + pre_prev[j - 1]
            prev, pre_prev = cur, prev
        return cur[-1]


def main():
    n, m = map(int, input().split())
    print(find_count_bu(n, m))


if __name__ == '__main__':
    main()
