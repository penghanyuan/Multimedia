from TP5.tools import *
from TP5.basique import *
from TP5.line_analytique import *
from TP5.gradient import *
import time

res_ori = readdata('./ml-100k/u.data',943,1682)
res = np.ma.masked_values(res_ori, -1)

mean = res.mean()
#
# predictions = np.zeros((res.shape[0], res.shape[1]))
# predictions = predictions*-1
#
# for uid in range(0, 943):
#     for fid in range(0, 1682):
#         predictions[uid, fid] = predi_basique(res,uid,fid, mean)
#     # print(uid)

print("prediction_basic finished")
predictions = np.load("prediction_basic.npy")
print(predictions)
# np.save("prediction_basic.npy",predictions)
# print("rmse = : ")
# print(rmse(predictions, res))

# line_analytique(res_ori, predictions)
alpha = 0.00000003
# gradient(alpha, 10000, res_ori, predictions, 100)


test_mkc = make_c(res_ori, 120)
test_A = make_A(np.array(test_mkc[0]),test_mkc[1],predictions)
test_c = test_mkc[0][1764:]

test_c = np.array(test_c)
test_A = np.matrix(test_A[1764:])


print(test_c.size)
b = np.load("b_value.npy")
predict_gradient = np.dot(test_A,b)[:,0]
predict_gradient_array = np.squeeze(np.asarray(predict_gradient[:,0]))
# print(test_c)
print(rmse(predict_gradient_array, test_c))
# test = np.append(data_basic[indice[i][0], :], data_basic[:, indice[i][1]].T)
