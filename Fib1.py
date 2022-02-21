countdownTimer = 81 
numberOfMonthsRabbitsLiveFor = 19
startingNumberOfRabbits = 2

indexOne = 0
indexTwo = 1
fibonacciRabbit = [1, 1]

while startingNumberOfRabbits < countdownTimer:
    #Always adding the two most recent numbers
    if startingNumberOfRabbits < numberOfMonthsRabbitsLiveFor:
        print ("Less")
        #Add the two most recent numbers together
        fibonacciRabbit.append(fibonacciRabbit[indexOne] + fibonacciRabbit[indexTwo])
        print (fibonacciRabbit[indexOne])
        print (fibonacciRabbit[indexTwo])
        print (fibonacciRabbit)
        indexOne += 1
        indexTwo += 1
    elif startingNumberOfRabbits == numberOfMonthsRabbitsLiveFor or startingNumberOfRabbits == numberOfMonthsRabbitsLiveFor+1:
        print ("Equal")
        #Remove one of the rabbits
        fibonacciRabbit.append(fibonacciRabbit[indexOne] + fibonacciRabbit[indexTwo] - 1)
        print (fibonacciRabbit[indexOne])
        print (fibonacciRabbit[indexTwo])
        print (fibonacciRabbit)
        indexOne += 1
        indexTwo += 1
    else:
        print ("More")
        #remove the number of rabbits equal to the fourth most recent (i.e. 3 months a rabbit dies)
        fibonacciRabbit.append((fibonacciRabbit[indexOne] + fibonacciRabbit[indexTwo]) - fibonacciRabbit[-(numberOfMonthsRabbitsLiveFor + 1)])
        print (fibonacciRabbit[indexOne])
        print (fibonacciRabbit[indexTwo])
        print (fibonacciRabbit)
        indexOne += 1
        indexTwo += 1

    startingNumberOfRabbits += 1

#Print the number of rabbits equal to the end of the countdowntimer
print (fibonacciRabbit[(countdownTimer - 1)])
