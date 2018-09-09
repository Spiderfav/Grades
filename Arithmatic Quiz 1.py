import collections
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
for x in range(10):
    #Select a random number from one to ten
     choice = random.randint(0,10)
    #Select a random number from one to ten
     choice_1 = random.randint(0,10)
     operation = random.randint(0,2)

#Select an operation at random
     if operation == 0:
         #If the operation chosen by the program is addition:
             operation = "plus"
             #With the two numbers randomly chosen by the program, formulate the question
             print ("What is,",choice,operation,choice_1,"?")
             guess = int(input())
             answer = choice + choice_1
#            If the answer is correct:
             if guess == answer:
                 #Print message
                     print("Congrats! You got it right!")
                     #If the answer was right add one to score
                     score = score + 1
                     print("The score now is:",score)

             else:
                    #Else print wrong
                     print("Wrong!")
                     print("The answer was:",answer)

     elif operation == 1:
        #If the operation chosen by the program is subtraction:
             operation = "minus"
             #Formulate question
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

# This is actually a very intelligent line because
#       it does different things depending on the situtation
#           1st: If there is a file with the name stored in the class, append name and score to it
#           2nd: If there is no file with name stored in class, make file and add the info
out_file = open(classs.upper() +".txt", "a+")
out_file.write( name.upper() + "," + str(score) + ",")
out_file.close()

print("Now the averages!")
#Opens the file where score was just saved
ClassA = open(classs.upper() +".txt", "r")
ClassA = ClassA.read()
# Splits into a dictionary using the character to differenciate
items = ClassA.split(',')
#
lenght = len(items)
#
length = lenght-1
# Creates empty dictionary to store the averages later
ave_list = {}

#
for i in range (0,length,2):
    # Store the name from the file into the variable
     name = items[i]
     # Score is one position greater than the name so take it as an integer
     score = int(items[i+1])
     # If the position is not in the list, add it
     if name not in ave_list:
          ave_list[name] = []
     ave_list[name].append(score)
     # If there is more than three scores for one name, destroy/pop the first
     if len(ave_list[name]) >3:
          ave_list[name].pop(0)

print("Here are the all results results:")
#Print the averages
print(ave_list)
#Line break
print("\n")

# Create a new dictionary called averages
averages = {}

for i in range(0,length,2):
    # Store the name from the file into the variable
     name = items[i]
     # Score is one position greater than the name so take it as an integer
     score = int(items[i+1])
     #If the name is not in the averages
     if name not in averages:
         # The total is all the scores divided by how many there are, which is three
          total = sum(ave_list[name])/len(ave_list[name])
          # Round the total so we have a whole number
          total = round(total)
          averages[name] = total

#Sort the items in the list,
sorted_ave = sorted(averages.items())
print("And here is the sorted averages!")
print(sorted_ave)
