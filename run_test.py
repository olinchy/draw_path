import sys

from Validator import validate
from path import Path
from drawer import draw3d, draw2d

c = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']


def re_shape(files):
    return map(lambda x: Path(x[0], x[1]), zip(files, c))


if __name__ == '__main__':
    file_expect = file(sys.argv[1])
    file_reality = file(sys.argv[2])

    paths = re_shape([file_expect, file_reality])

    draw2d(paths, validate(paths))
    draw3d(paths, validate(paths))
