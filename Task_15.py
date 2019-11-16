age = int(input("What is you age?: "))

def user_age():
    if age % 2 == 0:
        for i in range(0, age+1, 2):
            print(i)
    else:
        for i in range(1, age+1, 2):
            print(i)


user_age()