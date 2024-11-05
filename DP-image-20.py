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
    max_index = numpy.where(density > 0.001)[0][-1]

    plot = seaborn.objects.Plot()
    plot = plot.add(seaborn.objects.Area(), x=point, y=density)
    plot = plot.limit(x=(point[min_index], point[max_index] + 1))
    plot_figure = plt.figure(dpi=300)
    plot_plot = plot.on(plot_figure).plot()
    plot_ax = plot_figure.axes[0]
    plot_ax.fill_between(x=point, y1=density, alpha=0.5, facecolor="#1f77b4")
    plot_ax.axvline(x=point[max_index])
    text_high = 0.05
    plot_ax.text(
        x=point[max_index] + 0.5,
        y=text_high + text_high / 5,
        s="epsilon",
        va="center",
        ha="center",
    )
    plot_plot.save("DP-image/20.png", dpi=300)
    # plot_plot.show()
