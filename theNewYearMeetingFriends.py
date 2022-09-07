coordinates = [int(x) for x in input().split()]
coordinates.sort()
print(coordinates[2] - coordinates[0])
