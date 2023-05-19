print("Welcome to my Quiz!")

playing = input("Want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Lets play")    
score = 0


answer = input("What does CPU stand for? "  )
if answer.lower() == "central processing unit":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")    

print('Okay, next question!')

answer = input("What does GPU stand for? "  )
if answer.lower() == "graphics processing unit":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")    

answer = input("What does OS stand for? "  )
if answer.lower() == "operating system":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")    

answer = input("What does PSU stand for? "  )
if answer.lower() == "power supply unit":
    score += 1
    print("Correct!")

print('Congratulations! You passed my computer quiz!')   

print(" You got " + str(score) + " questions correct! " )
print(" You got " + str((score / 4) * 100) + "%.")

