# FreeCodeCamp Python Projects

This repository contains five Python projects that offer different functionalities.

## Project 1: Arithmetic Formatter

File: `Arithmetic_formatter.py`

The `Arithmetic_formatter.py` script defines a function `arithmetic_arranger` that formats arithmetic problems and their answers in a visually appealing way. The function takes a list of arithmetic problems as input and returns a formatted string. It also has an optional parameter `show_answers` that, if set to True, displays the answers along with the problems.

**Usage Example:**
```python
from FreeCodeCampProjectsPython.Arithmetic_formatter import arithmetic_arranger

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
formatted_problems = arithmetic_arranger(problems)
print(formatted_problems)
```

## Project 2: Budget App

File: `Budget_app.py`

The `Budget_app.py` script defines a class `Category` that represents a budget category. It contains methods to perform operations like deposit, withdrawal, transfer, and checking funds. The `create_spend_chart` function is also defined here, which creates a bar chart representing the percentage spent in each category.

**Usage Example:**
```python
from FreeCodeCampProjectsPython.Budget_app import Category, create_spend_chart

food = Category("Food")
clothing = Category("Clothing")
entertainment = Category("Entertainment")

food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food")

# Print category details
print(food)
print(clothing)
print(entertainment)

# Print spend chart
print(create_spend_chart([food, clothing, entertainment]))
```

## Project 3: Time Calculator

File: `Time_calculator.py`

The `Time_calculator.py` script defines a function `add_time` that calculates the time after adding a given duration to a given start time. The function takes a start time, a duration, and an optional start day as input and returns the new time after adding the duration. It also accounts for rolling over to the next day and calculates the day of the week accordingly.

**Usage Example:**
```python
from FreeCodeCampProjectsPython.Time_calculator import add_time

print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))
```

## Project 4: Polygon Area Calculator

File: `Polygon_area_calculator.py`

The `Polygon_area_calculator.py` script defines a `Rectangle` class and a `Square` class that can be used to calculate the area, perimeter, and other properties of rectangles and squares. The classes provide methods to perform various calculations and can be used to work with different shapes.

**Usage Example:**
```python
from FreeCodeCampProjectsPython.Polygon_area_calculator import Rectangle, Square

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
```

## Project 5: Probability Calculator

File: `Probability_calculator.py`

The `Probability_calculator.py` script defines a `Hat` class that represents a hat containing different colored balls. It provides methods to draw a specified number of balls randomly from the hat. It also defines an `experiment` function that performs an experiment by drawing balls from the hat and calculating the probability of drawing expected balls. This function allows you to test different experiments with the hat.

**Usage Example:**
```python
from FreeCodeCampProjectsPython.Probability_calculator import Hat, experiment

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, expected_balls={"red": 2, "green": 1}, num_balls_drawn=5, num_experiments=2000)
print("Probability:", probability)
```
---

