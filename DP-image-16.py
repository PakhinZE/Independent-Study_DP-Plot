import cal_dis_val
import seaborn
import seaborn.objects
import matplotlib.pyplot as plt
import scipy.stats
import numpy

if __name__ == "__main__":
    point_1, density_1, shade_left_1, density_left_1, shade_right_1, density_right_1 = (
        cal_dis_val.cal_dis_val(scipy.stats.laplace, 1e-2, 1000, 0, 3)
    )
    point_2, density_2, shade_left_2, density_left_2, shade_right_2, density_right_2 = (
        cal_dis_val.cal_dis_val(scipy.stats.laplace, 1e-2, 1000, 3, 3)
    )

    min_index = numpy.where(density_1 > 0.001)[0][0]
    max_index = numpy.where(density_2 > 0.001)[0][-1]

    plot = seaborn.objects.Plot()
    plot = plot.add(seaborn.objects.Area(), x=point_1, y=density_1)
    plot = plot.add(seaborn.objects.Area(), x=point_2, y=density_2)
    plot = plot.limit(x=(point_1[min_index], point_2[max_index]))
    plot_figure = plt.figure(dpi=300)
    plot_plot = plot.on(plot_figure).plot()
    plot_ax = plot_figure.axes[0]

    text_high = 0.03
    plot_ax.annotate(
        text="",
        xy=(-4, text_high),
        xytext=(6, text_high),
        arrowprops=dict(arrowstyle="|-|"),
        va="center",
        ha="center",
    )
    plot_ax.text(
        x=1.5, y=text_high + text_high / 5, s="sensitivity", va="center", ha="center"
    )
    plot_plot.save("DP-image/16.png", dpi=300)
    # plot_plot.show()
