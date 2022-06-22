def multiple_references():
    print("Example where you get 3 references to the very same empty list")
    lists = [[]]*3
    lists[0].append(3)
    print(lists[0:3])
    print('This is how it\'s supposed to generate 3 distinct lists')
    listz = [[] for i in range(3)]
    listz[0].append(3)
    listz[0].append(4)
    listz[1].append(7)
    listz[1].append(1)
    print(listz[0:3])


def operation_with_mutable_seq():
    print('This function shows the differences between various methods applied to a \'list\' item')
    t = []
    x = True
    while True:
        user_choice = input('Choose [1-6]: (any other key to quit)\n'
                            '***** Those are the correct examples *****\n'
                            '1)\tfor append() method\n'
                            '2)\tfor concatenation operator\n'
                            '***** And those are wrong *****\n'
                            '3)\tWrong append\n'
                            '4)\tAssigning the return of append() to a var\n'
                            '5)\tUse of the concatenation operator without assignment\n'
                            '6)\tMixed concatenation of list and string items\n')
        match user_choice:
            case '1': t.append(x)
            case '2': t = t + [x]
            case '3': t.append([x])  # Creates a new list item and append it to existing list
            case '4': t = t.append(x)  # t == None
            case '5': t + [x]  # Does nothing
            case '6': t = t + x  # TypeError: can only concatenate list to list
            case _: quit(2)
        print(t)
        del t[0]


# Driver
choose_function = input('Pick an app from the list:\n'
                        '1)\tmultiple_reference\n'
                        '2)\toperation_with_mutable_seq\n')
match choose_function:
    case '1': multiple_references()
    case '2': operation_with_mutable_seq()
