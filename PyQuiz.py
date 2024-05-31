print("Welocome to PyQuiz")
prize=0
question=["1.Which of the following is the correct extension for Python files?\na .pyth\nb .pt\nc .py",
          "2.How do you start a comment in Python?\na.//\nb.#\nc.*","""3.Which keyword is used to define a function in Python?\na.func\nb.def\nc.define""",
          """4.What is the correct way to create a list in Python?\na.{1, 2, 3}\nb.(1, 2, 3)\nc.[1, 2, 3]""",
          """5.Which of the following is a valid variable name in Python?\na.1variable\nb.variable1\nc.variable-1"""]
answer=["c","b","b","b","b"]
for i in range(len(question)):
    print(question[i])
    ans=input("Enter correct option: ")
    if (ans==answer[i]):
        prize=prize+100
    
print("You win ",prize,"$")
    