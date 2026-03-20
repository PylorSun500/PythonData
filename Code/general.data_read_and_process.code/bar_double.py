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
plt.bar(x, y1, width=0.4, label = "产品A", tick_label = "tk")
plt.bar(x+0.4, y2, width=0.4, label = "产品B", yerr=[1, 1.5, 1.2, 1.2, 1.1])
plt.legend()
plt.ylim(0, 20)
plt.xlabel('产品说明')
plt.ylabel('产量')
plt.title('两组柱形图示例')

plt.show()