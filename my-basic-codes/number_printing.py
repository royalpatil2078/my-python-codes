# Taking input from the user
try:
    n = int(input("Enter a number: "))

# Printing numbers from 1 to n
    for i in range(1, n + 1):
        print(i)

except ValueError:
    print("Entered wrong value")

finally :
    print("Project completed")