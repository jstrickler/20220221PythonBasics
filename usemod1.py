
# from john/math load geometry.py
from john.math import geometry
import sys

print(geometry.ANIMAL)
print(geometry.circle_area(14))
print(geometry.square_area(188))
print(geometry.rectangle_area(14, 15))
print()
# module search:
# 1. current folder
# 2. folders in PYTHONPATH
# 3. builtin folders
for path in sys.path:
    print(path)
