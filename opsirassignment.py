import numpy as np

def solver2(M) :

    M[2] = M[2] - M[2,0] * M[0] 
    M[2] = M[2] - M[2,1] * M[1]

    if M[2,2] == 0 :
        M[2] = M[2] + M[3]
        M[2] = M[2] - M[2,0] * M[0]
        M[2] = M[2] - M[2,1] * M[1]

    if M[2,2] == 0 :
        print("Bruh")

    M[2] = M[2] / M[2,2]

    return M

def solver3(M) :

    M[3] = M[3] - M[3,0] * M[0] 
    M[3] = M[3] - M[3,1] * M[1] 
    M[3] = M[3] - M[3,2] * M[2]    

    if M[3,3] == 0:
        print("Bruh")


    M[3] = M[3] / M[3,3]

    return M

M = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 1, 2, 3],
        [4, 5, 6, 7]
    ], dtype=np.float_)

solver2(M)
print("")
print("Row Two:")
print(M)

solver3(M)
print("")
print("Row Three:")
print(M)
