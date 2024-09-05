import time
import random
import matplotlib.pyplot as plt
from alg_HW1 import poly_multy
from nSquaredPolyMult import poly_mult

# GROUP: Ryan Kardoes, Dmitry Bezborodov
# fill up the test cases of polynomials with random ints. Incule every 100th degree poly
test_cases = []
for i in range(1, 10001, 100):
    a, b = random.sample(range(-10000, 10000), i), random.sample(range(-10000, 10000), i)
    test_cases.append((a, b))

# define n
n = [i for i in range(0, 10000, 100)]
times_reg = []
times_dc = []

# time the functions
for test in test_cases:

    start_reg = time.time()
    poly_mult(test[0], test[1])
    time_reg = time.time() - start_reg

    start_dc = time.time()
    poly_multy(test[0], test[1])
    time_dc = time.time() - start_dc

    times_reg.append(time_reg)
    times_dc.append(time_dc)

# plot and save the figure comparison between functions
plt.figure(figsize=(10, 6))
plt.plot(n, times_reg, label='Regular', marker='o')
plt.plot(n, times_dc, label='Divide $ Concur', marker='o')
plt.xlabel('n')
plt.ylabel('Time')
plt.title('Algorithm Comparison')
plt.legend()
plt.grid(True)
plt.savefig('plot2.png', format='png')







