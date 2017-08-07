from numpy import array
import numpy as np
import re

p = re.compile('.* (\[[0-9.,\-]+\]|([\-0-9]+\.[0-9]+))')


class Path(object):
    def __init__(self, input_file, color):
        attr_list = map(lambda x: eval(p.match(x).group(1)), input_file.readlines())
        self._time_list = attr_list[0::4]
        self._translation_list = array(attr_list[1::4])
        self._quaternion = attr_list[2::4]
        self._rpy_list = attr_list[3::4]
        self._color = color

    def x(self):
        return self._translation_list[:, 0]

    def y(self):
        return self._translation_list[:, 1]

    def z(self):
        return self._translation_list[:, 2]

    def xy(self):
        return np.column_stack((self._translation_list[:, 0], self._translation_list[:, 1]))

    def color(self):
        return self._color
