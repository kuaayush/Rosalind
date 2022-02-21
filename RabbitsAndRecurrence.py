def Rabbit_Fib_number(months, offsprings):
    parent, child = 1,1
    for i in range(0, months-1):
        child, parent = parent, parent + (child*offsprings)
    return child

print(Rabbit_Fib_number(10,2))


