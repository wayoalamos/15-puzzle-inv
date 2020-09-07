import matplotlib.pyplot as plt
import numpy as np
np.random.seed(1)

examples = [0,
            1000*300,
            1500*300,
            2000*300,
            2500*300,
            3000*300,
            3500*300,
            4000*300,
            4500*300]
results = [
    0.25,
    0.7858,
    0.8212,
    0.8409,
    0.8529,
    0.8637,
    0.8708,
    0.8763,
    0.8809]


fig, ax = plt.subplots()
ax.scatter(examples, results)

# for i in examples:
#     ax.annotate(i, (data[i][0], data[i][1]))

plt.xlabel("Cantidad de ejercicios utilizados")
plt.ylabel("Exactitud de prediccion de la red neuronal")
# plt.show()
plt.savefig("graph4.png", dpi=300)


# plot_bar_x()
