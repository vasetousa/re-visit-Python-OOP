def merge_the_tools(string, k):
    # your code goes here
    mylist = []
    operations = 0
    new_string = ''
    last_element = None
    for el in string:
        if operations == k:
            mylist.append(new_string)
            new_string = ''
            operations = 0
            last_element = None
        if el != last_element:
            if el not in new_string:
                new_string += el
                last_element = el
        else:
            last_element = el

        operations += 1

    mylist.append(new_string)
    print('\n'.join(mylist))


if __name__ == '__main__':
    string = 'AABCAAADA'
    k = 3
    # string, k = input(), int(input())
    merge_the_tools(string, k)
