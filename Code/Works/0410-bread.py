from matplotlib import pyplot as plt
from matplotlib import font_manager as fm


fontpath = '/home/pylorsun/Documents/Study/2025-2026第二学期/PythonData/Assets/FontSources/CN_SA_寒蝉端黑体 v1.3/ChillDuanSansVF.ttf'
fm.fontManager.addfont(fontpath)
fontname = fm.FontProperties(fname = fontpath).get_name()

plt.rcParams['font.family'] = [fontname]
plt.rcParams['axes.unicode_minus'] = False

x = [250, 150, 4, 250, 50, 30, 4, 20]
pie_labels = ['面粉', '全麦粉', '酵母', '苹果酱', '鸡蛋', '黄油', '盐', '白糖']
explode = [0.1] * 8
plt.pie(x, labels=pie_labels, autopct='%3.1f%%', wedgeprops={'width': 0.6} ,pctdistance=0.5, explode=explode, shadow=True)
plt.legend(loc='upper right', bbox_to_anchor = [1.05, 1.1], ncol = 2, title = '图例')

plt.show()