n, stones = input(), input()

to_take = 0
for i in range(len(stones)-1):
    if stones[i] == stones[i+1]:
        to_take += 1

print(to_take)