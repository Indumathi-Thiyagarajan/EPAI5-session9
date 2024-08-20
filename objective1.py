from polygon import Polygon

def objective1():
    p1 = Polygon(3, 10)
    p2 = Polygon(4, 10)
    p3 = Polygon(5, 10)

    print(p1)
    print(p2)
    print(p3)

    print("\n equality check")
    print(p1 == p2)
    print(p2 == p2)

    print("Greater than check")
    print(p2 > p1)
    print(p3 > p2)

if __name__ == "__main__":
    objective1()