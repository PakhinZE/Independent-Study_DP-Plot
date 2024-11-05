import cal_dis_val
import seaborn
import seaborn.objects
import matplotlib.pyplot as plt
import scipy.stats

if __name__ == "__main__":
    point, density, shade_left, density_left, shade_right, density_right = (
        cal_dis_val.cal_dis_val(scipy.stats.norm, 1e-2, 1000, 0, 1)
    )

    plot = seaborn.objects.Plot()
    plot = plot.add(seaborn.objects.Area(), x=point, y=density)
    plot = plot.limit(x=(-8, 8))
    plot_figure = plt.figure(dpi=300)
    plot_plot = plot.on(plot_figure).plot()
    plot_ax = plot_figure.axes[0]
    plot_plot.save("DP-image/13.png", dpi=300)
    # plot_plot.show()