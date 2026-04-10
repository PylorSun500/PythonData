from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.cbook import boxplot_stats

x = np.arange(10, 64)
y = np.arange(10, 64)
data = [x, y]

bp = boxplot_stats(data)

plt.boxplot(data, patch_artist=True, widths=0.3)
j = 1
for i in bp:
    plt.text(j, i['whislo'], i['whislo'])
    plt.text(j, i['q1'], i['q1'])
    plt.text(j, i['q3'], i['q3'])
    j = j + 1
    
plt.show()