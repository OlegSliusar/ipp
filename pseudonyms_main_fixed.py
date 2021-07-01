"""This script pickes up a random funny Ukrainian pseudonym."""


import sys
import random


def main():
    """Execute the main function."""
    print("Ласкаво просимо в 'Підбір псевдоніма для Івана'\n")
    print("Псевдонім Івана буде:\n\n")

    first = ('Геть', 'Проб', 'Міто', 'Тутан', 'Найшлях', 'Дуд', 'Пуц',
            'Провин', 'Недалек', 'Близ', 'Травкен', 'Перемут')

    last = ('Куцько', 'Додько', 'Паликрай', 'Мітко', 'Забирайко',
            'Недавайко', 'Посилайко', 'Важницький', 'Тамєбік', 'Грішко',
            'Наливайко', 'Шмальницький', 'Конопляник', 'Дідок')

    while True:
        first_name = random.choice(first)

        last_name = random.choice(last)

        print("\n\n")
        print("{} {}".format(first_name, last_name), file=sys.stderr)
        print("\n\n")
        print("\n\nСпробуєш ще? (Натисни Enter або n, щоб вийти)\n")
        try_again = input()
        if try_again.lower() == "n":
            break

    input("\nНажміть Enter для завершення роботи.")

if __name__ == "__main__":
    main()
