import random
print("Rock-Paper-Scissor")
l=["Rock","Paper","Scissor"]
user=input("Enter your choice: ").capitalize()
comp=random.choice(l)

if (user==comp):
    print("Computer: ",comp)
    print("You: ",user)
    print("Tie")
elif (user==l[0] and comp==l[1] or user==l[1] and comp==l[2]  or user==l[2] and comp==l[0]):
  print("Computer: ",comp)
  print("You: ",user)
  print("Computer Win")
else:
   print("Computer: ",comp)
   print("You: ",user)
   print("You Win")

   
   
   
    