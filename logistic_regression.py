import numpy as np
from sklearn.linear_model import LogisticRegression
import os

accuracy = []

def pred(PACIENT, folder):
    model = LogisticRegression()
    y = []
    arrays = []
    # считываем каждую матрицу
    for i in range(1, len(folder)):
        if PACIENT + '/' in folder[i][0] + '/':
            continue
        for j in range(len(folder[i][2])):
            name = folder[i][0] + '/' + folder[i][2][j]
            with open(name, 'r') as file:
                matrix = []
                for k in file:
                    string = k.split()
                    matrix.append([float(k) for k in string])
                arrays.append(np.linalg.norm(np.array(matrix))) #норма
                if "LA_" in name:
                    y.append('LA')
                else:
                    y.append('HA')
    arrays = np.array(arrays).reshape(-1, 1)
    model.fit(arrays, y)
    checkx = []
    checky = []
    for i in range(1, len(folder)):
      if PACIENT + '/' in folder[i][0] + '/':
        for j in range(len(folder[i][2])):
            name = folder[i][0] + '/' + folder[i][2][j]
            with open(name, 'r') as file:
                matrix = []
                for k in file:
                    string = k.split()
                    matrix.append([float(k) for k in string])
                checkx.append(np.linalg.norm(np.array(matrix)))
                if "LA_" in name:
                    checky.append('LA')
                else:
                    checky.append('HA')
    checkx = np.array(checkx).reshape(-1, 1)
    prediction = model.predict(checkx)

    #считаем ошибки
    errors = 0
    amount = len(prediction)
    for i in range(amount):
        if prediction[i] != checky[i]:
            errors += 1
    accuracy.append((amount-errors)/amount)

#получаем список всех папок и файлов в них
folder = []
for i in os.walk("/home/alisa/ForMachineLearning"):
    folder.append(i)

#выбираем тестовые данные
for name in folder[0][1]:
    pred(name, folder)

print(max(accuracy))