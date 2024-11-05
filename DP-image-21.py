import cal_dis_val
import seaborn
import seaborn.objects
import matplotlib.pyplot as plt
import scipy.stats
import numpy

if __name__ == "__main__":
    point, density, shade_left, density_left, shade_right, density_right = (
        cal_dis_val.cal_dis_val(scipy.stats.norm, 1e-2, 1000, 0, 1)
    )

    min_index = numpy.where(density > 0.001)[0][0]
    max_index = numpy.where(density > 0.001)[0][-1]  # type: ignore

    plot = seaborn.objects.Plot()
    plot = plot.add(seaborn.objects.Area(), x=point, y=density)
    plot = plot.limit(x=(point[min_index], point[max_index] + 1))
    plot_figure = plt.figure(dpi=300)
    plot_plot = plot.on(plot_figure).plot()
    plot_ax = plot_figure.axes[0]
    plot_ax.fill_between(x=shade_left, y1=density_left, alpha=0.5, facecolor="#1f77b4")
    plot_ax.fill_between(
        x=shade_right, y1=density_right, alpha=0.5, facecolor="#d62728"
    )
    plot_ax.axvline(x=shade_right[0])
    text_high = 0.05
    plot_ax.text(
        x=shade_right[0] + 0.5,
        y=text_high + text_high / 5,
        s="epsilon",
        va="center",
        ha="center",
    )
    plot_ax.annotate(
        text="<delta",
        xy=(2.4, 0.01),
        xytext=(shade_right[0] + 1, text_high - 0.02),
        arrowprops=dict(arrowstyle="->"),
        va="center",
        ha="center",
    )
    plot_plot.save("DP-image/21.png", dpi=300)
    # plot_plot.show()
