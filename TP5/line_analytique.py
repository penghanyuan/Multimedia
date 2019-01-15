import numpy as np

def line_analytique(data, data_basic):
    c = []
    indice = []
    for i in range(0,943):
        for j in range(0, 1682):
            if data[i][j] !=-1:
                c.append(data[i][j])
                indice.append((i,j))


    c = np.array(c)
    print(c.size)
    A = np.zeros((c.size, 943+1682))

    print(c.size)
    for i in range(0, c.size):
        # print(data[i,:].size)
        # temp = np.delete(data_basic[i,:],fid)
        # print(temp.size)
        A[i] = np.append(data_basic[indice[i][0],:],data_basic[:,indice[i][1]].T)

    print(A.size)
    print(A)
    b = np.dot(np.dot(np.linalg.inv(np.dot(A.T,A)),A.T),c)
    print(b)