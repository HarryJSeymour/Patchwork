from graphics import * 

def usefulErrorMessages(typeOfError, additionalInformation): # Function used for handeling error messages outputted to user.
    if typeOfError == 1: # Error message if size is invalid.
        print("Invalid size, please choose a size of 5 or 7.")
        promt() # Recalls the Prompt Function so the user is allowed to re-enter a size.

    elif typeOfError == 2: # Error message if colours are the same.
        print("Please use 2 diffrent colours.")
        promt2(additionalInformation)

    elif typeOfError == 3: # Error message if size is invalid.
        print("Invalid colour, Please use a Valid colour.")
        print("VALID COLOURS: red, green, blue, magenta, orange or cyan.")
        promt2(additionalInformation) 


 # ---------------Main code------------------------

## Main program / drawings
def patchworkOne(win, size, c1, p1, p2, p3): # Rectangle Patchwork 8

    x = Point(p1, p2) # This is the bottom right corner of patch.
    y = Point(x.x - 10, p3) # x.x - 5 is the other side of rectangle I.E Width, 100 is the height of the first rectangle.
    
    for i in range(10): # Loops through 10 times changing the size of the rectangle to make a stair like patch.
        r = Rectangle(Point(x.x, x.y), Point(y.x,y.y))
        r.setFill(c1)
        r.draw(win)

        x.y = x.y + 10 # Decreases the hight from the top.
        y.x = y.x - 10 # Decreases the left to right side

def patchworkTwo(win, size, c2, p1, p2, p3): # Circles and Triangles Patchwork 8
    x = p1 - 30 # Uses the points given and withdraws a small amount so the patch isnt at the corner of the patch. Helps stop patches overlapping.
    y = p3 - 20

    # -Circles-.
    for i in range(3): # Creates the first 2 circles at the bottom of the patch, It does this 3 times, so there are 6 centre circles.
        for i in range(2):
            centre = Point(x, y) # The point where each circle is placed.
            c = Circle(centre,7) # The radius of each circle.
            # Displaying the circle visually.
            c.setFill(c2)
            c.draw(win)
            # Increases the x value so the circle is placed to the left of the first placed circle.
            x = x - 32

        # Resets the value for the second row.
        x = p1 - 30
        # Increases the hight so the next circles are one above.
        y = y - 30
    # Resets the value for the next operations.
    y = p3 - 20

    # Two variables used to position the 2 rows of 3 circles, placed inbetween the previous loops circles.
    a = p1 - 10
    b = p3 - 32
    for i in range(2): # This loop draws 3 sets of circles twice, inbetween the previous 6 circles which where draw.
        for i in range(3):
            centre = Point(a,b)
            c = Circle(centre,7)
            c.setFill(c2)
            c.draw(win)
            a = a - 37
        b = b - 32
        a = p1 - 10

    # -Triangles-.
    e = p3 - 32 # Variable used to store the Y position where the triangles will be placed.
    for i in range(2): # Loops 6 times. This The four sets of triangles, which point right.
        d = p1 - 18 # Variable used to store the X value.
        for i in range(2):
            for i in range(2):
                t = Polygon(Point(d,e), Point(d-10, e-10), Point(d-10, e+10)) # Creates the triangle.
                # Draws the traingles onto the graphical window.
                t.setFill(c2)
                t.draw(win)
                # Increases the X value so the triangle to the left is drawn, 10 pixels away.
                d = d - 10
            # Increases the distance for the second set of triangles.
            d = d - 15
        # Increases Height so the second time the loop runs the triangles are drawn 32 pixels above.
        e = e - 32
    
    e = p3 - 15 # Value used to store the Y value for the next sets of triangles.
    for i in range(3): # Loop to draw the downward facing triangles. 
        d = p1 - 10 # Sets a X value where the first triangle is placed.
        for i in range(3):

            for i in range(2): # Draws the two triangles together.
                t = Polygon(Point(d, e), Point(d + 10, e - 5), Point(d - 10, e - 5))
                t.setFill(c2)
                t.draw(win)

                t = Polygon(Point(d, e - 5), Point(d + 10, e - 10), Point(d - 10, e - 10))
                t.setFill(c2)
                t.draw(win)
            #Then after looping the x value is moved across to the left, by 35 pixels to draw the next 2 triangles. (2x)
            d = d - 35
        # The Y value is then increased so the next 3 sets of triangles are drawn above.
        e = e - 30
            

