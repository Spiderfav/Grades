import random
score = 0 
operation = 0
choice = 0
choice_1 = 0
guess = 0

def create_q( operation, choice, choice_1, guess ):
        choice = random.randint(0,10)
        print(choice)
        choice_1 = random.randint(0,10)
        print(choice_1)
        operation = random.randint(0,2)
        if operation == 0:
                operation = "plus"
                print ("What is,",choice,operation,choice_1,"?")
                guess = input()
                answer( operation, choice, choice_1, guess )
        elif operation == 1:
                operation = "minus"
                print ("What is,",choice,operation,choice_1,"?")
                guess = input()
                answer( operation, choice, choice_1, guess )
        elif operation == 2:
                operation = "times"
                print ("What is,",choice,operation,choice_1,"?")
                guess = input()
                answer( operation, choice, choice_1, guess )


                
                                
def answer( operation, choice, choice_1, guess ):
        if operation == "plus":
                answer = choice + choice_1
                if guess == answer:
                        print("Congrats! You got it right!")
                        score =+1
                        print(answer)
                        print(score)
                else:
                        print("Wrong!")
                        print(answer)
        elif operation == "minus":
                answer = choice - choice_1
                if guess == answer:
                        print("Congrats! You got it right!")
                        score =+1
                        print(answer)
                        print(score)
                else:
                        print("Wrong!")
                        print(answer)
        elif operation == "times":
                answer = choice * choice_1
                if guess == answer:
                        print("Congrats! You got it right!")
                        score =+1
                        print(answer)
                        print(score)
                else:
                        print("Wrong!")
                        print(answer)
                







print("Welcome to the quiz!")
name = input("Enter Your Name: ")
print("Hello,",name,", let's start the quiz!")
create_q( operation, choice, choice_1, guess )
