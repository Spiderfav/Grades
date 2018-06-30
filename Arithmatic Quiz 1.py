import random
score = 0
operation = 0
choice = 0
choice_1 = 0
guess = 0
#Just to test


def create_q( operation, choice, choice_1, guess):
        choice = random.randint(0,10)
        choice_1 = random.randint(0,10)
        operation = random.randint(0,2)

        if operation == 0:
                operation = "plus"
                answer( operation, choice, choice_1, guess, score )

        elif operation == 1:
                operation = "minus"
                answer( operation, choice, choice_1, guess, score )

        elif operation == 2:
                operation = "times"
                answer( operation, choice, choice_1, guess, score )




def answer( operation, choice, choice_1, guess, score ):

        if operation == "plus":
                print ("What is,",choice,operation,choice_1,"?")
                guess = int(input())
                answer = choice + choice_1

                if guess == answer:
                        print("Congrats! You got it right!")
                        score += 1
                        print("The score now is:",score)

                else:
                        print("Wrong!")
                        print("The answer was:",answer)

        elif operation == "minus":
                print ("What is,",choice,operation,choice_1,"?")
                guess = int(input())
                answer = choice - choice_1

                if guess == answer:
                        print("Congrats! You got it right!")
                        score += 1
                        print("The score now is:",score)

                else:
                        print("Wrong!")
                        print("The answer was:",answer)

        elif operation == "times":
                print ("What is,",choice,operation,choice_1,"?")
                guess = int(input())
                answer = choice * choice_1

                if guess == answer:
                        print("Congrats! You got it right!")
                        score += 1
                        print("The score now is:",score)

                else:
                        print("Wrong!")
                        print("The answer was:",answer)









print("Welcome to the quiz!")
name = input("Enter Your Name: ")
print("Hello,",name,", let's start the quiz!")
for x in range(9):
    create_q( operation, choice, choice_1, guess)

print("Your total for the test was:",score,"/10.")
