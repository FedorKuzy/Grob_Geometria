def creat_cube(size=4):
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
#Проверка
cube = creat_cube()
print(cube)