def table(n):
    for i in range (1,11):
        print(f"{n}X{i}={n*i}")

user_input=int(input("Enter number:"))
table(user_input)