import numpy as np
import threading
import random

lock = threading.Lock()

#TOTAL_FILES = 30367
TRIANING_FILES = 27367
VALIDATION_FILES = 3000


def load_files(data, initial, final):
    for i in range(initial, final):
        fo = open('../data/ida-solutions/sol_ida_problem_'+str(i)+'_.txt')
        for l in fo.readlines():
            data.append(l)
        fo.close()
    random.shuffle(data)
    return data


def load_data(batch_size, data):
    lock.acquire()
    x_train, y_train = None, None
    for _ in range(batch_size):
        if len(data) < 2:
            print('CARGANDO DATOS OTRA VEZ!')
            data = load_files(data, 0, TRIANING_FILES)

        line = data.pop()
        solution = line[-5:]  # last 4 chars
        line = line[:-5]  # all line except the solution
        line = line.replace(" ", "")
        x_sample = np.array([list(line)]).astype('f')
        y_sample = np.array([list(solution.rstrip())]).astype('f')

        if x_train is None:
            x_train, y_train = x_sample, y_sample
        else:
            x_train = np.append(x_train, x_sample, axis=0)
            y_train = np.append(y_train, y_sample, axis=0)
    lock.release()
    return x_train, y_train


def load_data_e(batch_size, data):
    lock.acquire()
    x_train, y_train = None, None
    for _ in range(batch_size):
        line = random.choice(data)
        solution = line[-5:]  # last 4 chars
        line = line[:-5]  # all line except the solution
        line = line.replace(" ", "")
        x_sample = np.array([list(line)]).astype('f')
        y_sample = np.array([list(solution.rstrip())]).astype('f')

        if x_train is None:
            x_train, y_train = x_sample, y_sample
        else:
            x_train = np.append(x_train, x_sample, axis=0)
            y_train = np.append(y_train, y_sample, axis=0)
    lock.release()
    return x_train, y_train
