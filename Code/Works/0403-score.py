import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['SimHei']

# 直接使用模拟成绩，不读取Excel，彻底解决报错
data = [55,68,72,85,90,45,78,88,92,66,73,81,59,95,85,77,62,83,91,70]
bins = [0,10,20,30,40,50,60,70,80,90,100]

n,bins,patches = plt.hist(data, bins=bins, color="skyblue", edgecolor="black", rwidth=0.8, alpha=0.7, histtype="bar")

plt.xlabel("期末综合成绩")
plt.ylabel("人数")
plt.title("期末综合成绩分布直方图")
plt.xticks(bins)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()

print("各分数段人数：", n)