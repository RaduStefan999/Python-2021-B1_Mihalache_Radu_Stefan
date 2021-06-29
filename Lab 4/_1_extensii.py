import os

def extensii (director) :
    extensii_list = set([])
    files = os.listdir(director)
    
    for file in files :
        for poz in range(len(file) - 1 , 0, -1):
            if (file[poz] == '.') :
                extensii_list.add(file[poz + 1:])
                break

    return sorted( extensii_list )


print ( extensii("C:/") )