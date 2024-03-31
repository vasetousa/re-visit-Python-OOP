def checkDom(strArr):
    # code goes here
    parameters = {
        '<p>': '</p>',
        '<strong>': '</strong>',
        '<em>': '</em>',
        '<i>': '</i>',
        '<b>': '</b>'
    }
    tags_list = []
    tags_errors = []
    tags = ''
    text_in_tags = []
    flag = False
    tag_string = strArr[0]
    for el in tag_string:
        if el == '<':
            if flag and tags:
                text_in_tags.append(tags)
                tags = ''
                flag = False
            tags += el
        elif el == '>':
            tags += el
            tags_list.append(tags)
            tags = ''
            flag = True
        else:
            tags += el

    len_of_tags = len(tags_list)

    if len_of_tags % 2 != 0:
        return 'wrong tag, missing a tag or syntax'

    counter = 0
    message = ''
    tag_flag_element = False
    for element in tags_list:
        if counter == len_of_tags // 2:
            continue

        el = parameters[element]
        el_in_list_from_end_to_beginning = tags_list[len_of_tags - counter - 1]
        next_el_in_list_after_el = tags_list.index(element)+1
        if el == el_in_list_from_end_to_beginning:
            tag_flag_element = True
        elif el == tags_list[next_el_in_list_after_el]:
            tag_flag_element = True
        else:
            tags_errors.append(element)
            tag_flag_element = False
            for _ in tags_list:
                if parameters[element] == _:
                    message = f'the HTML tag is not correct, your {tags_errors[0]} tag might be misplaced'
                else:
                    message = f'the HTML tag is not correct, you have extra {tags_errors[0]} tag'
        counter += 1
    if tag_flag_element:
        return 'the HTML tag is correct'

    return message


# keep this function call here
# print(checkDom(['<p><strong>Hello</strong></p>']))
print(checkDom(['<p><i></i><strong>Hello</strong></p>']))


'''finish logic'''