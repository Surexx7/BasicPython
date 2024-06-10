# Ask users heigth and width of the wall and calculate the area of wall and cost required to
# paint the wall

import math

def paint_calculation(height,width):
    cost=(h*w)/coverage
    a=math.ceil(cost)
    print(f"The total cost is: {a}")


h=int(input("Enter the height of the wall: "))
w=int(input("Enter the width if the wall: "))
coverage=7
paint_calculation(height=h,width=w)
