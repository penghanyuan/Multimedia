import numpy as np

def readdata(file,nbuser,nbfilm):
    res=np.ones((nbuser, nbfilm))
    res = res*-1
    fichier = open(file, 'rU')
    lignes = fichier.readlines()

    for line in lignes :
        #print(line)
        lineSplit = line.split("\t")
        userid=int(lineSplit[0])-1
        filmid=int(lineSplit[1])-1
        score=int(lineSplit[2])
        # print(str(userid)+" "+str(filmid)+" "+str(score))
        res[userid,filmid]=score
    return res
    # lecture ligne a ligne

nbuser = 943
nbfilm = 1682
len = nbuser*nbfilm

def aler():
    scorealea=np.random.random()*5
    # print(scorealea)
    # print("scorealea :" + str(scorealea))

# def creatTargetsArray(data,nbuser,nbfilm):
#     res=numpy.ones((nbuser, nbfilm))
#     res = res*-1
#     for indexU in range(nbuser):
#         for indexF in range (ubfilm):
#             res[indexU, indexF]= data[index]


def creatPredictionsArray():
    res = np.random.randint(1,5,size=[nbuser,nbfilm])
    print("Matrice de notes aléatoires:",res)
    return res

def rmse(predictions, targets):
    print("Prédicteur_1_RMSE:",np.sqrt(np.mean((predictions - targets) ** 2)))



rmse(creatPredictionsArray(), readdata('./ml-100k/u.data',943,1682))
