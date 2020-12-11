import argparse
import numpy as np
import matplotlib.pyplot as plt
import functions


def error_func(a, h):
    return a * h ** 2


# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    "--x_value", "-x", type=float, default=-9.0, help="Value of X-Axis (float)"
)
parser.add_argument(
    "--lower_bound",
    "-l",
    type=float,
    default=0.001,
    help="Lower bound of h-method values (float)",
)
parser.add_argument(
    "--upper_bound",
    "-u",
    type=float,
    default=1.0,
    help="Upper bound of h-method values (float)",
)
parser.add_argument(
    "--step_size",
    "-s",
    type=float,
    default=0.1,
    help="Step size of h-method value (float)",
)
parser.add_argument(
    "--function",
    "-f",
    type=str,
    choices=functions.dispatcher.keys(),
    default="f",
    help="Name of function (str)",
)
args = parser.parse_args()

# initialize environment
h_delta_values = np.arange(args.lower_bound, args.upper_bound, args.step_size)
h_values = np.linspace(args.lower_bound, args.upper_bound, 10000)
orig_function = functions.dispatcher[args.function]
derived_function = functions.derivation_dispatcher[f"{args.function}_diff"]
y = []

# caclulate function values
for delta_h in h_delta_values:
    y.append(
        functions.approx_diff(orig_function, args.x_value, delta_h)
        - derived_function(args.x_value)
    )

# calculate parabola error fit function
parabolic_fit = np.polyfit(h_delta_values, y, 2)
error = np.poly1d(parabolic_fit)

# plot functions
plt.scatter(
    h_delta_values,
    y,
    label=f"{args.function}_h'({args.x_value}) - {args.function}'({args.x_value})",
)
plt.plot(
    h_values, error(h_values), label=f"error(h) = {parabolic_fit[0]:.2f} * h^2"
)
plt.xlabel("h-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.show()
