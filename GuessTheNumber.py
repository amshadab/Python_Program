import random
comp=random.randint(0,10)
print(comp)
i=1
print("You have only 5 attempts")
while(i<=5):
    user=int(input("Guess the no. between 0-10: "))
    if(user==comp):
        print("You are Correct: ",user)
        print(f"Attempt: {i}")
        break
    elif(user>comp):
        print(f"Guess the number lesser than {user}")
    elif(i==5):
        print("You Loose")
    elif(user<comp):
        print(f"Guess the number greater than {user}")
    i=i+1