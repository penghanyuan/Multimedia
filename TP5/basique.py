import numpy as np


def predi_basique(data, uid, fid , r_):
    # print(data[uid,:])
    bu = data[uid,:].mean() - r_
    bi = data[:,fid].mean() - r_
    res = r_ + bu + bi
    return res
