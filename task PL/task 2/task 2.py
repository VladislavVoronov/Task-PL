from math import sqrt


def check_position(xc, yc, radius, x, y):
    distance = sqrt((xc - x) ** 2 + (yc - y) ** 2)
    if distance == radius:
        return 0
    elif distance < radius:
        return 1
    else:
        return 2


with open('circle.txt', 'r') as f:
    line = f.readline()
    xc, yc = line.split()
    line = f.readline()
    radius = line

with open('points.txt', 'r') as f:
    lines = f.readlines()

with open('results.txt', 'w') as f:
    for line in lines:
        x, y = line.rstrip('\n').split()

        position = check_position(int(xc), int(yc), int(radius), int(x), int(y))

        f.write(str(position) + '\n')
