import random
secret = random.randint(1,10)
print('--I love Python--')
temp=input("Guess a number: ")
guess=int(temp)
while guess !=secret:
    temp=input("Wrong ! Guess again ?")
    guess=int(temp)
    if guess == secret:
        print("You are right!")
    else:
        if guess >secret:
          print("Wrong, the answer is too big.")
        else:
          print("Wrong, the answer is too small.")     
print("Game is over.")
