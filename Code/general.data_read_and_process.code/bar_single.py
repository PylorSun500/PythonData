import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import pandas as pd

fontpath = '/home/pylorsun/Documents/Study/2025-2026第二学期/PythonData/Assets/FontSources/CN_SA_寒蝉端黑体 v1.3/ChillDuanSansVF.ttf'
fm.fontManager.addfont(fontpath)
fontname = fm.FontProperties(fname=fontpath).get_name()
plt.rcParams['font.family'] = [fontname]
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(10, 6))
y = np.array([18, 12, 13, 8, 20])
x = np.arange(len(y))

tk = [chr(i) for i in range(97, 97+5)]
plt.bar(x, y, width=0.4, align='edge', label="产品A",tick_label=tk)

# for i in range(97, 97+5):
#     print(chr(i))

plt.legend()

plt.show()