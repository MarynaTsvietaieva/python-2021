# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from numpy import arange

def approximate_sqrt2(n):
    estimates = list()
    for i in range(0,n):
        x = ((4*i + 2)**2)/((4*i + 1)*(4*i + 3))
        if(i != 0) : x = x*estimates[-1]
        estimates.append(x);
    return estimates


def plot_estimates(estimates):
    X = arange(1, len(estimates)+1)
    plt.semilogx(X, estimates)
    plt.xlabel("Number of points")
    plt.ylabel("Estimates of √2")
    plt.title("Final estimate of √2: {}".format(estimates[-1]))
    plt.axhline(1.4142, color='green')

    plt.show()


if __name__ == '__main__':
    # used for tests, do not change
    n = 20
    estimates = approximate_sqrt2(n)
    print(estimates)
    plot_estimates(estimates)