from geometry.formulas import divide_segment
from geometry.shapes import get_cube_edges, create_cube
cube = create_cube(size=4)
edges = get_cube_edges()
pointA = cube["A"]
pointA1 = cube["A1"]
pointM = divide_segment(pointA, pointA1,1,3)
print(f"Кол во точек: {len(cube)}")
print(f"Кол во ребер: {len(edges)}")
print(f"Точка в отношение 1:3: {pointM}")


