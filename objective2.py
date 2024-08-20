from polygon import PolygonSequence

def objective2():
    n = 25
    circumradius = 10
    polygon_sequence = PolygonSequence(n, circumradius)
    print(polygon_sequence)
    print(f'Max Efficiency Polygon: {polygon_sequence.max_efficiency_polygon}')

if __name__ == "__main__":
    objective2()