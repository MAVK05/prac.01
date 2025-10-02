# Point in a rectangle (centered at (0,0), width = 10, height = 5)

# read coordinates from user (allow floats)
x = float(input("Enter the x-coordinate of the point: "))
y = float(input("Enter the y-coordinate of the point: "))

width = 10.0
height = 5.0

half_width = width / 2.0   # 5.0
half_height = height / 2.0 # 2.5

# check if point is inside (inclusive of boundary)
if abs(x) <= half_width and abs(y) <= half_height:
    print(f"Point ({x}, {y}) is in the rectangle")
else:
    print(f"Point ({x}, {y}) is not in the rectangle")
