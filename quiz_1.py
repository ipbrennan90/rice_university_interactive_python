# def equation(numbers):
#     tel = {}
#     for number in numbers:
#         tel[number] = (-5)*(number**5) + 69*(number**2) - 47
#     print tel
#     return tel.keys()[tel.values().index(max(tel.values()))]
#
# print equation([0,1,2,3])
#

# def future_value(present_value, annual_rate, periods_per_year, years):
#     rate_per_period = annual_rate / periods_per_year
#     periods = periods_per_year * years
#     future_value = float(present_value*(1+rate_per_period)**periods)
#     return future_value
#
#     # Put your code here.
#
# print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)

import math
# def regular_polygon_area(n, s):
#     return float((.25*n*s**2)/(math.tan(math.pi/n)))
#
# print(regular_polygon_area(7,3))


def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale

project_to_distance(2, 7, 4)
