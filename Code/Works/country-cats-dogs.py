import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = [
    "PingFang SC",
    "Heiti TC",
    "Arial Unicode MS",
    "SimHei",
]
plt.rcParams["axes.unicode_minus"] = False


countries = ["美国","英国","土耳其","瑞士","韩国","俄罗斯","墨西哥","日本","澳大利亚","巴西","加拿大","中国"]

cat_rate = [39, 27, 15, 26, 6, 57, 24, 14, 29, 28, 33, 19]
dog_rate = [51, 27, 11, 22, 23, 29, 42, 15, 39, 44, 33, 25]


fig, axes = plt.subplots(1, 2, figsize=(12, 8))

axes[0].barh(countries, cat_rate, color="#c79a2f", height=0.55)
axes[0].set_title("部分国家养猫人群的比例", fontsize=18)
axes[0].set_xlabel("人群比例(%)", fontsize=12)
axes[0].set_xlim(0, 65)
axes[0].invert_yaxis()

for i, value in enumerate(cat_rate):
    axes[0].text(value + 0.8, i, str(value), va="center", fontsize=11)

axes[1].barh(countries, dog_rate, color="#1098a5", height=0.55)
axes[1].set_title("部分国家养狗人群的比例", fontsize=18)
axes[1].set_xlabel("人群比例(%)", fontsize=12)
axes[1].set_xlim(0, 55)
axes[1].invert_yaxis()

for i, value in enumerate(dog_rate):
    axes[1].text(value + 0.8, i, str(value), va="center", fontsize=11)

plt.tight_layout()
plt.show()
