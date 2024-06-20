LAB = "turtlelab6.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.8",LAB)

from turtlelab6 import turtle,home,rocky,flippy,check

from math import sqrt, atan2, degrees

def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def walkto(x, y):
    dx = x - turtle.x
    dy = y - turtle.y
    dist = sqrt(dx**2 + dy**2)
    angle = degrees(atan2(dy, dx))
    turtle.left(angle - turtle.heading)
    turtle.forward(dist)

total_distance_nemo_first = distance(turtle.x, turtle.y, rocky.x, rocky.y) + distance(rocky.x, rocky.y, flippy.x, flippy.y) + distance(flippy.x, flippy.y, home.x, home.y)
total_distance_mozart_first = distance(turtle.x, turtle.y, flippy.x, flippy.y) + distance(flippy.x, flippy.y, rocky.x, rocky.y) + distance(rocky.x, rocky.y, home.x, home.y)

if total_distance_nemo_first <= total_distance_mozart_first:
    walkto(rocky.x, rocky.y)
    walkto(flippy.x, flippy.y)
else:
    walkto(flippy.x, flippy.y)
    walkto(rocky.x, rocky.y)

walkto(home.x, home.y)

check()