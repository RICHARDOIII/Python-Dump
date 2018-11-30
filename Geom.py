import math
#  File: Geom.py

#  Description:

#  Student Name: Daniel Espinoza

#  Student UT EID: dee467

#  Partner Name: Mark Simmons

#  Partner UT EID: mjs5839

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created:9/15/2018

#  Date Last Modified:9/17/2018

class Point(object):
    # constructor
    # x and y are floats
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get distance
    # other is a Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    # get a string representation of a Point object
    # takes no arguments
    # returns a string
    def __str__(self):
        return '(' + str(self.x) + ", " + str(self.y) + ")"

    # test for equality
    # other is a Point object
    # returns a Boolean
    def __eq__(self, other):
        tol = 1.0e-16
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))


class Circle(object):
    # constructor
    # x, y, and radius are floats
    def __init__(self, radius=1, x=0, y=0):
        self.radius = radius
        self.center = Point(x, y)
        if radius < 0:
            self.radius = 1 # override invalid parameter with default value

    # compute cirumference
    def circumference(self):
        return 2.0 * math.pi * self.radius

    # compute area
    def area(self):
        return math.pi * self.radius * self.radius

    # determine if point is strictly inside circle
    def point_inside(self, p):
        return (self.center.dist(p) < self.radius)

    # determine if a circle is strictly inside this circle
    def circle_inside(self, c):
        distance = self.center.dist(c.center)
        return (distance + c.radius) < self.radius

    # determine if a circle c intersects this circle (non-zero area of overlap)
    # the only argument c is a Circle object
    # returns a boolean
    def does_intersect(self, c):
        distance = self.center.dist(c.center)
        return distance < c.radius + self.radius

    # determine the smallest circle that circumscribes a rectangle
    # the circle goes through all the vertices of the rectangle
    # the only argument, r, is a rectangle object
    def circle_circumscribes(self, r):
        self.radius=(r.ul.dist(r.lr))/2
        self.center=Point(r.ul.x+(r.length()/2),r.ul.y-(r.width()/2))

    # string representation of a circle
    # takes no arguments and returns a string
    def __str__(self):
        return ("center: ("+str(self.center.x)+","+str(self.center.y)+") radius: "+ str(self.radius))

    # test for equality of radius
    # the only argument, other, is a circle
    # returns a boolean
    def __eq__(self, other):
        tol = 1.0e-16
        return(abs(radius.self - radius.other) < tol)

class Rectangle(object):
    # constructor
    def __init__(self, ul_x=0, ul_y=1, lr_x=1, lr_y=0):
        if ((ul_x < lr_x) and (ul_y > lr_y)):
            self.ul = Point(ul_x, ul_y)
            self.lr = Point(lr_x, lr_y)
        else:
            self.ul = Point(0, 1)
            self.lr = Point(1, 0)

    # determine length of Rectangle (distance along the x axis)
    # takes no arguments, returns a float
    def length(self):
        return self.lr.x-self.ul.x

    # determine width of Rectangle (distance along the y axis)
    # takes no arguments, returns a float
    def width(self):
        return self.ul.y - self.lr.y

    # determine the perimeter
    # takes no arguments, returns a float
    def perimeter(self):
        return 2*self.length()+2*self.width()
    
    # determine the area
    # takes no arguments, returns a float
    def area(self):
        return self.length() * self.width()

    # determine if a point is strictly inside the Rectangle
    # takes a point object p as an argument, returns a boolean
    def point_inside(self, p):
        return(p.x > self.lr.x and p.x < self.lr.x \
               and p.y < self.ul.y and p.y > self.lr.y)

    # determine if another Rectangle is strictly inside this Rectangle
    # takes a rectangle object r as an argument, returns a boolean
    # should return False if self and r are equal
    def rectangle_inside(self, r):
        return(self.point_inside(r.ul)==True and self.point_inside(r.lr)==True)

    # determine if two Rectangles overlap (non-zero area of overlap)
    # takes a rectangle object r as an argument returns a boolean
    def does_intersect(self, other):
        return not(self.ul.x > other.lr.x \
            or self.ul.y < other.lr.y \
            or self.lr.x < other.ul.x \
            or self.lr.y > other.ul.y)

    # determine the smallest rectangle that circumscribes a circle
    # sides of the rectangle are tangents to circle c
    # takes a circle object c as input and returns a rectangle object
    def rect_circumscribe(self, c):
        ul_x = c.center.x - c.radius
        ul_y = c.center.y + c.radius
        lr_x = c.center.x + c.radius
        lr_y = c.center.y - c.radius
        return Rectangle(ul_x, ul_y, lr_x, lr_y)

    # give string representation of a rectangle
    # takes no arguments, returns a string
    def __str__(self):
        return("ul: {p1}, lr: {p2}".format(p1 = self.ul, p2 = self.lr))

    # determine if two rectangles have the same length and width
    # takes a rectangle other as argument and returns a boolean
    def __eq__(self, other):
        tol = 1.0e-16
        return(abs(self.area - other.area) < tol)


