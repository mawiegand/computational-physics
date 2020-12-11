import argparse
import numpy as np
import matplotlib.pyplot as plt
import functions

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    "--lower_bound",
    "-l",
    type=float,
    default=-20.0,
    help="Lower bound of X-Axis (float)",
)
parser.add_argument(
    "--upper_bound",
    "-u",
    type=float,
    default=20.0,
    help="Upper bound of X-Axis (float)",
)
parser.add_argument(
    "--step_size",
    "-s",
    type=float,
    default=0.001,
    help="Step size of X-Axis values (float)",
)
parser.add_argument(
    "--delta_h", "-d", type=float, default=0.1, help="h-method value (float)"
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
x_values = np.arange(args.lower_bound, args.upper_bound, args.step_size)
y_derived = []
y_approx = []
orig_function = functions.dispatcher[args.function]
derived_function = functions.derivation_dispatcher[f"{args.function}_diff"]

# caclulate function values
for x in x_values:
    y_approx.append(functions.approx_diff(orig_function, x, args.delta_h))
    y_derived.append(derived_function(x))

# plot calculated function values
plt.plot(x_values, y_approx, label=f"{args.function}_h'(x)")
plt.plot(x_values, y_derived, label=f"{args.function}'(x)")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.show()
