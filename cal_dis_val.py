import numpy


def cal_dis_val(distribution, delta, count, mean, var=1):
    distri = distribution
    max_float = 0.9999999999999999
    min_float = 0.0000000000000001
    max_point = distri.ppf(max_float, loc=mean, scale=var)
    min_point = distri.ppf(min_float, loc=mean, scale=var)
    point = numpy.linspace(min_point, max_point, count)
    density = distri.pdf(point, loc=mean, scale=var)
    epsilon = distri.interval(1 - delta * 2, loc=mean, scale=var)[1]
    shade_left = numpy.linspace(-max_point, epsilon, count // 2)
    density_left = distri.pdf(shade_left, loc=mean, scale=var)
    shade_right = numpy.linspace(epsilon, max_point, count // 2)
    density_right = distri.pdf(shade_right, loc=mean, scale=var)
    return point, density, shade_left, density_left, shade_right, density_right


if __name__ == "__main__":
    pass
