print("Welcome to my Computer Quiz!!")

playing = input('Do you want to play? ')

if playing.lower() != "yes":
    quit()

print("OK, Lets play :)")

score = 0

# 1st Ques

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("oops, you got it wrong :(")

# 2nd Ques

answer = input("What does GPU stand for? ")

if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("oops, you got it wrong :(")

# 3rd Ques

answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("oops, you got it wrong :(")

# 4th Ques

answer = input("What does ROM stand for? ")

if answer.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("oops, you got it wrong :(")

# 5th Ques

answer = input("What does PSU stand for? ")

if answer.lower() == "power supply unit":
    print('Correct!')
    score += 1
else:
    print("oops, you got it wrong :(")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score/5) * 100) + "%.")
