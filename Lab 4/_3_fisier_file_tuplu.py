import os

def fisier_file(my_path) :
    if os.path.isfile (my_path) :
        input_file = open(my_path, "r")
        data = input_file.read()

        return data[-20:]
    
    elif os.path.isdir (my_path) :
        extensions_dict = dict([])

        for (root, director, files) in os.walk(my_path) :
            for file in files :
                for poz in range(len(file) - 1, 0, -1) :
                    if (file[poz] == '.') :
                        
                        if (file[poz:] in extensions_dict) == False :
                            extensions_dict[file[poz:]] = 1
                        else :
                            extensions_dict[file[poz:]] += 1
                        break
        
        return extensions_dict



print ( fisier_file("D:\work\\bd\Learning\Python\Lab 4") )