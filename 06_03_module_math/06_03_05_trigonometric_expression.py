import math

x = float(input())
r = x * math.pi / 180
print(math.sin(r) + math.cos(r) + math.tan(r) ** 2)