def main():


# open the file geom.txt
    data_bank=[]
    in_file = open("./geom.txt", "r")
    for line in in_file:
        data_bank.append(line.split())
# create Point objects P and Q
    x=0
    P = Point(float(data_bank[x][0]),float(data_bank[x][1]))
    x+=1
    Q = Point(float(data_bank[x][0]),float(data_bank[x][1]))
    x+=1
# print the coordinates of the points P and Q
    print("Coordinates of P: ",end="")
    print(P)
    print("Coordinates of Q: ",end="")
    print(Q)
# find the distance between the points P and Q
    print("Distance between P and Q: ", end="")
    print(str(P.dist(Q)))
# create two Circle objects C and D
    C= Circle(float(data_bank[x][2]),float(data_bank[x][0]),float(data_bank[x][1]))
    x+=1
    D= Circle(float(data_bank[x][2]),float(data_bank[x][0]),float(data_bank[x][1]))
    x+=1
# print C and D
    print("C:", end=" ")
    print(C)
    print("D:", end=" ")
    print(D)
# compute the circumference of C
    print("Circumference of C: "+str(C.circumference()))
# compute the area of D
    print("Area of D: "+str(D.area()))
# determine if P is strictly inside C
    if (C.point_inside(P)):
        print("P is inside C")
    else:
        print("P is not inside C")
# determine if C is strictly inside D
    if (D.circle_inside(C)):
        print("C is inside D")
    else:
        print("C is not inside D")
# determine if C and D intersect (non zero area of intersection)
    if (C.does_intersect(D)):
        print("C does intersect D")
    else:
        print("C does not intersect D")
# determine if C and D are equal (have the same radius)
    if (C.radius==D.radius):
        print("C is equal to D")
    else:
        print("C is not equal to D")
# create two rectangle objects G and H
    G= Rectangle(float(data_bank[x][0]),float(data_bank[x][1]),float(data_bank[x][2]), float(data_bank[x][3]))
    x+=1
    H= Rectangle(float(data_bank[x][0]),float(data_bank[x][1]),float(data_bank[x][2]), float(data_bank[x][3]))
#print the two rectangles G and H
    print("Rectangle G:",G)
    print("Rectangle H:",H)
# determine the length of G (distance along x axis)
    print("Length of G:",str(G.length()))
# determine the width of H (distance along y axis)
    print("Width of H:",str(H.width()))
# determine the perimeter of G
    print("Perimeter of G",str(G.perimeter()))
# determine the area of H
    print("Area of H:",str(H.area()))
# determine if point P is strictly inside rectangle G
    if(G.point_inside(P)):
        print("P is inside G")
    else:
        print("P is not inside G")
# determine if rectangle G is strictly inside rectangle H
    if(H.rectangle_inside(G)):
        print("G is inside H")
    else:
        print("G is not inside H")
# determine if rectangles G and H overlap (non-zero area of overlap)
    if(G.does_intersect(H)):
        print("G does overlap H")
    else:
        print("G does not overlap H")
# find the smallest circle that circumscribes rectangle G
# goes through the four vertices of the rectangle
    Circle_G=Circle()
    Circle_G.circle_circumscribes(G)
    print("Circle that circumscribes G:",Circle_G)
# find the smallest rectangle that circumscribes circle D
# all four sides of the rectangle are tangents to the circle
    rect_D=Rectangle()
    rect_D.rect_circumscribe(D)
    print("Rectangle that circumscribes D:",rect_D)
# determine if the two rectangles have the same length and width
    if(H.length()==G.length() and H.width()==G.width()):
        print("Rectangle G is equal to H")
    else:
        print("Rectangle G is not equal to H")
# close the file geom.txt
    in_file.close()
# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()