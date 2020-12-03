import numpy

matrix = []
open_char = '.'
tree_char = '#'

with open ('./day3input.txt') as f:
    row = []
    for line in f:
        matrix.append(list(line.strip('\n')))

print matrix
print("number of rows: {}, columns: {}".format(len(matrix[0]), len(matrix)))

def treeCounter(x_travel, y_travel):
    rows = len(matrix[0])
    columns = len(matrix)
    curr_x = 0
    curr_y = 0
    tree_count = 0
    while (curr_y < columns):
        print("current position X: {}, Y: {}".format(curr_x, curr_y))
        print("x position: {} modulo {} = {}".format(curr_x, rows, curr_x%rows))

        curr_char = matrix[curr_y][curr_x%rows]
        if curr_char == tree_char:
            tree_count += 1
        curr_x+=x_travel
        curr_y+=y_travel
    return tree_count

def part1():
    answer = treeCounter(3, 1)
    print("tree count: {}".format(answer))

def part2():
    slopes = []
    slopes.append(treeCounter(1,1))
    slopes.append(treeCounter(3,1))
    slopes.append(treeCounter(5,1))
    slopes.append(treeCounter(7,1))
    slopes.append(treeCounter(1,2))
    print("slopes: {}".format(slopes))
    ans = numpy.prod(slopes)
    print("multiplied: {}".format(ans))

part1()
part2()