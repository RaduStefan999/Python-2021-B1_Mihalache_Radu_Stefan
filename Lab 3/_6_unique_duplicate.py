def unique_duplicate (list) :
    set_from_list = set(list)
    return (len(set_from_list), len(list) - len(set_from_list))


A = [10, 10, 2, 2, 13, 17, 99, 2]
print(unique_duplicate(A))