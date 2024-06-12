"""
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?


"""


import random as rd
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
rd.shuffle(lst)
# print(lst)

data = pd.DataFrame({'whoAmI':lst})
data.head()
# print(data)

# data = pd.get_dummies(data['whoAmI'])

# print(data)

unique_name = []
for name in lst:
    if name not in unique_name:
        unique_name.append(name)
    
# print(unique_name)

result = pd.DataFrame()


for name in unique_name:
    result[name] = (data['whoAmI'] == name)

# print(result)

result = result.astype(int)
print(result)