import seaborn
import seaborn.objects
import matplotlib.pyplot as plt
import numpy

if __name__ == "__main__":
    random = numpy.random.default_rng()
    point = random.integers(low=-3, high=3, size=1000, endpoint=True)

    plot = seaborn.objects.Plot()
    plot = plot.add(
        seaborn.objects.Bars(width=0.5),
        seaborn.objects.Hist(stat="probability", discrete=True),
        x=point,
    )
    plot_figure = plt.figure(dpi=300)
    plot_plot = plot.on(plot_figure).plot()
    plot_ax = plot_figure.axes[0]
    plot_plot.save("DP-image/11.png", dpi=300)
    # plot_plot.show()
