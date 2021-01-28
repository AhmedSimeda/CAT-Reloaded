# a helping function to determine whether there is no change or not
def is_right(charge, r):
    return (charge%10 == 0) or ((charge-r)%10 == 0)

k, r = tuple(map(int, input().split()))

charge = k
n_shovel = 1
while not is_right(charge, r):
    n_shovel += 1
    charge    = k*n_shovel
    
print(n_shovel)