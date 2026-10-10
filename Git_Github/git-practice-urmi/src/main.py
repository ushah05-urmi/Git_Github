from datetime import date
from utils import add, subtract, multiply, divide

print("Name: Urmi Ushah")
print("Today's Date:", date.today())

print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))
try:
    print("Division:", divide(10, 5))
except ValueError as error:
    print("Error:", error)
