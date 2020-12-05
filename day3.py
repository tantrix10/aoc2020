with open("data_day_3.txt", "r") as dat:
    data = dat.read()

data = [row for row in data.split('\n') if row != '']
width = len(data[0])
depth = len(data)

# Who has time for recurrsion, it's christmas
def counter(x_jump, y_jump):
    x,y,total=0,0,0
    while y < depth:
        total += 1 if data[y][x%width] == '#' else 0
        x += x_jump
        y += y_jump
    return total



print(f"Part 1 anser: {counter(3,1)}")
x1 = counter(1,1)
x2 = counter(3,1)
x3 = counter(5,1)
x4 = counter(7,1)
x5 = counter(1,2)
print(f"Part 2 answser: {x1*x2*x3*x4*x5}")
