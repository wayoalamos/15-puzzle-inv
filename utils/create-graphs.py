import matplotlib.pyplot as plt
import numpy as np
np.random.seed(1)

data = {
    "NN": [3992, 13744573],
    "WIDA-1": [3814, 4161977750],
    "WIDA-1.2": [3850, 3396879619],
    "WIDA-1.3": [3914, 2952287168],
    # "wida 1.35": [3946, 2882884064],
    # "wida 1.38": [3962, 2159673028],
    "WIDA-1.39": [3966, 1958066775],
    # "wida 1.398": [3966, 1958797819],
    "WIDA-1.4": [3980, 312341955],
    "WIDA-1.5": [4072, 132259329],
    "WIDA-1.6": [4188, 152999758],
    "WIDA-2": [4964, 132259329]
}

length = [data[i][0] for i in data]
expansions = [data[i][1] for i in data]
names = [i for i in data.keys()]
fig, ax = plt.subplots()
ax.scatter(length, expansions)

for i in data:
    ax.annotate(i, (data[i][0], data[i][1]))

plt.xlabel("largo de la soluciones")
plt.ylabel("expansions realizadas")
plt.show()


def plot_bar_x():
    # this is for plotting purpose
    index = np.arange(len(names))
    plt.xlabel('Algoritmos', fontsize=5)
    plt.ylabel('Optimalidad', fontsize=5)
    plt.xticks(index, names, fontsize=15, rotation=30)
    plt.title('Optimalidad (largo/largo optimo)')
    plt.show()

# plot_bar_x()
