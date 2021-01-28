rows = int(input().split()[0])
colored = False

for _ in range(rows):
    row = input().split()
    if (not colored) and (len(set(row)&{'C', 'M', 'Y'})>0):
        colored = True

if colored:
    print("#Color")
else:
    print("#Black&White")




