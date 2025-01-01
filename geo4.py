import math

class Rectangle:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3
        self.x4, self.y4 = x4, y4

    def contains_point(self, x, y):
        """Checks if a given point is inside the rectangle."""
        return (self.x1 <= x <= self.x2 and self.y1 <= y <= self.y4) or \
               (self.x3 <= x <= self.x4 and self.y1 <= y <= self.y4) or \
               (self.x1 <= x <= self.x2 and self.y3 <= y <= self.y2) or \
               (self.x3 <= x <= self.x4 and self.y3 <= y <= self.y2)

def calculate_coordinates(x1, y1, x4, y4):
    """Calculates the other two corner points given the upper left and lower right corners."""
    x2, y2 = x4, y1
    x3, y3 = x1, y4
    return x2, y2, x3, y3

def create_rectangle_from_corners(x1, y1, x2, y2, x3, y3, x4, y4):
    """Creates a rectangle from given four corner points."""
    return Rectangle(x1, y1, x2, y2, x3, y3, x4, y4)

def create_rectangle_from_diagonals(x1, y1, x4, y4):
    """Creates a rectangle from given diagonal points."""
    x2, y2, x3, y3 = calculate_coordinates(x1, y1, x4, y4)
    return Rectangle(x1, y1, x2, y2, x3, y3, x4, y4)

def create_rectangle_from_previous(prev_rect, x4, y4):
    """Creates a rectangle based on the previous rectangle and a new lower right corner."""
    x1, y1 = prev_rect.x2, prev_rect.y2
    x2, y2, x3, y3 = calculate_coordinates(x1, y1, x4, y4)
    return Rectangle(x1, y1, x2, y2, x3, y3, x4, y4)

def check_point_in_rectangles(rectangles, x, y):
    """Checks if a given point is inside any of the rectangles."""
    for i, rectangle in enumerate(rectangles, start=1):
        if rectangle.contains_point(x, y):
            return f"The point ({x}, {y}) is inside rectangle Slot {i}."
    return "The point ({x}, {y}) is not inside any of the rectangles."

def create_square_around_point(x, y, side_length):
    """Creates a square around a given point with a specified side length."""
    x1 = x - side_length / 2
    y1 = y + side_length / 2
    x2 = x + side_length / 2
    y2 = y + side_length / 2
    x3 = x - side_length / 2
    y3 = y - side_length / 2
    x4 = x + side_length / 2
    y4 = y - side_length / 2
    return Rectangle(x1, y1, x2, y2, x3, y3, x4, y4)

def check_square_alignment(rectangles, square):
    """Checks if the square is fully inside any of the rectangles."""
    for i, rectangle in enumerate(rectangles, start=1):
        if rectangle.contains_point(square.x1, square.y1) and \
           rectangle.contains_point(square.x2, square.y2) and \
           rectangle.contains_point(square.x3, square.y3) and \
           rectangle.contains_point(square.x4, square.y4):
            return f"Square is inside rectangle Slot {i}"
    return "Square is misaligned"

def print_all_slots(rectangles):
    """Prints all the rectangles and their coordinates."""
    for i, rectangle in enumerate(rectangles, start=1):
        print(f"Slot {i}:")
        print(f"Upper left: ({rectangle.x1}, {rectangle.y1})")
        print(f"Upper right: ({rectangle.x2}, {rectangle.y2})")
        print(f"Lower left: ({rectangle.x3}, {rectangle.y3})")
        print(f"Lower right: ({rectangle.x4}, {rectangle.y4})")
        print()

def main():
    rectangles = []
    slot_number = 1

    while True:
        print("Menu:")
        print("1. Create a new parking slot")
        print("2. Check if a point is inside a parking slot")
        print("3. Check square alignment")
        print("4. Print all slots")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Choose input method:")
            print("1. Enter all four corner coordinates")
            print("2. Enter diagonals")
            input_method = input("Enter your choice: ")

            if input_method == '1':
                while True:
                    x1 = float(input("Enter x-coordinate of upper left: "))
                    y1 = float(input("Enter y-coordinate of upper left: "))
                    x2 = float(input("Enter x-coordinate of upper right: "))
                    y2 = float(input("Enter y-coordinate of upper right: "))
                    x3 = float(input("Enter x-coordinate of lower left: "))
                    y3 = float(input("Enter y-coordinate of lower left: "))
                    x4 = float(input("Enter x-coordinate of lower right: "))
                    y4 = float(input("Enter y-coordinate of lower right: "))

                    if x1 <= x2 and y1 <= y3:
                        break
                    else:
                        print("Invalid coordinates. Please ensure the upper-left corner has smaller x and y coordinates than the lower-right corner.")

                rectangle = create_rectangle_from_corners(x1, y1, x2, y2, x3, y3, x4, y4)
            elif input_method == '2':
                if slot_number == 1:
                    x1 = float(input("Enter x-coordinate of upper left: "))
                    y1 = float(input("Enter y-coordinate of upper left: "))
                    x4 = float(input("Enter x-coordinate of lower right: "))
                    y4 = float(input("Enter y-coordinate of lower right: "))
                    rectangle = create_rectangle_from_diagonals(x1, y1, x4, y4)
                else:
                    x1 = rectangles[-1].x2
                    y1 = rectangles[-1].y2
                    x4 = float(input("Enter x-coordinate of lower right: "))
                    y4 = float(input("Enter y-coordinate of lower right: "))
                    rectangle = create_rectangle_from_previous(rectangles[-1], x4, y4)
            else:
                print("Invalid input method.")
                continue

            rectangles.append(rectangle)
            print(f"Rectangle {slot_number} added.")
            print(f"Upper left: ({rectangle.x1}, {rectangle.y1})")
            print(f"Upper right: ({rectangle.x2}, {rectangle.y2})")
            print(f"Lower left: ({rectangle.x3}, {rectangle.y3})")
            print(f"Lower right: ({rectangle.x4}, {rectangle.y4})")
            print()
            slot_number += 1

        elif choice == '2':
            x = float(input("Enter x-coordinate of the point: "))
            y = float(input("Enter y-coordinate of the point: "))
            print(check_point_in_rectangles(rectangles, x, y))

        elif choice == '3':
            x = float(input("Enter x-coordinate of the point: "))
            y = float(input("Enter y-coordinate of the point: "))
            square = create_square_around_point(x, y, 1.5)
            print(check_square_alignment(rectangles, square))
        
        elif choice == '4':
            print_all_slots(rectangles)

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()