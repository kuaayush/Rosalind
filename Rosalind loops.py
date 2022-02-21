greetings = 1
while greetings <= 5:
  print ("Hello! " * greetings)
  greetings = greetings + 1
print()

# If you want to repeat an action several times, you can use a while loop.
# Here, the initial value of greetings is 1, so The program prints Hello once.
# After print statement, it adds 1 to the pre-existing value of greetings.
# The value of greetings is then passed to the condition thats present beside 'while'.
# If the condition is satisfied the loop runs again.
# After printing Hello 5 times, greetings becomes 6,and the while condition of greeting <= 5 is no longer satisfied,
# so the program would come out of the while loop(c0ntinue past the while loop).

names = ['Alice', 'Bob', 'Charley']
for name in names:
  print ("Hello, " + name + "!")
print()


# Two positive integers a and b (a < b < 10000)
# Find the sum of all odd integers from a through b, inclusively.
a = 4132
b = 9014
sum = 0
for i in range(a, b+1):
    if i % 2 == 1:
        sum = sum +i
print(sum)

        
