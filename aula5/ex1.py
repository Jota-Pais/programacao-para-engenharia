import math
x1 =  float(input("defina o x do primeiro elemento:"))
y1 =  float(input("defina o y do primeiro elemento:"))
x2 =  float(input("defina o x do segundo elemento:"))
y2 =  float(input("defina o x do segundo elemento:"))

distance = math.sqrt((x2-x1)**2 +(y2 - y1)**2)
print(distance)
