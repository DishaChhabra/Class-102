import random
number = random.randint(1,10)
prediction = 5

while prediction>0:
    prediction = prediction - 1 
    guess=int(input('enter a number from 1-10: '))
    if guess==number:
        print('congrats!!')
        break
    else :
        print('the guess is wrong!!')
if prediction == 0:
    print('you lose')
