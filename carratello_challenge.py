from math import sqrt

print("Enter the three legs of a triangle to see if it is a triangle, a right triangle, an obtuse triangle, and/or an acute triange.")
side_a=int(input("Input side a:"))
side_b=int(input("Input side b:"))
side_c=int(input("Input side c:"))
def is_triangle():
    if (side_a > side_b + side_c) or (side_b > side_a + side_c) or (side_c > side_a + side_b):
        print ("Not a triangle.")
    else:
        print ("Is a triangle.")

is_triangle()
def is_right_triangle():
    if (side_a * side_a + side_b * side_b == side_c * side_c) or (side_b * side_b + side_c * side_c == side_a * side_a) or (side_c * side_c + side_a * side_a == side_b * side_b):
        print("Is a right triangle")
    else:
        print("Not a right triangle")
        
is_right_triangle()
def is_obtuse():
    if (side_a * side_a + side_b * side_b < side_c * side_c) or (side_b * side_b + side_c * side_c < side_a * side_a) or (side_c * side_c + side_a * side_a < side_b * side_b):
        print("Is obtuse")
    else:
        print("Not obtuse")
        
is_obtuse()
def is_acute():
    if (side_a * side_a + side_b * side_b > side_c * side_c) or (side_b * side_b + side_c * side_c > side_a * side_a) or (side_c * side_c + side_a * side_a > side_b * side_b):
        print("Is acute")
    else:
        print("Not acute")
        
is_acute()
input("You are done.")