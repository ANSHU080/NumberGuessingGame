from random import randint
a=randint(1,10)
count=0
score=0
while count<10:
    try:
        n = int(input("guess a number: "))
        if n in range(1,11):
            if n==a:
                print('what agenius ')
                score+=1
            else:
                print("OOPS!! wrong guess")
        else:
            print("enter a number between 1-10")
    except ValueError:
        print("enter a number")
    count+=1
print(f"GAME OVER! \n your score is {score} ")

