# Segitiga sama kaki

rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

# Diamond
rows = 5

for k in range(1, rows + 1):
    print(" " * (rows - k) + "* " * k)

for k in range(rows - 1, 0, -1):
    print(" " * (rows - k) + "* " * k)

# kotak

rows = 8
cols = 8
for m in range(rows):
    for j in range(cols):
        if (m + j) % 2 == 0:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()