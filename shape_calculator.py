# define Rectangle class and its methods
class Rectangle:
    def __init__(self, width, height):  # initialise/constructor call Rectangle's width and height variables/parameters. accepts two arguments.
        self.width = width              # any instance created of the Rectangle class will initialise with these two variables.
        self.height = height

    def set_width(self, width):         # defining a method to change the value of the initial width value. pass in one argument.
        self.width = width              # reassigns the old width variable to a new one. this new width value will be used in all subsequent methods defined below.

    def set_height(self, height):       # defining a method to change the value of the initial height value. pass in one argument.
        self.height = height            # reassigns the old height variable to a new one. this new height value will be used in all subsequent methods defined below

    def get_area(self):                 # defining a method to calculate the area of the rectangle.
        return self.width * self.height # no arguments required. uses the stored variables. returns the result when the method is called.

    def get_perimeter(self):                        # defining a method to calculate the perimeter of the rectangle.
        return (2 * self.width + 2 * self.height)   # no arguments required. uses the stored variables. returns the result when the method is called.
    
    def get_diagonal(self):                                     # defining a method to calculate the diagonal of the rectangle.
        return ((self.width ** 2 + self.height **2 ) ** 0.5)    # no arguments required. uses the stored variables. returns the result when the method is called.

    def __str__(self):                  # a constructor overload defined to customise the print format of the Rectangle class. returns the format to the screen when a print method is called
        return "Rectangle(width={}, height={})".format(self.width, self.height)

    def get_picture(self):                      # defining a method to draw the rectangle.
        if self.height > 50 or self.width > 50: # check if the height or width is greater than 50 then output the message to the screen.
            return ("Too big for picture")

        picture_collection = ""         # create an empty string to collect the symbols for the picture creation
        for _ in range(self.height):                        # loop through the height's value/variable to create the number of rows to print. no need for a named variable for looping through.
            picture_collection += '*' * self.width + '\n'   # using Python's polymorphism to print width's value/variable times of the symbol '*' with a newline special character at the end of each line.
        #return picture_collection                          # the collection is collated/added each time, to the string bucket created above
        print(picture_collection)                           # print/return the collated strings. these have a newline character at the end so should print each set on a new line

    def get_amount_inside(self, shape):             # defining a method to calculate the areas of two shapes and dividing by each other. accepts one argument (an instance of the Rectangle class).
        return self.get_area() // shape.get_area()  # calls the get_area method above on itself and then also calls the get_method above on the new passed-in instance of the Rectangle class.

# define Square class and its methods. Square is a sub-class of Rectangle class. will inherit all of its methods and variables 
# with little modifications reducing code redundancy and encouraging code factoring.
class Square(Rectangle):
    def __init__(self, side):                               # initialise Squares's variable/parameter 'side'. accepts one argument.
        Rectangle.__init__(self, width=side, height=side)   # call Rectangle class' constructor with keyword arguments for 
                                                            # width and height using the parameter 'side' initialised during Square's call.
    
    def set_side(self, side):       # defining a method to set the width and height of the square shape when called. takes two arguments. this an independent function to set Square class' side lengths.
        self.width = side           # the argument passed is then given to the width and height variables. these variable are then ready for subsequent usage in the Rectangle class' function calls.
        self.height = side          
                                    
    def __str__(self):              # a constructor overload defined to customise the print format of the Square class. returns the format to the screen when a print method is called.
        return "Square(side={})".format(self.width)

    def set_width(self, width):                 # defining a method to change the value of the initial side value. pass in one argument.
        Rectangle.set_width(self, width)        # reassigns the Rectangle class' old width variable to a new one. this new side value will be used in all subsequent methods
                                                # width variables has been inherited from Rectangle class. self argument required because we are calling the Rectangle class.

    def set_height(self, height):               # defining a method to change the value of the initial side value. pass in one argument
        Rectangle.set_height(self, height)      # reassigns the Rectangle class' old height variable to a new one. this new side value will be used in all subsequent methods
                                                # height variable has been inherited from Rectangle class. self argument required because we are calling the Rectangle class.

###### WORKING TEST BENCH AREA ######
if __name__ == '__main__':
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    rect.get_picture()

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    sq.get_picture()

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))

    r1 = Rectangle(10, 6)
    r2 = Rectangle(5, 3)
    print(r1.get_amount_inside(r2))

