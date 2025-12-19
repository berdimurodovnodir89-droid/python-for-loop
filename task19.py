ball = int(input(f' Ball 1:'))
min_ball = ball

for i in range(2,6) :
    ball = int(input(f' Ball 2:'))
    if ball < min_ball :
     min_ball = ball

print(min_ball)

for i in range(2,6) :
    ball = int(input(f' Ball 2:'))
    if ball > max_ball :
     max_ball = ball
print(max_ball)

print(max_ball + min_ball)
