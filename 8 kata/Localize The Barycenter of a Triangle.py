'''
https://www.codewars.com//kata/5601c5f6ba804403c7000004
'''

def bar_triang(point_a, point_b, point_c): 
    point_x = (point_a[0] + point_b[0] +  point_c[0])/3.0
    point_y = (point_a[1] + point_b[1] +  point_c[1])/3.0
    return ([round(point_x,4), round(point_y,4)]);

print(bar_triang([4, 6], [12, 4], [10, 10]),"==", [8.6667, 6.6667])
print(bar_triang([4, 2], [12, 2], [6, 10]), "==", [7.3333, 4.6667])
print(bar_triang([4, 8], [8, 2], [16, 6]), "==", [9.3333, 5.3333])
