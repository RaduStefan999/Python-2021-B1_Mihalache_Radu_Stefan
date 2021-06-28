def my_function(*positionals, **keys) :
    nr = 0
    
    for key in keys :
        if (positionals.count(keys[key]) != 0) : nr = nr + 1

    return nr 

print ( my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5) )