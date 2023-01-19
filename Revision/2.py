# Write a program to iterate the first 10 numbers and in each iteration, 
# print the sum of the current and previous number.

for i in range(10):
    print("Current:", i, "Previous:", i - 1, "Sum:", i + (i - 1))