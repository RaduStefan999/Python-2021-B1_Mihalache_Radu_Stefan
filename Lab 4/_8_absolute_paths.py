import os

def absolute_paths (root_path) :

    absolute_paths_list = []

    for file in os.listdir(root_path) :
        if os.path.isfile(file) :
            absolute_paths_list.append(os.path.abspath( os.path.join(root_path, file) ) ) 

    return absolute_paths_list

print ( absolute_paths("D:\work\\bd\Learning\Python\Lab 4") )