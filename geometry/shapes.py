def create_cube(size=4):
    #Корды всх 8 углов куба [X, Y, Z]
    points={
        "A": [0, 0, 0],
        "B": [size, 0, 0],
        "C": [size, size, 0],
        "D": [0, size, 0],
        "A1": [0, 0, size],
        "B1": [size, 0, size],
        "C1": [size, size, size],
        "D1": [0, size, size],
    }
    return points
def get_cube_edges():
    #все ребра куба
    edges=[
        #Низ куба
        ("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"),
        #Вверх куба
        ("A1", "B1"), ("B1", "C1"), ("C1", "D1"), ("D1", "A1"),
        #Вертикальные
        ("A", "A1"), ("B", "B1"), ("C", "C1"), ("D", "D1")
    ]
    return(edges)