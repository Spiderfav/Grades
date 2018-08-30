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

out_file = open(classs.upper() +".txt", "a+")
out_file.write( name.upper()+","+str(score))
out_file.close()

print("Now the averages!")
ClassA = open(classs.upper() +".txt", "r")
ClassA = ClassA.read()
items = ClassA.split(',')
lenght = len(items)
length = lenght-1
ave_list = {}

for i in range (0,length,2):
     name = items[i]
     score = int(items[i+i])
     if name not in ave_list:
          ave_list[name] = []
     ave_list[name].append(score)
     if len(ave_list[name]) >3:
          ave_list[name].pop(0)

print("Here are the averages:")
print(ave_list)
print("\n")

averages = {}
for i in range(0,length,2):
     name = items[i]
     score = int(items[i+1])
     if name not in averages:
          total = sum(ave_list[name])/len(ave_list[name])
          total = round(total)
          averages[name] = total

sorted_ave = sorted(averages.items(), key = lambda x: x[1], reverse = True)
print("And here is the sorted dictionary!")
print(sorted_ave) 

###Write score to a text file
##Dictionary2 = {}
##
##Dictionary2.update({name.upper(): score})
##
##
##Dictionary = {}
##with open(classs.upper() +".txt") as f:
##    for l in f:
##          Dictionary[l[0]] = l[1]
##          print(Dictionary)


