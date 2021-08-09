import os

def pred(PACIENT, folder):
    main_list = {}
    test_list = {}
    for i in range(1, 4):
        for j in range(5):
            for k in range(7):
                index = (i, j, k)
                main_list[index] = []
                test_list[index] = []
    y = []
    testy = []
    # считываем каждую матрицу
    for i in range(1, len(folder)):
        if PACIENT + '/' in folder[i][0] + '/':
            for j in range(1, 3):
                testy.append('LA')
                name = folder[i][0] + '/LA_1_' + str(j) + '.dat'
                with open(name, 'r') as file:
                    matrix = []
                    for k in file:
                        string = k.split()
                        matrix.append([float(k) for k in string])
                    for k in range(len(matrix)):
                        for n in range(len(matrix[k])):
                            test_list[(1, n, k)].append(matrix[k][n])
                name = folder[i][0] + '/LA_2_' + str(j) + '.dat'
                with open(name, 'r') as file:
                    matrix = []
                    for k in file:
                        string = k.split()
                        matrix.append([float(k) for k in string])
                    for k in range(len(matrix)):
                        for n in range(len(matrix[k])):
                            test_list[(2, n, k)].append(matrix[k][n])
                name = folder[i][0] + '/LA_3_' + str(j) + '.dat'
                with open(name, 'r') as file:
                    matrix = []
                    for k in file:
                        string = k.split()
                        matrix.append([float(k) for k in string])
                    for k in range(len(matrix)):
                        for n in range(len(matrix[k])):
                            test_list[(3, n, k)].append(matrix[k][n])
                testy.append('HA')
                name = folder[i][0] + '/HA_1_' + str(j) + '.dat'
                with open(name, 'r') as file:
                    matrix = []
                    for k in file:
                        string = k.split()
                        matrix.append([float(k) for k in string])
                    for k in range(len(matrix)):
                        for n in range(len(matrix[k])):
                            test_list[(1, n, k)].append(matrix[k][n])
                name = folder[i][0] + '/HA_2_' + str(j) + '.dat'
                with open(name, 'r') as file:
                    matrix = []
                    for k in file:
                        string = k.split()
                        matrix.append([float(k) for k in string])
                    for k in range(len(matrix)):
                        for n in range(len(matrix[k])):
                            test_list[(2, n, k)].append(matrix[k][n])
                name = folder[i][0] + '/HA_3_' + str(j) + '.dat'
                with open(name, 'r') as file:
                    matrix = []
                    for k in file:
                        string = k.split()
                        matrix.append([float(k) for k in string])
                    for k in range(len(matrix)):
                        for n in range(len(matrix[k])):
                            test_list[(3, n, k)].append(matrix[k][n])
            continue
        for j in range(1, 3):
            y.append('LA')
            name = folder[i][0] + '/LA_1_' + str(j) + '.dat'
            with open(name, 'r') as file:
                matrix = []
                for k in file:
                    string = k.split()
                    matrix.append([float(k) for k in string])
                for k in range(len(matrix)):
                    for n in range(len(matrix[k])):
                        main_list[(1, n, k)].append(matrix[k][n])
            name = folder[i][0] + '/LA_2_' + str(j) + '.dat'
            with open(name, 'r') as file:
                matrix = []
                for k in file:
                    string = k.split()
                    matrix.append([float(k) for k in string])
                for k in range(len(matrix)):
                    for n in range(len(matrix[k])):
                        main_list[(2, n, k)].append(matrix[k][n])
            name = folder[i][0] + '/LA_3_' + str(j) + '.dat'
            with open(name, 'r') as file:
                matrix = []
                for k in file:
                    string = k.split()
                    matrix.append([float(k) for k in string])
                for k in range(len(matrix)):
                    for n in range(len(matrix[k])):
                        main_list[(3, n, k)].append(matrix[k][n])
            y.append('HA')
            name = folder[i][0] + '/HA_1_' + str(j) + '.dat'
            with open(name, 'r') as file:
                matrix = []
                for k in file:
                    string = k.split()
                    matrix.append([float(k) for k in string])
                for k in range(len(matrix)):
                    for n in range(len(matrix[k])):
                        main_list[(1, n, k)].append(matrix[k][n])
            name = folder[i][0] + '/HA_2_' + str(j) + '.dat'
            with open(name, 'r') as file:
                matrix = []
                for k in file:
                    string = k.split()
                    matrix.append([float(k) for k in string])
                for k in range(len(matrix)):
                    for n in range(len(matrix[k])):
                        main_list[(2, n, k)].append(matrix[k][n])
            name = folder[i][0] + '/HA_3_' + str(j) + '.dat'
            with open(name, 'r') as file:
                matrix = []
                for k in file:
                    string = k.split()
                    matrix.append([float(k) for k in string])
                for k in range(len(matrix)):
                    for n in range(len(matrix[k])):
                        main_list[(3, n, k)].append(matrix[k][n])

    unwanted = []
    # приводим данные к нужной форме
    for key in main_list.keys():
        if len(set(main_list[key])) > 1:
            # main_list[key] = np.array(main_list[key]).reshape(-1, 1)
            continue
        else:
            unwanted.append(key)
    for i in range(len(unwanted)):
        main_list.pop(unwanted[i])
        test_list.pop(unwanted[i])

   #находим вектора разниц
    predict = []
    for i in range(4):
        for key in test_list.keys():
            diff = []
            for j in range(len(main_list[key])):
                if main_list[key][j] > test_list[key][i] and main_list[key][j] >= 0:
                    diff.append(main_list[key][j] - test_list[key][i])
                elif test_list[key][i] >= main_list[key][j] and test_list[key][i] >= 0:
                    diff.append(test_list[key][i] - main_list[key][j])
                else:
                    if main_list[key][j] > test_list[key][i]:
                        diff.append(test_list[key][i] - main_list[key][j])
                    else:
                        diff.append(main_list[key][j] - test_list[key][i])
            mini = [9999, 0.1]
            for j in range(len(diff)):
                if diff[j] < mini[0]:
                    mini = [diff[j], j]
            predict.append(y[mini[1]]==testy[i])
    print(predict.count(True)/len(predict))

# получаем список всех папок и файлов в них
folder = []
for i in os.walk("/home/alisa/ForMachineLearning"):
    folder.append(i)

# выбираем тестовые данные
for name in folder[0][1]:
    pred(name, folder)