import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matfonter import matfonter
matfonter("/Users/pylorsun/Documents/Study/2026term2/PythonData/Assets/FontSourcesMacOS/CN_SA_寒蝉端黑体 v1.3/ChillDuanSansVF.ttf")

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv(r"Code/Works/hr.csv", encoding="gbk")

sns.countplot(data=df, x=df.columns[-1])

plt.title("各工龄人数分布")
plt.xlabel("工龄")
plt.ylabel("人数")
plt.show()