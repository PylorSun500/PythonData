import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12, 14))
ax = fig.add_subplot(111, projection='3d')

# === 配色 ===
MIKU_TEAL = '#39c5bb'
MIKU_DARK = '#1a8a82'
SKIN = '#fde8d0'
CHEEK = '#f4c4c4'
WHITE = '#f8f8f8'
BLACK = '#2a2a2a'
RED = '#e04040'
GRAY = '#c0c0c8'
DARK_GRAY = '#555555'

# =============================================
# 头部（球体）
# =============================================
phi = np.linspace(0, 2 * np.pi, 50)
theta = np.linspace(0, np.pi, 40)
Phi, Theta = np.meshgrid(phi, theta)

head_r = 1.0
head_cx, head_cy, head_cz = 0, 0.4, 5.0

hx = head_cx + head_r * np.sin(Theta) * np.cos(Phi)
hy = head_cy + head_r * np.sin(Theta) * np.sin(Phi)
hz = head_cz + head_r * np.cos(Theta)
ax.plot_surface(hx, hy, hz, color=SKIN, alpha=0.92, shade=True, linewidth=0)

# =============================================
# 脖子
# =============================================
nz = np.linspace(0, 0.5, 10)
nphi = np.linspace(0, 2 * np.pi, 20)
Nz, Nphi = np.meshgrid(nz, nphi)
nr = 0.16
nx = nr * np.cos(Nphi)
ny = head_cy + nr * np.sin(Nphi) - 0.05
nz_a = head_cz - head_r + 0.15 - Nz
ax.plot_surface(nx, ny, nz_a, color=SKIN, alpha=0.92, shade=True, linewidth=0)

# =============================================
# 身体（圆柱 + 领口装饰）
# =============================================
bz = np.linspace(0, 2.5, 20)
bphi = np.linspace(0, 2 * np.pi, 30)
Bz, Bphi = np.meshgrid(bz, bphi)
br = 0.65
bx = br * np.cos(Bphi)
by = head_cy - 0.6 + br * np.sin(Bphi)
bz_a = head_cz - head_r - 0.35 - Bz
ax.plot_surface(bx, by, bz_a, color=GRAY, alpha=0.85, shade=True, linewidth=0)

# 领口红色装饰线
collar_z = head_cz - head_r - 0.35
collar_ang = np.linspace(0, 2 * np.pi, 100)
collar_r = 0.68
ax.plot(collar_r * np.cos(collar_ang),
        head_cy - 0.6 + collar_r * np.sin(collar_ang),
        np.full_like(collar_ang, collar_z),
        color=MIKU_TEAL, linewidth=3)

# =============================================
# 齐刘海（前发）
# =============================================
bang_u = np.linspace(-0.85, 0.85, 40)
bang_v = np.linspace(0, 0.55, 15)
Bu, Bv = np.meshgrid(bang_u, bang_v)

# 刘海贴在前额，沿球面弯曲
b_x = Bu
b_y = head_cy + 0.85 - Bv * 0.3
b_z = head_cz + np.sqrt(np.clip(head_r**2 - b_x**2 - (b_y - head_cy)**2, 0, None))
# 让刘海稍向前突出
b_y = b_y + 0.03 * (1 - Bv / 0.55)
ax.plot_surface(b_x, b_y, b_z, color=MIKU_TEAL, alpha=0.92, shade=True, linewidth=0)

