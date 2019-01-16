import numpy as np
from TP5.tools import *
# from tp5.basique import *


#----------------- Preparations ------------------
print("----Quelques chiffres importants dans predi_voisinage:----")
print("reducing the number of element by 6")
nbuser=int(943/6)
nbfilm=int(1682/6)
L = 10
matrice = readdata('./ml-100k/u.data', 943, 1682)
res=matrice[0:nbuser,0:nbfilm]

#-------------------- Tools ------------------------

def calculMean(data):
    total = 0
    nb = 0
    for val in data:
        if(val != -1):
            total += val
            nb = nb + 1

    return total/nb


def readdata(file,nbuser,nbfilm):
    res=np.ones((nbuser, nbfilm))
    res = res*-1
    fichier = open(file, 'rU')
    lignes = fichier.readlines()

    for line in lignes :
        lineSplit = line.split("\t")
        userid=int(lineSplit[0])-1
        filmid=int(lineSplit[1])-1
        score=int(lineSplit[2])
        res[userid,filmid]=score
    return res

def predi_basique(data, uid, fid , r_):

    bu = calculMean(data[uid,:]) - r_
    bi = calculMean(data[:,fid]) - r_
    res = r_ + bu + bi
    return res

def calculTotal(res,nbuser,nbfilm):
    total = 0
    for i in range(0,nbuser):
        for j in range(0,nbfilm):
            val=res[i,j]
            if(val != -1):
                total += val
    return total

def computenbvote(res,nbuser,nbfilm):
    nbvote=0
    for i in range(0,nbuser):
        for j in range(0,nbfilm):
            val=res[i,j]
            if(val != -1):
                nbvote=nbvote+1
    return nbvote

#-------------------- Predicteur ------------------------

# print qqc
# données réduites
nbscore=computenbvote(res,nbuser,nbfilm)
print("note",nbscore)
print("res_length", len(res))
print("res_width", len(res[0]))
mean = calculTotal(res,nbuser,nbfilm)/computenbvote(res,nbuser,nbfilm)
print("mean:",mean)
print("----------------------------------------------------------")




def creatR():
    R = np.ones((nbuser, nbfilm))
    R = R*-1

    for u in range(0,nbuser):
        for i in range(0,nbfilm):
            R[u][i] = res[u][i] - predi_basique(res, u, i, mean)

    return R


# Matrice similarite S
def calculS(R, res):
    S = np.ones((nbfilm, nbfilm))
    S = S * -1

    for i in range(0,nbfilm):
        for j in range(0,nbfilm):
            somme_R = np.sum( R[:,i] * R[:,j], axis=0 ) #分子
            somme_Res = np.sqrt((np.sum(R[:,i]*R[:,i]) * np.sum(R[:,j]*R[:,j]))) #分母
            S[i][j] = somme_R / somme_Res
    return S


#les L premiers apres mette en ordre les similarites
def ordreDecroi_L(matrice_similarite, i, L):

    similarite_i = matrice_similarite[i]  #par ligne ou colonne tout marche
    tuple=sorted(enumerate(similarite_i), key=lambda x: x[1])
    tuple.reverse()
    similarite_i_ordre_decroi_preL = tuple[0: L+1]  #doit enlever soi meme
    Li = similarite_i_ordre_decroi_preL
    return Li

def predi_voisinage():
    new_R = np.ones((nbuser, nbfilm))
    new_R = new_R*-1
    R = creatR()
    S = calculS(R, res)

    for u in range(0,nbuser):
        for i in range(0,nbfilm):
            somme_up = 0
            somme_down = 0
            Li = ordreDecroi_L(S, i, 10)
            for index in range(0, 10):
                j = Li[index][0]
                somme_up += S[i][j]* R[u][j]
                somme_down += np.abs(S[i][j])
            new_R[u][i] = predi_basique(res, u, i, mean) + somme_up/somme_down
    return new_R


def rmse_voisinage(predictions, targets):
    return np.sqrt(np.mean((predictions - targets) ** 2))



# print("rmse = : ")
# print("R:", creatR())
# calculS(creatR(),res)
# print("S:", calculS(creatR(), res))
# calculSimilarite(creatR(),res)
# print("S:", calculSimilarite(creatR(), res))
# print("Li:", ordreDecroi_L(calculS(creatR(),res), 1, 10))

def predi_voisinage_main():
# print("Prédicteur_voisinage_RMSE:", rmse_voisinage(predi_voisinage(), res))
    return rmse_voisinage(predi_voisinage(), res)

