def Mortal_Fib_Rabbit(months, alive_months):
    a, b, F = 0, 1, [1,1]
    for i in range(2, months):
        if i < alive_months:
            F.append(F[a]+ F[b])
            a +=1
            b +=1
        elif i == alive_months or i == alive_months+1:
            F.append(F[a]+F[b]-1)
            a+=1
            b+=1
        else:
            F.append(F[a]+F[b]-F[-(alive_months + 1)])
            a +=1
            b +=1
    print("\nThe number of rabit pairs after %s months is %s.\n" %(months, F[months-1]))
    return F

MONTHS = int(input("Enter the number of countdown months:"))
ALIVE_MONTHS = int(input("\nEnther the number of months the rabbit lives for:"))
print(Mortal_Fib_Rabbit(MONTHS, ALIVE_MONTHS))

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# def Rabbit_Fib_number(months, offsprings):
#     parent, child, = 1,1
#     for i in range(0, months-1):
#         child, parent = parent, parent + (child*offsprings)
#     return child
# print(Rabbit_Fib_number(34,3))

# def Rabbit(n,k):
#     import numpy as np
#     P = np.zeros(n)
#     P[0] = 1
#     P[1] = 1
#     for i in range(3, n):
#         P[i] = P[i-1] + P[i-2]*k
#         print(P)

# n = 5
# k = 3
# Rabbit(n,k)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# import numpy as np
# def Mortal_Fib_Rabbit(months, offsprings, alive_months):
#     F = np.zeros(months)
#     F[0], F[1], F[2], F[3], F[4] = 1, 1, 2, 2, 3
#     for n in range(5,months):
#         F[n] = F[n-1] + F[n-2]*offsprings - F[-(alive_months + 1)]
#     print(F[n])
#     return F

# print(Mortal_Fib_Rabbit(10, 2, 3))
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
