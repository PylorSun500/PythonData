import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot as plt
import numpy as np
from matplotlib import font_manager
fontpath = '/Users/pylorsun/Documents/Study/2025-2026第二学期/PythonData/Assets/FontSourcesMacOS/CN_SA_寒蝉端黑体 v1.3/ChillDuanSansVF.ttf'
font_manager.fontManager.addfont(fontpath)
fontname = font_manager.FontProperties(fname = fontpath).get_name()
plt.rcParams['font.family'] = [fontname]
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 从CSV文件读取数据，通过表头名称引用各列
csv_path = './Code/Works/tempanddropfall/data.csv'
data = np.genfromtxt(csv_path, delimiter=',', names=True, dtype=None, encoding='utf-8')

month_x = data['月份']
data_precipitation = data['降水量mm']
data_evaporation = data['蒸发量mm']
data_tem = data['气温℃']

fig, ax = plt.subplots(figsize=(10, 6))

barh1 = ax.bar(month_x, data_precipitation, label='降水量', color='#1f77b4')
barh2 = ax.bar(month_x, data_evaporation, bottom=data_precipitation, label='蒸发量', color='#ff7f0e')

ax2 = ax.twinx()
lines = ax2.plot(month_x, data_tem, 'mo--', label='气温') 

ax.set_xlabel('月份', fontsize=12)
ax.set_ylabel('降水量/蒸发量 (mm)', fontsize=12)
ax2.set_ylabel('气温 (℃)', fontsize=12)
ax.set_xticks(month_x)
ax.set_xticklabels([f'{i}' for i in month_x]) 
ax.set_ylim(0, 380)
ax2.set_ylim(0, 35)

handles1, labels1 = ax.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax.legend(handles1 + handles2, labels1 + labels2, loc='upper right') 

plt.title('某地区全年的平均气温与降水量、蒸发量', fontsize=14)

plt.tight_layout()
plt.show()