n = int(input())    # number of elements in the set
row = input().split(' ') # set numbers
myset = set()

myset.update(row)   # adding the set
myset = {int(x) for x in myset}
commands = int(input()) # number of the commands given

for el in range(commands):
    try:
        command, integer = input().split(' ')
    except ValueError:
        integer = 0
        command = 'pop'

    integer = int(integer)
    if command == 'pop':
        myset.pop()
    elif command == 'remove':
        myset.remove(integer)
    elif command == 'discard':
        myset.discard(integer)


set_sum = sum(myset)
print(set_sum)

'''
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5
'''