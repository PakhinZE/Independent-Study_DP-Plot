import seaborn
import seaborn.objects
import matplotlib.pyplot as plt
import matplotlib.figure as mpl
import scipy.stats
import numpy
import matplotlib


def cal_dis_val(distribution, delta, count, mean):
    distri = distribution
    max_float = 0.99999999
    min_float = 0.00000001
    max_point = distri.ppf(max_float, loc=mean)
    min_point = distri.ppf(min_float, loc=mean)
    point = numpy.linspace(min_point, max_point, count)
    density = distri.pdf(point, loc=mean)
    epsilon = distri.interval(1 - delta * 2, loc=mean)[1]
    shade_left = numpy.linspace(-max_point, epsilon, count // 2)
    density_left = distri.pdf(shade_left, loc=mean)
    shade_right = numpy.linspace(epsilon, max_point, count // 2)
    density_right = distri.pdf(shade_right, loc=mean)
    return point, density, shade_left, density_left, shade_right, density_right


if __name__ == "__main__":
    point_1, density_1, shade_left_1, density_left_1, shade_right_1, density_right_1 = (
        cal_dis_val(scipy.stats.norm, 1e-2, 1000, 0)
    )
    point_2, density_2, shade_left_2, density_left_2, shade_right_2, density_right_2 = (
        cal_dis_val(scipy.stats.norm, 1e-2, 1000, 3)
    )

    plot = seaborn.objects.Plot()
    plot = plot.add(seaborn.objects.Line(), x=point_1, y=density_1)
    plot = plot.add(seaborn.objects.Line(), x=point_2, y=density_2)
    # plot = plot.theme({"figure.dpi": 300, "savefig.dpi": 300})
    plot_figure = plt.figure()
    plot_plot = plot.on(plot_figure).plot()
    plot_ax = plot_figure.axes[0]
    plot_ax.fill_between(
        x=shade_left_1, y1=density_left_1, alpha=0.5, facecolor="#1f77b4"
    )
    plot_ax.fill_between(
        x=shade_right_1, y1=density_right_1, alpha=0.5, facecolor="#d62728"
    )
    plot_ax.fill_between(
        x=shade_left_2, y1=density_left_2, alpha=0.5, facecolor="#1f77b4"
    )
    plot_ax.fill_between(
        x=shade_right_2, y1=density_right_2, alpha=0.5, facecolor="#d62728"
    )
    plot_ax.annotate(
        text="",
        xy=(point_1[0], 0.1),
        xytext=(point_2[-1], 0.1),  # xytext=(point_2[-1], 0.1),
        arrowprops=dict(arrowstyle="|-|"),
        va="center",
        ha="center",
    )
    plot_ax.text(x=1.5, y=0.1 + 0.02, s="sensitivity", va="center", ha="center")
    plot_plot.show()
    print(matplotlib.rcParams["figure.figsize"])
    print(matplotlib.rcParams["savefig.dpi"])
    print(matplotlib.rcParams["figure.dpi"])