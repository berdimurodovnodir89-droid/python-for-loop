

ball = int(input('ball 1 :'))
    
min_ball = ball
max_ball = ball

for i in range(2,5+1) :
   ball = int(input(f'ball {i}:'))
    
   if ball > max_ball :
    max_ball = ball
   if ball < min_ball :
    min_ball = ball

print(f'max_ball = {max_ball}, min_ball = {min_ball}')