from matplotlib import pyplot as plt
import numpy as np

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = 'SimHei'
x = np.linspace(10, 210, 20, endpoint=False)
y = np.array([0.5, 2.0, 4.4, 7.9, 12.3, 17.7, 24.1, 31.5, 39.9, 49.2,
              59.5, 70.8, 83.1, 96.4, 110.7, 126.0, 142.2, 159.4, 177.6,
              196.8])
plt.scatter(x, y, marker='o', cmap=matplotlib.cm.winter, c=x)   
plt.xlabel('车速(km/h)')
plt.ylabel('制动距离(m)')
plt.suptitle('车速与制动的关系')
plt.title('制作者：24计算机3班', loc='right', fontsize=8)
plt.text(-5, -45, '数据来源：丰田公司测试数据')
plt.grid()
plt.show()