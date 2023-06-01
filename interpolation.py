from prettytable import PrettyTable


def lagrange(dots, x):
    result = 0
    n = len(dots)
    for i in range(n):
        nom, denom = 1, 1
        for j in range(n):
            if i == j:
                continue
            nom *= x - dots[j][0]
            denom *= dots[i][0] - dots[j][0]

        result += dots[i][1] * (nom / denom)

    return result

# TODO def lagrange_inaccuracy()


# def gauss(dots, x):



def get_finite_differences_table(dots):
    diff_table = PrettyTable()

    index = []  # formation of the first column
    for i in range(len(dots)):
        index.append(i)
    diff_table.add_column("o", index)

    x = []  # formation of the second column
    for i in range(len(dots)):
        x.append(dots[i][0])
    diff_table.add_column("x", x)

    y = []  # formation of the third column
    for i in range(len(dots)):
        y.append(dots[i][1])
    diff_table.add_column("y", y)

    last_delta = []
    count_of_deltas = len(dots) - 1
    for i in range(count_of_deltas):
        column_name = "delta^" + str(i+1) + "y_i" if i != 0 else "delta y_i"
        if i == 0:
            current_delta = []
            for j in range(len(dots)):
                current_delta.append(dots[j][1])
            diff_table.add_column(column_name, current_delta)
            last_delta = current_delta
        else:
            current_delta = []
            for j in range(count_of_deltas - i + 1):
                current_delta.append(round(last_delta[j + 1] - last_delta[j], 3))
            while len(current_delta) < 7:
                current_delta.append('')  # FIXME
            diff_table.add_column(column_name, current_delta)
            last_delta = current_delta

    return diff_table
