from typing import Protocol


# Define what behavior an object must have
class Drawable(Protocol):
    def draw(self) -> None: ...


# Any class with a draw() method satisfies this protocol
# NO inheritance needed!


# Protocol has NO effect on these classes
class Circle:
    def draw(self) -> None:
        print("Drawing circle")


class Square:
    def draw(self) -> None:
        print("Drawing square")


# Both work with this function
# Protocol only matters HERE ↓
def render(shape: Drawable) -> None:  # Type hint uses Protocol
    shape.draw()


# ✅ Works! (even though Circle/Square don't inherit from Drawable)
# Type checker:
render(Circle())  # ❌ Error: Circle missing draw()
render(Square())  # ✅ OK: Square has draw()

# But you can still create Circle instances!
c = Circle()  # ✅ No problem
