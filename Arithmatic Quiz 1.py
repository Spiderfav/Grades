import random

#Set all the variables
score, operation, choice, choice_1, guess = 0, 0, 0, 0, 0

print("Welcome to the quiz!")
name = input("Enter Your Name: ")
print("Hello,",name,"!")
print ("Now, what class are you in?")
classs = input()
#Name and class is to be used later
print("Just to make sure, you are:",name,"and your class is:",classs)
print("Let's start the quiz!")

#Start a for loop to create the questions
for x in range(9):
    #Select a random number from one to ten
     choice = random.randint(0,10)
    #Select a random number from one to ten
     choice_1 = random.randint(0,10)
     operation = random.randint(0,2)

#Select an operation at random
     if operation == 0:
             operation = "plus"
             print ("What is,",choice,operation,choice_1,"?")
             guess = int(input())
             answer = choice + choice_1

             if guess == answer:
                     print("Congrats! You got it right!")
                     #If the answer was right add one to score
                     score = score + 1
                     print("The score now is:",score)

             else:
                    #Else print wrong
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
                     score = score + 1
                     print("The score now is:",score)
             else:
                     print("Wrong!")
                     print("The answer was:",answer)


#Print the score the user got
print("Your total for the test was:",score,"/10.")
#Write score to a text file

out_file = open(classs + name +".txt", "wt")
out_file.write("Score:",str(score))
out_file.close()
