#Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

import pandas as pd
import random

lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создание one-hot представления
unique_labels = data['whoAmI'].unique()
one_hot = pd.DataFrame(0, columns=unique_labels, index=data.index)
for label in unique_labels:
    one_hot[label] = (data['whoAmI'] == label).astype(int)

# Объединение исходного DataFrame с one-hot представлением
data = pd.concat([data, one_hot], axis=1)
data = data.drop('whoAmI', axis=1)

data.head()


