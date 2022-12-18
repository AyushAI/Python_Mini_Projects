# QUIZ GAME 

print("Welcome to the Game ")

playing = input("Do you want to continue with the game ?---(y/n) : ")

if playing.lower() != 'y':
    quit()

print("Yay ! Let's get started !")
score = 0

answer = input("What does AI stand for ")
if answer.lower() == "artificial intelligence":
    print(" Correct Answer")
    score+=1
else:
    print("Oops Incorrect guess, better luck next time !")


answer = input("What does ML stand for ")
if answer.lower() == "machine learning":
    print(" Correct Answer")
    score+=1
else:
    print("Oops Incorrect guess, better luck next time !")


answer = input("What does CV stand for ")
if answer.lower() == "computer vision":
    print(" Correct Answer")
    score+=1
else:
    print("Oops Incorrect guess, better luck next time !")


answer = input("What does NLP stand for ")
if answer.lower() == "natural language processing":
    print(" Correct Answer")
    score+=1
else:
    print("Oops Incorrect guess, better luck next time !")


answer = input("What are three types of Machine Learning ?")
if answer.lower() == "supervised unsupervised reinforcement":
    print(" Correct Answer")
    score+=1
else:
    print("Oops Incorrect guess, better luck next time !")


print("Total correct guessed questions are  ",score)
print("your score is ",(score//5)*100," %")
print("thanks for playing the game")