def patchworkControl(size, c1,c2,c3): # This function is in charge of calling the individual functions which create the two sepearate patches.
    win = GraphWin("Patchwork.", size*100, size*100)
    #size the amount of patches x/y 5 or 7.
    # c1/c2/c3 are colours.

    p1 = 100 # bottom right corner of patch.
    p2 = 0 # Base of the patch
    p3 = 100 # top of the patch

    #TOP of patch
    for i in range(size): # This loop calls the function to draw the first 5/7 patches located at the top of the window, they are the rectangles.
        patchworkOne(win, size, c1, p1, p2, p3)
        p1 = p1 + 100 # This increases the x value so the next rectangle in the loop is drawn to the right.

    #Bottom of patch
    p3 = 100 * size # This sets the Y value so the patches are drawn at the bottom of the Graphical window.
    m = size - 1 # This is a variable for storing how much p2 will be Multiplied by.
    p2 = 100 * m #This is the Y value of where the base of the patch will be.
    p1 = 100 # This is the X value of where the patch will be.
    for i in range(size):
        patchworkOne(win, size, c1, p1, p2, p3)
        p1 = p1 + 100
        
    # These values are used to change the positions
    p1 = 200 
    p2 = 100 
    p3 = 200 

    u1 = 100 * size
    o1 = 100
    o2 = 100
    o3 = 200

    for i in range(size - 2): # Middle patches.
        for i in range(1): #This loop calls the function to draw the sides of the patchwork.
            patchworkOne(win, size, c1, o1, o2, o3)
            patchworkOne(win, size, c1, u1, o2, o3)

        for i in range(size-2): #This loop calls the function to draw the second type of patch work, (Circles and triangles.)
            patchworkTwo(win, size, c2, p1, p2, p3)

    #These values are used to change the positions.
            p1 = p1 + 100
        p1 = 200
        p2 = p2 + 100
        p3 = p3 + 100
        o2 = o2 + 100
        o3 = o3 + 100
    win.getMouse()


# -------------User Inputs------------------

def promt(): # This function is the first to be called, and is used to allow the user to input a Patch size.
    size = int(input("Please enter the amount of patches you would like: "))
    if size == 5 or size == 7:
        promt2(size) # If patch size is 5 or 7, the user is allowed to input colours in prompt2()
    else:
        usefulErrorMessages(1, 0) # This calls the function which handles error messages, and gives it the parameter of 1, which is used to identify where the error occured.

def promt2(size): # This function is used after prompt(), and allows the user to enter the specified valid colours.
    validColours = ["red", "green", "blue", "magenta", "orange", "cyan"] # List of valid colours.
    colour1 = str(input("Please input colour 1:"))
    colour2 = str(input("Please input colour 2:"))
    colour3 = str(input("Please input colour 3:"))

    if colour1 == colour2 and colour1 == colour3: # Checks there are atleast 2 diffrent colours present.
        usefulErrorMessages(2, size) # Sends the size parameter aswell as the error function will recall Promt2 if there are any errors, 
                                     # and it will require the size variable in order to pass it to the patchworkControl Function.

    else:       # This else statment checks the colours the user inputed against the validColours list, if the if loop stores, which happens if a colour is not == to validcolours, then the error function is called.
        for i in range(len(validColours)):
            if colour1 == validColours[i]:
                for i in range(len(validColours)):
                   if colour2 == validColours[i]:
                    for i in range(len(validColours)):
                       if colour3 == validColours[i]:
                           print("Valid colours!")
                           patchworkControl(size, colour1, colour2, colour3) # Sends all valid user inputs to the patchworkControl Function.
                           return() # Ends the function.

        usefulErrorMessages(3,size) #Calls the error function if this loop isnt compleated.


promt() # Call function.