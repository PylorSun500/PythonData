# pyplot - 绘图接口

sentence: 
```python
from matplotlib import pyplot # as plt
```

## `pyplot.plot()` - 折线图

`plot(x, y, fmt, scalex=[bool], scaley=[bool], data=, label=)`

```python
x = []
y = []
plt.plot(x, y)
plt.show()
```

### 折线图样式参数
```python
# 颜色和线型
plt.plot(x, y, color='blue', linestyle='-', marker='o')

# 常用颜色：'red', 'blue', 'green', 'orange', 'purple', 'gray'
# 常用线型：'-' (实线), '--' (虚线), ':' (点线), '-.' (点划线)
# 常用标记：'o' (圆圈), '*' (星号), 's' (方块), '^' (三角形), 'D' (菱形)
```

### 添加数据标签
```python
for i, value in enumerate(y):
    plt.text(i, value + 0.01, f'{value:.4f}', rotation=45, fontsize=6, ha='right', va='top')
```

## `pyplot.bar()` - 条形图

`bar(x, y, width=0.8, bottom=None, *, align='center', label=None, tick_label=None)`<br>

[柱形图 示例代码](../Code/general.data_read_and_process.code/bar_single.py)

### 基本柱形图
```python
y = np.array([18, 12, 13, 8, 20])
x = np.arange(len(y))
tk = [chr(i) for i in range(97, 97+5)]  # ['a', 'b', 'c', 'd', 'e']

plt.figure(figsize=(10, 6))
plt.bar(x, y, width=0.4, align='edge', label="产品A", tick_label=tk)
plt.legend()
plt.show()
```

**实现思路**：
1. 柱形图通过不同高度的矩形条来比较各类别的数值大小
2. 使用 `np.arange()` 生成等间距的 x 坐标位置，确保柱形均匀分布
3. `width` 参数控制柱形的宽度，`align` 参数控制柱形对齐方式（'edge' 或 'center'）
4. `tick_label` 参数用于设置 x 轴刻度标签，替代默认的数字标签
5. 使用 `plt.figure(figsize=(10, 6))` 设置图形大小，确保图表有足够的显示空间

### 多组柱形图

可以同时绘制多个柱形图，然后将它们并排显示

[bar_double.py](../Code/general.data_read_and_process.code/bar_double.py)

**实现思路**：
1. 多组柱形图的核心思想是将不同组的数据在同一类别位置上并排显示
2. 通过调整第二组柱形的 x 坐标位置（`x+0.4`），使其与第一组柱形错开显示
3. 柱形宽度（`width=0.4`）需要适当设置，确保两组柱形之间有一定间距但不会重叠
4. 使用 `yerr` 参数可以为柱形添加误差棒，表示数据的不确定性范围
5. 通过 `plt.ylim()` 设置 y 轴范围，确保所有柱形都能完整显示且图表布局美观

### 堆积柱形图

[bar_stack.py](../Code/general.data_read_and_process.code/bar_stack.py)

堆积柱形图通过分别将第二列各图形放在第一列的最高值上面。与多组柱形图类似，通过 **调整 x 坐标位置** 实现并排显示
- 将 `plt.bar()` 返回的柱形对象保存到变量中，第二组柱形通过 `bottom=y1` 参数堆叠在第一组柱形之上。
- 使用 `zip()` 函数同时遍历两组柱形对象，为每个柱形添加数据标签
    - 通过 `bar.get_x()`、`bar.get_height()` 等方法获取柱形的精确位置和高度，确保标签位置准确
    - 标签位置需要根据柱形宽度进行微调，使其显示在柱形中间或顶部

### 带有误差棒的柱形图

`yerr = []` 或者 `xerr = []`

```python
plt.bar(x, y, width=0.4, yerr=[1, 1.5, 1.2, 1.2, 1.1])
```

误差棒用于表示数据的不确定性或标准差。在 `bar()` 函数中：

- 使用 `yerr` 参数为垂直柱形图添加垂直方向的误差棒
- 使用 `xerr` 参数可以为水平柱形图添加水平方向的误差棒
- 误差棒数据应该是一个与 y 数据长度相同的列表或数组，表示每个数据点的误差范围。

误差棒从柱形顶部向上和向下延伸，直观展示数据的波动范围。

## `pyplot.scatter()` 散点图

```py
pyplot.scatter(x, y, c=None, marker=None, alpha=None)
```

参数：
`x` : x 轴数据
`y` : y 轴数据

## `pyplot.boxplot` 箱形图

```py
pyplot.boxplot(x, 
            notch=None, sym=None, vert=None, whis=None, positions=None, 
            widths=None, 
            patch_artist=None, bootstrap=None,
            usermedians=None, conf_intervals=None,
            meanline=None, 
            showmeans=None, showcaps=None, showbox=None, showfliers=None,
            boxprops=None, labels=None, flierprops=None,
            medianprops=None, meanprops=None,
            capprops=None, whiskerprops=None)
```
其中：
- `notch` ：箱体缺口
- `whis` ：须线范围定义

可以使用 `cbook.boxplot_stats` 快速统计最大值、最小值等特殊值。
该方法返回一个字典，可以通过调用其键来映射对应的值。常用键如下：

- `med` : 中位数
- `q1` : 第一四分位数（25%）
- `q3`: 第三四分位数（75%）
- `whislo`: 下须（whisker low）
- `whishi`: 上须（whisker high）
- `fliers`: 离群值（异常值）
- `mean`: 平均值（可选）
- `cilo`, `cihi`: 置信区间（可选）
- `label`: 数据标签（可选）

### `pyplot.pie()` - 饼状图

[pie.py](../Code/general.data_read_and_process.code/pie.py)

用法：
```py
pie(x, explode=None, labels=None, autopct=None, pctdistance=0.6, startangle=None, * ,data=None, wedgeprops=None)
```

其中：
- `autopct` 自动计算百分比，传入 **控制符** ，如 `%3.1f%%` ；
- `*distance` 系列控制对应元素的相对距离；
- `startangle` 控制开始的角度，默认是 `0` ，即 `x+` 。

### 环状图

使用 `wedgeprops` 控制扇形的属性。
`wedgeprops` 的输入值是一个字典。例如：

```py
pie(..., wedgeprops={'width': 0.6})
```

这时，`width` 键控制扇形的径向宽度，使整个图表呈现环状图样式。

### 分离型饼图

使用 `explode` 属性使扇形之间出现空隙。传入数组或列表。这个列表的 `len()` 应该对应到饼图的数据量。例如：

```py
# 我们有 7 个数据：
dev_explode = [0.1]*7
exblode=dev_explode 
```

还有一些内容....

## 雷达图 `pyplot.polar()`

用法：
```py
plt.polar(theta, r, **kwargs)
```
其中，`angles` 表示角度坐标；`data` 表示

### 为雷达图做标签

### 为雷达图做填充色

## 单子图绘制 `pyplot.subplot()`

用法：
```python
plt.subplot(nrows, ncols, index, sharex, sharey, projection)
```

