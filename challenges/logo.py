from collections import Counter, deque

if __name__ == '__main__':
    # s = input()
    s = 'aabbbccde'
    most_common = sorted(Counter(s).items(), key=lambda x: (-x[1], x[0]))

    for char, count in most_common:
        print(f'{char} {count}', end='\n')
