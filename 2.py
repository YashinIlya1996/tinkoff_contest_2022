def find_buckets_count(n, m):
    """ До тех пор, пока размер наименьшей стороны получившегося прямоугольника равен
        предыдущему, будут закрашиваться квадраты одинакового размера.
        Количество таких квадратов (и ведер) определяется целочсленным делением длины большей стороны на
        длину меньшей стороны, остаток от деления - новая наименьшая сторона получившегося прямоугольника
        Отрезаем квадраты, пока есть возможность и считаем их количество """

    count = 0
    if n > m:
        n, m = m, n
    while n and m:
        count += m // n
        n, m = m % n, n
    return count


def main():
    n, m = map(int, input().split())
    print(find_buckets_count(n, m))


def test():
    from random import randint
    for _ in range(1000):
        n = randint(1, 10 ** 18)
        m = randint(1, 10 ** 18)
        assert find_buckets_count(n, m) == find_buckets_count(m, n)
        assert find_buckets_count(n, n) == find_buckets_count(m, m) == 1
        print('OK')


if __name__ == '__main__':
    main()
