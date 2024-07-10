def point_check(x0, y0, x, y):
    return (x0 - x) ** 2 + (y0 - y) ** 2


f = open('Circle.txt')
Center_of_Circle = f.readline().split()
Center_of_Circle = [float(Center_of_Circle[0]), float(Center_of_Circle[1])]
radius = float(f.readline())
f.close()

point = []
with open('Coordinate_points.txt') as f:
    for line in f:
        point.append([float(el) for el in line.split()])
        for el in point:
            if point_check(el[0], el[1], Center_of_Circle[0], Center_of_Circle[1]) < radius**2 :
                print('1')
            elif point_check(el[0], el[1], Center_of_Circle[0], Center_of_Circle[1]) > radius**2 :
                print('2')
            else:
                print('0')
        point.clear()
