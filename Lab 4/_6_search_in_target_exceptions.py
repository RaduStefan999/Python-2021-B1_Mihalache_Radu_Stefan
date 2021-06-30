import os

def search_in_target (target, to_search, callback) :

    files_containing = []
    
    if os.path.isfile(target) :

        data = open(target).read()
        if (data.count(to_search) != 0) : files_containing.append(target)

    elif os.path.isdir(target) :
        
        for (root, director, fisiere) in os.walk(target) :
            for fisier in fisiere :
                if os.path.isfile(os.path.join(root, fisier)) :
                    
                    data = open(os.path.join(root, fisier)).read()
                    if (data.count(to_search) != 0) : files_containing.append(os.path.join(root, fisier))
    else :
        callback( ValueError(target) )

    return files_containing


def handle_exception(err) :
    try :
        raise err
    except ValueError as e :
        print (e)

print (search_in_target("D:\work\\bd\Learning\Python\Lab 4", "def", handle_exception) )