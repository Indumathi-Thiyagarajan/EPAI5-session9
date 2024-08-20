from polygon import Polygon

class PolygonSequence:
    def __init__(self, max_vertices, circumradius):
        self.max_vertices = max_vertices
        self.circumradius = circumradius
        self._polygons = [Polygon(i, circumradius) for i in range(3, max_vertices + 1)]

    def __len__(self):
        return len(self._polygons)

    def __getitem__(self, s):
        return self._polygons[s]

    @property
    def max_efficiency_polygon(self):
        return max(self._polygons, key=lambda p: p.efficiency)

    def __repr__(self):
        return (f'PolygonSequence(max_vertices={self.max_vertices}, circumradius={self.circumradius}, '
                f'polygons={len(self._polygons)})')

def objective2():
    n = 25
    circumradius = 10
    polygon_sequence = PolygonSequence(n, circumradius)
    
    print("Polygon Sequence:")
    print(polygon_sequence)
    
    print(f"\nNumber of polygons in sequence: {len(polygon_sequence)}")
    
    print("\nFirst polygon in sequence:")
    print(polygon_sequence[0])
    
    print("\nLast polygon in sequence:")
    print(polygon_sequence[-1])
    
    print("\nMax Efficiency Polygon:")
    print(polygon_sequence.max_efficiency_polygon)

if __name__ == "__main__":
    objective2()
