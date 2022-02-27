def find_answer(a, b, n):
    """ пусть s - сумма xi по i от 1 до n
        тогда A = X + s, B = X - s, -> s = (a - b) // 2, X = (a + b) // 2
        Т.к. по условию xi могут повторяться и xi > 0, то для гипотезы необходимо n <= s < inf
        X = 0 при равенстве a и b, следовательно не подходит под условие даже при n = 0,
        т.к. по гипотезе Васи X д.б. натуральным"""

    if any([a <= b, (a - b) % 2, a > b and n == 0]):
        answer = 'NO'
    else:
        s = (a - b) // 2
        answer = 'YES' if n <= s else 'NO'
    return answer


def main():
    a, b, n = map(int, input().split())
    print(find_answer(a, b, n))


if __name__ == '__main__':
    main()
