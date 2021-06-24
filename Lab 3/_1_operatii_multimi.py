def set_operations(A, B) :
    A_intersectat_B = A.intersection(B)
    A_reunit_B = A.union(B)
    A_minus_B = A.difference(B)
    B_minus_A = B.difference(A)
    
    return (A_intersectat_B, A_reunit_B, A_minus_B, B_minus_A)

A = set([10, 7, 6, 98, 50, 30, 45, 67])
B = set([67, 60, 10, 12, 7])

X,Y,Z,T = set_operations(A, B)

print(X)
print(Y)
print(Z)
print(T)