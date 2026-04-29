# ①导入模块
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.cbook import boxplot_stats
plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False
# ②准备数据
angles=np.linspace(0,2*np.pi,6,endpoint=False)
data=[[0.40,0.32,0.35,0.30,0.30,0.88],
      [0.85,0.35,0.30,0.40,0.40,0.30],
      [0.43,0.89,0.30,0.28,0.22,0.30],
      [0.30,0.25,0.48,0.85,0.45,0.40],
      [0.20,0.38,0.87,0.45,0.32,0.28],
      [0.34,0.31,0.38,0.40,0.92,0.28]]
radar_labels=['研究型','艺术型','社会型','企业型','传统型','现实性']

# ③绘制图形
data=np.concatenate((data,[data[0]]))
angles=np.concatenate((angles,[angles[0]]))
radar_labels=np.concatenate((radar_labels,[radar_labels[0]]))

plt.polar(angles,data)
plt.thetagrids(angles*180/np.pi,radar_labels)
plt.fill(angles,data,alpha=0.25)

# ④展示图形
plt.show()