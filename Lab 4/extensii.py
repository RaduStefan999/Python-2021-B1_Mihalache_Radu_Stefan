import os

def extensii (director) :
    return os.listdir(director)

print ( extensii("C:/") )