import random
score, operation, choice, choice_1, guess = 0, 0, 0, 0, 0

print("Welcome to the quiz!")
name = input("Enter Your Name: ")
print("Hello,",name,", let's start the quiz!")
for x in range(9):
     choice = random.randint(0,10)
     choice_1 = random.randint(0,10)
     operation = random.randint(0,2)

     if operation == 0:
             operation = "plus"
             print ("What is,",choice,operation,choice_1,"?")
             guess = int(input())
             answer = choice + choice_1

             if guess == answer:
                     print("Congrats! You got it right!")
                     #global score
                     score = score + 1
                     print("The score now is:",score)

             else:
                     print("Wrong!")
                     print("The answer was:",answer)

     elif operation == 1:
             operation = "minus"
             print ("What is,",choice,operation,choice_1,"?")
             guess = int(input())
             answer = choice - choice_1

             if guess == answer:
                     print("Congrats! You got it right!")
                     score = score + 1
                     print("The score now is:",score)

             else:
                     print("Wrong!")
                     print("The answer was:",answer)

     elif operation == 2:
             operation = "times"
             print ("What is,",choice,operation,choice_1,"?")
             guess = int(input())
             answer = choice * choice_1

             if guess == answer:
                     print("Congrats! You got it right!")
                     #global score
                     score = score + 1
                     print("The score now is:",score)
             else:
                     print("Wrong!")
                     print("The answer was:",answer)


print("Your total for the test was:",score,"/10.")
