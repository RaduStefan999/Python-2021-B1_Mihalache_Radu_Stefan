def group_by_rhyme (words) :
    words = sorted(words, key = lambda word: word[-2:])

    rhyme = words[0][-2:]

    rhyme_words_list = []
    word_rhymed = [words[0]]

    words = words[1:]

    for word in words :
        
        if rhyme == word[-2:] :
            word_rhymed.append(word)
        else :
            rhyme_words_list.append(word_rhymed)
            word_rhymed = [word]
            rhyme = word[-2:]

    rhyme_words_list.append(word_rhymed)
    

    return rhyme_words_list


print(group_by_rhyme(['ana', 'giovani', 'banana', 'carte', 'mecani', 'arme', 'parte', 'bani'])) 