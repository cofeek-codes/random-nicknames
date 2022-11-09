import random


def main():
    words__file = open('words.txt')
    words = words__file.read().split('\n')
    output = f'{random.choice(words)} {random.choice(words)}'
    words__file.close()
    print(output)


if __name__ == '__main__':
    main()
