import cal_dis_val
import seaborn
import seaborn.objects
import matplotlib.pyplot as plt
import scipy.stats

if __name__ == "__main__":
    point_1, density_1, shade_left_1, density_left_1, shade_right_1, density_right_1 = (
        cal_dis_val.cal_dis_val(scipy.stats.laplace, 1e-2, 1000, 0, 6)
    )
    point_2, density_2, shade_left_2, density_left_2, shade_right_2, density_right_2 = (
        cal_dis_val.cal_dis_val(scipy.stats.laplace, 1e-2, 1000, 3, 6)
    )

    plot = seaborn.objects.Plot()
    plot = plot.add(seaborn.objects.Area(), x=point_1, y=density_1)
    plot = plot.add(seaborn.objects.Area(), x=point_2, y=density_2)
    plot = plot.limit(x=(point_1[0], point_2[-1]))
    plot_figure = plt.figure(dpi=300)
    plot_plot = plot.on(plot_figure).plot()
    plot_ax = plot_figure.axes[0]
    plot_plot.save("DP-image/14.png", dpi=300)
    # plot_plot.show()
