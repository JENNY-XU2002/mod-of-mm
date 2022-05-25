import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')  # 一行一列第一个
X = np.arange(1, 10, 1)
Y = np.arange(1, 10, 1)
X, Y = np.meshgrid(X, Y)  # 将坐标向量变为坐标矩阵，列为x的长度，行为y的长度
Z = 3 * X + 2 * Y + 30

# 构建平面
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet, linewidth=0, antialiased=True)
# 设置坐标轴
ax.set_xlabel("x-label", color='r')
ax.set_ylabel("y-label", color='g')
ax.set_zlabel("z-label", color='b')
ax.set_zlim3d(0, 100)

# 图例
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.savefig("d3_plane.png")
plt.show()