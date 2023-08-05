import os
import numpy as np

alphas_s = np.linspace(0.1, 1.0, 5)
l1_ratios = np.linspace(0.1, 1.0, 5)



for alpha in alphas_s:
    for l1 in l1_ratios:
        os.system(f"python simple_model3.py -a {alpha} -r {l1}")
        