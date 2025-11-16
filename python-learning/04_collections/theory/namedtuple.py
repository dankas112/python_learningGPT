from collections import namedtuple

point = namedtuple('Point', ['x', 'y', 'xx', 'yy', 'xxx'])
p = point(10, 20, 66, 'pipi', 25.678)
print(p.xxx, p.yy)