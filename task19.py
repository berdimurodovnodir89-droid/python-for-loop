ball = int(input(f' Ball 1:'))
max_ball = ball
 
for i in range(2,6) :
    ball = int(input(f' Ball 2:'))
    if ball < max_ball :
     max_ball = ball

print(max_ball)
  