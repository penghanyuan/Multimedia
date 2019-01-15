import numpy as np

def make_c(data, numData):
    c = []
    indice = []
    for i in range(0, numData):
        for j in range(0, numData):
            if data[i][j] != -1:
                c.append(data[i][j])
                indice.append((i, j))
    return (c, indice)

def make_A(c, indice, data_basic):
    A = np.zeros((c.size, 943 + 1682))
    for i in range(0, c.size):
        A[i] = np.append(data_basic[indice[i][0], :], data_basic[:, indice[i][1]].T)
    return A

def gradient(alpha, iter, data, data_basic, numData):
    mkc = make_c(data,numData)
    c = np.array(mkc[0])
    print(c.size)
    indice = mkc[1]

    A = make_A(c, indice, data_basic)

    b = np.zeros((943 + 1682,1))
    A = np.matrix(A)
    b = np.matrix(b)
    c = np.matrix(c)
    lam = np.dot(A.T, c.T)
    gra = 0
    t = 0
    while t < iter:
        # c_predit = np.dot(A,b)
        print(t)

        # print("b value before ")
        # print(b)
        # print("b size ")
        # print(b.size)
        gra = (np.dot(np.dot(A.T, A),b) - lam)
        b = b - alpha * gra
        # print("b value after")
        # print(b)
        # print("b size ")
        # print(b.size)
        print("gradient")
        print(gra)
        # print("size gra")
        # print(gra.size)
        t = t+1
        # print(t)
    print("gradient")
    print(gra)
    print("b value")
    print(b)
    np.save("b_value.npy",b)
    return b