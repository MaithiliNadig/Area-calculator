while True :
    shape = input("Which shape do you want to calculate the area of(square, rectangle, circle) or type 'stop' to quit:").lower()

    if shape == "square":
        side = float(input("Enter the side length in centimeters: "))
        area_square = side*side
        print("The area of your square is " + str(area_square) + " square centimeters")

    
    elif shape == "rectangle":
        length = float(input("Enter the length in centimeters: "))
        width = float(input("Enter the width in centimeters: "))
        area_rectangle = length * width
        print("The area of the rectangle is " + str(area_rectangle) + "square centimeters.")

    elif shape == "circle":
        radius = float(input("Enter the radius in centimeters: "))
        area_circle = 3.14 * radius * radius
        print("The area of the circle is " + str(area_circle) + " square centimeters.")

    elif shape == "stop":
        print("Thank you for you time")
        break

    else :
        print("Try again with one of the valid choices")

    print()
