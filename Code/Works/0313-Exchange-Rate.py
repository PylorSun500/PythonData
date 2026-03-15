import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

df = pd.read_excel("/Users/pylorsun/Documents/Study/2025-2026第二学期/PythonData/Assets/exchange_data.xlsx")
print(df.columns)
y2017 = df[2017]
y2019 = df[2019]
x = np.arange(len(y2019))
plt.plot(x, y2019, color='gray', linestyle='--', marker='*')
plt.plot(x, y2017, color='blue', linestyle='-', marker='o')
plt.title("2017年7月与2019年7月美元 / 人民币汇率走势")
plt.legend(['2019年7月美元/人民币汇率', '2017年7月美元/人民币汇率'])
plt.xlabel('日期')
plt.ylabel('汇率')
for i, (j, y) in enumerate(zip(y2017, y2019)):
    plt.text(i+0.1, j+0.01, f'{j:.4f}', rotation=45, fontsize=6, ha='right', va='top')
    plt.text(i+0.1, y+0.01, f'{y:.4f}', rotation=45, fontsize=6, ha='right', va='top')
plt.show()