import matplotlib.pyplot as plt
import numpy as np

data=[5,5,5,5]
angles=[0.25*np.pi,0.75*np.pi,1.25*np.pi,1.75*np.pi]
radar_labels=[chr(i+65) for i in range(4)]

data=np.concatenate((data,[data[0]]))
angles=np.concatenate((angles,[angles[0]]))
radar_labels=np.concatenate((radar_labels,[radar_labels[0]]))
# print(data)
# print(angles)

plt.polar(angles,data)
plt.thetagrids(angles*180/np.pi,radar_labels)
plt.fill(angles,data,alpha=0.25)
plt.show()