from matplotlib import pyplot as plt

x = [20, 30, 23, 45, 79, 10, 13]
pie_labels = [chr(i + 65) for i in range(len(x))]
explode = [0.1] * 7
plt.pie(x, labels=pie_labels, autopct='%3.1f%%', wedgeprops={'width': 0.6} ,pctdistance=0.5, explode=explode, shadow=True)
plt.legend(loc='upper right', bbox_to_anchor = [1.05, 1.1], ncol = 2, title = '图例')

plt.show()