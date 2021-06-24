def operations_over_sets (*sets) :

    resaults_set = {}

    for setA in sets :
        for setB in sets :
            if (setA != setB) :
                resaults_set[(repr(setA) + ' | ' + repr(setB))] = setA.intersection(setB)
                resaults_set[(repr(setA) + ' & ' + repr(setB))] = setA.union(setB)
                resaults_set[(repr(setA) + ' - ' + repr(setB))] = setA.difference(setB)
                resaults_set[(repr(setB) + ' - ' + repr(setA))] = setB.difference(setA)

    return resaults_set

print( operations_over_sets({1,2}, {2, 3}) )