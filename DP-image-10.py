import seaborn
import seaborn.objects
import matplotlib.pyplot as plt
import scipy.stats
import numpy

if __name__ == "__main__":
    random = numpy.random.default_rng()
    point = random.normal(size=1000)
    density = scipy.stats.gaussian_kde(point)

    plot = seaborn.objects.Plot()
    plot = plot.add(seaborn.objects.Area(), x=point, y=density(point))
    plot = plot.limit(x=(numpy.min(point), numpy.max(point)))
    plot_figure = plt.figure(dpi=300)
    plot_plot = plot.on(plot_figure).plot()
    plot_ax = plot_figure.axes[0]
    plot_plot.save("DP-image/10.png", dpi=300)
    # plot_plot.show()