# =============================================
# 双马尾 —— Miku 最标志性的特征
# =============================================
def twin_tail(ax, side):
    """在 head 侧面生成一条青色马尾 ribbon"""
    t_len = np.linspace(0, 1, 80)   # 马尾长度方向 (1D)
    t_wid = np.linspace(-1, 1, 10)  # 马尾宽度方向 (1D)

    # ---- 马尾中心路径 (1D 计算，避免 gradient 在 2D 上返回 tuple) ----
    c_x = side * (0.82 + 0.4 * t_len + 2.0 * t_len**2 + 0.2 * np.sin(t_len * 4.5))
    c_y = head_cy - 0.05 + 0.25 * t_len - 0.06 * np.sin(t_len * 3.5)
    c_z = head_cz + 0.25 - 0.4 * t_len - 5.5 * t_len**1.6

    # ---- 1D 切向量 ----
    dcx = np.gradient(c_x)
    dcy = np.gradient(c_y)
    dcz = np.gradient(c_z)
    c_norm = np.sqrt(dcx**2 + dcy**2 + dcz**2) + 1e-8
    ctx, cty, ctz = dcx / c_norm, dcy / c_norm, dcz / c_norm

    # ---- 1D 宽度方向 (world-x 与切向的叉积) ----
    cwx = np.zeros_like(ctx)
    cwy = ctz
    cwz = -cty
    cwn = np.sqrt(cwx**2 + cwy**2 + cwz**2) + 1e-8
    cwx, cwy, cwz = cwx / cwn, cwy / cwn, cwz / cwn

    # ---- 1D 宽度 ----
    c_ribbon_w = 0.32 + 0.08 * np.sin(t_len * 5) - 0.1 * t_len

    # ---- 广播到 2D meshgrid 构造曲面 ----
    T, W = np.meshgrid(t_len, t_wid)
    X = c_x + cwx * c_ribbon_w * W
    Y = c_y + cwy * c_ribbon_w * W
    Z = c_z + cwz * c_ribbon_w * W

    ax.plot_surface(X, Y, Z, color=MIKU_TEAL, alpha=0.88, shade=True, linewidth=0)

    # 深色发尾渐变
    tip = T > 0.78
    ax.plot_surface(np.where(tip, X, np.nan),
                    np.where(tip, Y, np.nan),
                    np.where(tip, Z, np.nan),
                    color=MIKU_DARK, alpha=0.6, shade=True, linewidth=0)

    # ---- 发饰（红色发带结） ----
    knot_u = np.linspace(0, 2 * np.pi, 25)
    knot_v = np.linspace(-0.2, 0.2, 8)
    Ku, Kv = np.meshgrid(knot_u, knot_v)
    kr = 0.12
    knot_x = c_x[3] + kr * np.cos(Ku)
    knot_y = c_y[3] + kr * np.sin(Ku) * 0.6 + Kv
    knot_z = c_z[3] + kr * np.sin(Ku) * 0.8
    ax.plot_surface(knot_x, knot_y, knot_z, color=RED, alpha=0.9, shade=True, linewidth=0)


# 左右双马尾
twin_tail(ax, side=-1)
twin_tail(ax, side=1)

# =============================================
# 侧发（头两侧的短鬓发）
# =============================================
def side_hair(ax, side):
    su = np.linspace(0, 1, 30)
    sv = np.linspace(-1, 1, 6)
    Su, Sv = np.meshgrid(su, sv)
    s_x = side * (0.88 + 0.15 * Su)
    s_y = head_cy - 0.3 - 0.2 * Su
    s_z = head_cz + 0.05 - 0.35 * Su
    ax.plot_surface(s_x, s_y + Sv * 0.06, s_z + Sv * 0.02,
                    color=MIKU_DARK, alpha=0.8, shade=True, linewidth=0)

side_hair(ax, side=-1)
side_hair(ax, side=1)

# =============================================
# 眼睛
# =============================================
for sx, sy, sz in [(-0.28, 0.92, 5.22), (0.28, 0.92, 5.22)]:
    eye_u = np.linspace(0, 2 * np.pi, 20)
    eye_v = np.linspace(0, 0.12, 6)
    Eu, Ev = np.meshgrid(eye_u, eye_v)
    er_x = 0.1
    er_y = 0.06
    ex = sx + er_x * np.cos(Eu)
    ey = sy + er_y * np.sin(Eu) + Ev * 0.02
    ez = sz + Ev * 0
    ax.plot_surface(ex, ey, ez, color=MIKU_TEAL, alpha=0.9, shade=True, linewidth=0)
    # 瞳孔
    ax.scatter([sx], [sy + 0.01], [sz + 0.07], color=BLACK, s=30, alpha=0.9)
    ax.scatter([sx + 0.02], [sy + 0.02], [sz + 0.1], color=WHITE, s=6)

