def loop (dictionary) :
    resault = []
    key = dictionary["start"]
    
    while resault.count(key) == 0 :
        resault.append(key)
        key = dictionary[key]

    return resault

print ( loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}) )