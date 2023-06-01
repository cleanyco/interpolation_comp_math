# TODO table of finite differences
# TODO input of interpolation point (x0, x1...xn - interpolation nodes);
# TODO plot graphs
# TODO lagrange & gauss
# F(xi) = yi

from interpolation import get_finite_differences_table

dots = [[2.1, 3.759], [2.15, 4.186], [2.2, 4.922], [2.25, 5.349], [2.3, 5.928], [2.35, 6.419], [2.4, 7.084]]
table = get_finite_differences_table(dots)
print(table)