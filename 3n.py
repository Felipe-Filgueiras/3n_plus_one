import matplotlib.pyplot as plt
import numpy as np

def n_mais_um():
    num = input("Insira o número inicial: ")
    trigger = True
    num_list = []

    while trigger:
        num = int(num)
        num_list.append(num)
        if num == 1:
            trigger = False
            continue
        if (num % 2) == 0:
            num = num/2
        else:
            num = ((num*3)+1)

    print(num_list)
    return num_list

def graph_plot(number_list):
    list = number_list
    ypoints = np.array(list)
    xpoints = []
    tam = len(list)

    for i in range(tam):
        xpoints.append(i)

    plt.plot(xpoints, ypoints)

    for i, j in zip(xpoints, ypoints):
        plt.text(i, j+0.5, '{}'.format(j))
    plt.show()

graph_plot(n_mais_um())


