import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)  
sin_y = np.sin(x)
cos_y = np.cos(x)

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(x, sin_y, label='正弦曲线', color='#1f77b4')
ax.plot(x, cos_y, label='余弦曲线', color='#ff7f0e')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_position(('data', 0))   
ax.spines['bottom'].set_position(('data', 0)) 

xticks = [-2*np.pi, -3*np.pi/2, -np.pi, -np.pi/2, 0,
          np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
xticklabels = ['$-2\pi$', '$-3\pi/2$', '$-\pi$', '$-\pi/2$', '0',
               '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$']
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels)

ax.set_ylim(-1.1, 1.1)
ax.set_yticks([-1, -0.5, 0, 0.5, 1])

ax.legend(loc='upper right')

plt.tight_layout()
plt.show()
