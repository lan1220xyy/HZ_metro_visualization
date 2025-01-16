import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def generate_paper_style_colorbar(max, min, save_path):
    """
    生成符合论文排版美观的颜色条 (colorbar)。

    参数:
    - max: 颜色条的最大值。
    - min: 颜色条的最小值。
    - save_path: 保存路径（包括文件名和扩展名，例如 'colorbar.eps'）。
    """
    # 创建一个图形和轴，颜色条的宽高比精致调整
    fig, ax = plt.subplots(figsize=(0.3, 4))  # 宽度为 0.3，高度为 4

    # 设置颜色条的归一化范围
    norm = mcolors.Normalize(vmin=min, vmax=max)
    sm = plt.cm.ScalarMappable(cmap='coolwarm', norm=norm)
    sm.set_array([])

    # 添加颜色条，精致化外观
    cbar = fig.colorbar(sm, cax=ax, orientation='vertical')
    cbar.ax.tick_params(labelsize=10, width=0.5, length=3)  # 刻度字体大小和刻度线宽度
    cbar.outline.set_linewidth(0.5)  # 设置边框宽度

    # 添加刻度标签，设置字体
    cbar.ax.set_ylabel('Value', fontsize=12, labelpad=10, rotation=270, weight='light')  # 标签旋转
    cbar.ax.yaxis.set_label_position('right')  # 标签放在右侧
    plt.show()

    # 保存颜色条为 .eps 文件
    # plt.savefig(save_path, dpi=300, bbox_inches='tight', format='eps')
    plt.close()


# 示例调用
generate_paper_style_colorbar(100, 0, "paper_style_colorbar.eps")