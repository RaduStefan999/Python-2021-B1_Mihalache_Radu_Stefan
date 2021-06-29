import os
import sys

dictionar_extensii = dict([])

for file in os.listdir( sys.argv[1] ) :
    
    if os.path.isfile(file) :
        for poz in range( len(file) - 1, 0, -1) :
            
            
            if (file[poz] == '.') :
                if (file[poz:] in dictionar_extensii) == False :
                    dictionar_extensii[file[poz:]] = 1
                else :
                    dictionar_extensii[file[poz:]]  += 1
                break

print (dictionar_extensii)

