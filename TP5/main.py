from TP5.tools import *
from TP5.basique import *
import time

res = readdata('./ml-100k/u.data',943,1682)
res = np.ma.masked_values(res, -1)

# res_temp = np.ones((943,1682))
# for uid in range(0, 943):
#     for fid in range(0, 1682):
#         if res[uid, fid] == -1:
#             res_temp[uid, fid] = 0
#         else:
#             res_temp[uid, fid] = res[uid, fid]
#
mean = res.mean()
#
# print(res_temp.shape)
# print(res_temp.size)

predictions = np.zeros((res.shape[0], res.shape[1]))
predictions = predictions*-1

for uid in range(0, 943):
    for fid in range(0, 1682):
        predictions[uid, fid] = predi_basique(res,uid,fid, mean)
    # print(uid)

print("mask")
predictions = np.ma.masked_values(predictions, -1)
# print(predictions)
print("rmse = : ")
print(rmse(predictions, res))