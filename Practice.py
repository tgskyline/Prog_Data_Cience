import numpy as np
import pandas as pd



# series = [[23,45,12,679], [14,48,69,38]]
# new_series = np.array(series)
# print(new_series.ndim)
# print(new_series.shape)


# a= np.ones(10) + 4

# a = np.ones(10) * 4

# a = np.full(10, 4)

# a = np.zeros(10) * 4

# print(a)

# import numpy as np
# dataset = np.array(['paul', 'jacob', 'vince', 'paul', 'miky', 'larence', 'warren'])
# print(dataset == 'paul')

# import numpy as np

# percentiles = [98, 76.37, 55.55, 69, 88]
# first_subject = np.array(percentiles)
# print(first_subject.dtype.name)

# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# # arr[-2::-2] = -1

# # arr[arr % 2 == 0] = -1

# # arr[::2] = -1

# arr[1::2] = -1

# print (arr)


# arr = np.eye(5)

# print(arr)

# # arr = arr - (np.eye(5) + 1)

# # arr = np.full((5x5),-1)

# arr[arr != 1] = -1

# # arr[arr == 0] = -1

# print(arr)


# nomes = ("Minas Gerais", "Amazonas", "Maranhão", "Goiás", "Santa Catarina")
# siglas = ("MG", "AM", "MA", "GO", "SC")
# estados = pd.Series(siglas, nomes)
# print(estados)

# X = [3, 6, 1, 9, 2, 4, 7]
# print(X)
# print(X[::-1])
# print(X[-1::-1])
# print(X[:0:-1])
# print(X[6::-1])
# print(X[6:0:-1])

# A = [9, 2, 5, 7]
# B = [x for x in range(12,21,3)]

# print(B)
# A.append(B)
# print(A)


# estrutura_aninhada = ( [1,2,3],(4,5,6,7),[8,9],( [10,11,12], [(13, 14), 15] ) )
# print(estrutura_aninhada[3][1][0][0])

# dic = { "MG": {"Capital": "Belo Horizonte", 
#                "Cidades": {1:"Contagem", 
#                            2:"Luiz de Fora", 
#                            3:"Sete Lagoas"}
#               },
#         "SP": {"Capital": "São Paulo", 
#                "Cidades": {1:"Campinas", 
#                            2:"Piracicaba",
#                            3:"Franca"}
#               },
#         "RS": {"Capital": "Porto Alegre", 
#                "Cidades": {1:"Pelotas", 
#                            2:"Gramado", 
#                            3:"Canela"}
#               } 
#       }
# dic["MG"]["Cidades"][2] = "Juiz De Fora"
# print(dic['MG']['Cidades'][2])

# n = '5'
# print(type(n))


# x = range(7)
# soma = sum(filter(lambda x_i: x_i % 2 == 0, x))
# print(soma)

# def func():
#     x = 1
#     print(x)

# x = 10
# func()
# print(x)

# from functools import reduce
# teste = [1, 9, 8, 2, 3, 7, 6, 4, 5]
# print(reduce(lambda n1, n2: n1 if n1 > n2 else n2, teste))

import numpy as np
A = np.arange(1, 16).reshape(3,5)

print (A)

# linha1 = A[1,:]
# linha1 = A[1]
# linha1 = A[1:2,:][0]
# linha1 = A[1,0:]

linha1 = A[:][1]


print(linha1)