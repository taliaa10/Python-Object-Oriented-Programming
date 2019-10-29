class Square:
    def __init__(self, side):
        self.side = side

    def __add__(squareOne, squareTwo):
        return ((4 * squareOne.side) + (4*squareTwo.side))


squareOne = Square(5)  # 5 * 4 = 20
squareTwo = Square(10)  # 10 * 4 = 40
print('Sum of sides of both the squares = ', squareOne + squareTwo)
