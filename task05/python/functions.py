import numpy as np


def f(x):
    return np.exp(-x / 2) * np.cos(2 * x)


def f_diff(x):
    return (-1 / 2) * np.exp(-x / 2) * (4 * np.sin(2 * x) + np.cos(2 * x))


def g(x):
    return np.exp(-1 / 2 * x) * np.sin(x)


def g_diff(x):
    return (1 / 2) * np.exp(-x / 2) * (2 * np.cos(x) - np.sin(x))


def h(x):
    return np.exp(-1 / x ** 2) * np.sin(0.2 * x ** 2)


def h_diff(x):
    return (
        np.exp(-1 / x ** 2)
        * (2 * np.sin(0.2 * x ** 2) + 0.4 * x ** 4 * np.cos(0.2 * x ** 2))
    ) / x ** 3


def approx_diff(func, x, h):
    return (func(x + h) - func(x - h)) / (2 * h)


# prepare function dispatcher
dispatcher = {"f": f, "g": g, "h": h}
derivation_dispatcher = {"f_diff": f_diff, "g_diff": g_diff, "h_diff": h_diff}
