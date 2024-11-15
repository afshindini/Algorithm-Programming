"""This is a solution to ancient berland circus problem"""

import math


def triangle_area(side1:float, side2:float, side3:float) -> float:
    """Calculate the area of triangle using heros formula"""
    side = 0.5*(side1 + side2 + side3)
    return math.sqrt(side*(side - side1)*(side - side2)*(side - side3))


def points_distance(pt1_x:float, pt1_y:float, pt2_x:float, pt2_y:float) -> float:
    """Calculate euclidean distance between two points"""
    return math.sqrt((pt1_x - pt2_x)**2 + (pt1_y - pt2_y)**2)


def circum_radius(side1:float, side2:float, side3:float, area:float) -> float:
    """Calculate the radious based on the triangle sides and area"""
    return 0.25*(side1*side2*side3)/area


def polygon_area(n_sides:int, rad:float) -> float:
    """calculate area of polygon based on its number of sides and circum radius"""
    return 0.5*(rad**2)*n_sides*math.sin(2*math.pi/n_sides)

def central_angle(side1:float, side2:float, side3:float) -> float:
    """Return central angles of all vertices"""
    angle = math.acos((side2*side2+side3*side3-side1*side1)/(2*side2*side3))
    return angle

def gcd_calculation(num1:float, num2:float) -> float:
    """Find the great common divisor"""
    if num1 < num2:
        return gcd_calculation(num2,num1)
    if abs(num2) < 0.01:
        return num1
    return gcd_calculation(num2, num1-math.floor(num1/num2)*num2)

def ancient_circus() -> float:
    """Return the smallest area of regular polygon"""
    vertices = []
    for _ in range(3):
        vertices.append(list(map(float,input().split(" "))))
    side1 = points_distance(vertices[0][0], vertices[0][1], vertices[1][0], vertices[1][1])
    side2 = points_distance(vertices[1][0], vertices[1][1], vertices[2][0], vertices[2][1])
    side3 = points_distance(vertices[2][0], vertices[2][1], vertices[0][0], vertices[0][1])
    angle1 = central_angle(side1, side2, side3)
    angle2 = central_angle(side2, side3, side1)
    angle3 = central_angle(side2, side1, side3)
    temp = 2*gcd_calculation(angle1, gcd_calculation(angle2,angle3))
    n_slides = round(2*math.pi/temp)
    tri_area = triangle_area(side1, side2, side3)
    radius = circum_radius(side1, side2, side3, tri_area)
    return polygon_area(n_slides, radius)





if __name__ == "__main__":
    print(ancient_circus())
    