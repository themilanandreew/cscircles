def trianglePerimeter(xA, yA, xB, yB, xC, yC):
    return distance2D(xA, yA, xB, yB) + distance2D(xA, yA, xC, yC) + distance2D(xB, yB, xC, yC)  # Variable distance2 is predefined
