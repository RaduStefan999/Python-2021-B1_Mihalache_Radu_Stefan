def lists_operation (*lists, x) :
    item_list = []

    for list in lists :
        hash_map = {}

        for item in list :
            if ((item in hash_map) == False) :
                hash_map[item] = 1
            else :
                hash_map[item] += 1

        for item in hash_map :
            if (hash_map[item] == x) :
                item_list.append(item)

    return item_list

print(lists_operation(['hello', 'it', 'is', 'me', 'hello'], ['can', 'I', 'can'], ['I', 'anymore', 'anymore'], x = 2))

