def compare_dictionar (A, B) :
    
    if ((type(A) is dict and type(B) is dict) == False) :
        return A is B

    if len(A) != len(B):
        return False
    
    is_equal = True
    for key in A :
        if key in B :
            is_equal = is_equal and compare_dictionar(A[key], B[key])
        else :
            return False

    return is_equal



A = {"A" : 11, "B" : 28, "C" : {"D" : 11, "E" : 12}}
B = {"A" : 11,  "B" : 28, "C" : {"D" : 11, "E" : 12}}

#print (A is B)
print (compare_dictionar(A, B))