# =============================================
# 嘴巴
# =============================================
mouth_t = np.linspace(-0.18, 0.18, 30)
mouth_x = mouth_t
mouth_y = head_cy + 0.62 + 0.02 * np.sin(mouth_t * np.pi / 0.18)
mouth_z = head_cz + np.sqrt(np.clip(head_r**2 - mouth_x**2
                                     - (mouth_y - head_cy)**2, 0, None))
ax.plot(mouth_x, mouth_y, mouth_z, color='#d08080', linewidth=2)

# =============================================
# 腮红
# =============================================
for ch_x, ch_y in [(-0.4, 0.72), (0.4, 0.72)]:
    ch_z = head_cz + np.sqrt(np.clip(head_r**2 - ch_x**2 - (ch_y - head_cy)**2, 0, None))
    ch_u = np.linspace(0, 2 * np.pi, 15)
    ch_v = np.linspace(0, 0.08, 4)
    Cu, Cv = np.meshgrid(ch_u, ch_v)
    ax.plot_surface(ch_x + 0.08 * np.cos(Cu),
                    ch_y + 0.06 * np.sin(Cu),
                    ch_z + 0.01 + Cv,
                    color=CHEEK, alpha=0.4, shade=True, linewidth=0)

# =============================================
# 胳臂（简单圆柱体）
# =============================================
def arm(ax, side):
    arm_z = np.linspace(0, 1.8, 12)
    arm_phi = np.linspace(0, 2 * np.pi, 15)
    Az, Ap = np.meshgrid(arm_z, arm_phi)
    ar = 0.17
    a_cy = head_cy - 0.55
    a_cz = head_cz - head_r - 0.3
    ax_center = side * (br + 0.05)
    a_x = ax_center + ar * np.cos(Ap)
    a_y = a_cy + ar * np.sin(Ap)
    a_z = a_cz - Az
    ax.plot_surface(a_x, a_y, a_z, color=GRAY, alpha=0.85, shade=True, linewidth=0)

arm(ax, side=-1)
arm(ax, side=1)

# =============================================
# 头顶蝴蝶结
# =============================================
bow_u = np.linspace(0, 2 * np.pi, 30)
bow_v = np.linspace(-0.3, 0.3, 8)
Bu2, Bv2 = np.meshgrid(bow_u, bow_v)
bow_cx, bow_cy, bow_cz = 0, head_cy + 0.08, head_cz + head_r + 0.05
bow_r = 0.25
# 左右两个蝴蝶结圈
for bow_dx, bow_rot in [(-0.18, -0.5), (0.18, 0.5)]:
    bx_arr = bow_cx + bow_dx + bow_r * 0.4 * np.cos(Bu2) + Bv2 * 0.03
    by_arr = bow_cy + bow_r * 0.3 * np.sin(Bu2) * (0.6 + 0.4 * np.abs(np.cos(Bu2)))
    bz_arr = bow_cz + Bv2
    ax.plot_surface(bx_arr, by_arr, bz_arr, color=RED, alpha=0.85, shade=True, linewidth=0)

# =============================================
# 视角与标题
# =============================================
ax.view_init(elev=10, azim=-25)
ax.set_xlim(-5, 5)
ax.set_ylim(-3, 6)
ax.set_zlim(-2, 8)
ax.set_facecolor('#eceff4')

# 隐藏坐标轴面板
ax.xaxis.set_pane_color((1, 1, 1, 0))
ax.yaxis.set_pane_color((1, 1, 1, 0))
ax.zaxis.set_pane_color((1, 1, 1, 0))
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_zlabel('')
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_zticklabels([])
ax.set_title('初音ミク  —  Matplotlib 3D', fontsize=16,
             color=MIKU_TEAL, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()
