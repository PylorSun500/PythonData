import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import numpy as np
import pandas as pd

fontpath = '/home/pylorsun/Documents/Study/2025-2026第二学期/PythonData/Assets/FontSources/CN_SA_寒蝉端黑体 v1.3/ChillDuanSansVF.ttf'
fm.fontManager.addfont(fontpath)
fontname = fm.FontProperties(fname=fontpath).get_name()
plt.rcParams['font.family'] = [fontname]
plt.rcParams['axes.unicode_minus'] = False

y1 = np.array([12, 5, 15, 10, 6])
y2 = [6, 8, 16, 11, 7]
x = np.arange(len(y1))
tk = [chr(i) for i in range(97, 97+5)]
bar_width = 0.4
bar0A = plt.bar(x, y1, width=0.4, label = "产品A", tick_label = "tk")
bar0B = plt.bar(x, y2, width=0.4, label = "产品B",bottom=y1)
for bA, bB in zip(bar0A, bar0B):
    plt.text(bA.get_x() + bar_width/3, bA.get_height(), bA.get_height())
    plt.text(bA.get_x() + bar_width/3, bB.get_height() + bA.get_height(), bB.get_height())
plt.legend()
plt.xlabel('产品说明')
plt.ylabel('产量')
plt.title('两组柱形图示例')

plt.show()