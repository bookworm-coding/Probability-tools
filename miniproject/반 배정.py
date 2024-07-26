from fractions import Fraction
from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np


def moment(var_list, k):
	num = len(var_list)
	return sum([j ** k for j in var_list]) / num


list_all = []
for _ in range(10000):
	case = np.random.randint(low=1, high=13, size=30)
	list_class = [0 for _ in range(13)]

	for i in case:
		list_class[i - 1] += 1

	list_all.append(list_class[0])

plt.hist(list_all, rwidth=0.8, color="skyblue")
plt.show()

print(moment(list_all, 1), moment(list_all, 2), moment(list_all, 3))

