n = int(input())

polyhedrons = {
    "T": 4,
    "C": 6,
    "O": 8,
    "D": 12,
    "I": 20
}

faces = 0
for _ in range(n):
    faces += polyhedrons[input()[0]]

print(faces)
