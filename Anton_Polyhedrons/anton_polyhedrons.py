"""This is a solution for anton and polyhedrons problem"""

def anton_polyhedrons() -> int:
    """Return the number of faces of polyhedrons"""
    polyhedrons = {"Tetrahedron": 4, "Cube": 6, "Octahedron": 8,
                   "Dodecahedron": 12, "Icosahedron": 20}
    number = int(input(""))
    faces = 0
    for _ in range(number):
        faces += polyhedrons[input("")]

    return faces


if __name__ == "__main__":
    print(anton_polyhedrons())
