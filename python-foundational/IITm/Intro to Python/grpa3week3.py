n = str(input())
x, y = 0, 0

while n != 'STOP':
    if n == 'UP':
        y += 1
    elif n == 'DOWN':
        y -= 1
    elif n == 'RIGHT':
        x += 1
    elif n == 'LEFT':
        x -= 1
    n = str(input())
if x < 0:
    x = -1*x
if y < 0:
    y = -1*y

distance = x+y
print(distance)
