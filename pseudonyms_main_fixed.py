"""This script pickes up a random funny Ukrainian pseudonym."""


import sys
import random


def main():
    """Execute the main function."""
    print("Ласкаво просимо в 'Підбір псевдоніма для Івана'\n")
    print("Псевдонім Івана буде:\n\n")

    first_name = ('Геть', 'Проб', 'Міто', 'Тутан', 'Найшлях', 'Дуд', 'Пуц',
            'Провин', 'Недалек', 'Близ', 'Травкен', 'Перемут')

    last_name = ('Куцько', 'Додько', 'Паликрай', 'Мітко', 'Забирайко',
            'Недавайко', 'Посилайко', 'Важницький', 'Тамєбік', 'Грішко',
            'Наливайко', 'Шмальницький', 'Конопляник', 'Дідок')

    family_name = ('Гетьковович', 'Пробовович', 'Мітовович', 'Тутановович', 'Найшляховович', 'Дудовович', 'Пуцовович',
                    'Провинович', 'Недалекович', 'Близович', 'Травенович', 'Перемутович')

    while True:
        first_n = random.choice(first_name)
        last_n = random.choice(last_name)
        family_n = False
        if random.randrange(1, 4) == 1:
            family_n = random.choice(family_name)

        print("\n\n")
        if family_n:
            print("{} {} {}".format(first_n, last_n, family_n), file=sys.stderr)
        else:
            print("{} {}".format(first_n, last_n), file=sys.stderr)

        print("\n\n")
        print("\n\nСпробуєш ще? (Натисни Enter або n, щоб вийти)\n")
        try_again = input()
        if try_again.lower() == "n":
            break

    input("\nНажміть Enter для завершення роботи.")

if __name__ == "__main__":
    main()
