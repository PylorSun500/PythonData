import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import pandas as pd

fontpath = '/home/pylorsun/Documents/Study/2025-2026第二学期/PythonData/Assets/FontSources/CN_SA_寒蝉端黑体 v1.3/ChillDuanSansVF.ttf'
fm.fontManager.addfont(fontpath)
fontname = fm.FontProperties(fname=fontpath).get_name()
plt.rcParams['font.family'] = [fontname]
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(-np.pi, np.pi, 1000)
ysinx = np.sin(x)
ycosx = np.cos(x)
plt.plot(x, ysinx, x, ycosx)
plt.legend(['正弦曲线', '余弦曲线'])
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])
plt.show()