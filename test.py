import generator as gen
import pathFinder as pf

def test():
    g = gen.Generator()
    p = pf.PathFinder()

    g.set_up_generator(20, 20)
    g.clear()

    g.generate(0, 1, 5, 6)

    a = g.get_labyrinth()

    for i in range(len(g.get_labyrinth())):
        for j in g.get_labyrinth()[i]:
            print(j, end=' ')
        print()

    print()
    AM = p.find(1, 3, 11, 13, a)

    for y in range(len(a)):
        for x in range(len(a[0])):
            print(AM[y][x], end=' ')
        print()