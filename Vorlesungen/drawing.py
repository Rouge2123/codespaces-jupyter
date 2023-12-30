import turtle

# ws = turtle.Turtle()
# ws.speed(0)
# ws.color("cyan")

# for j in range (1,100):
#     for i in range (1,6):
#         ws.left (144)
#         ws.forward (200)
#         ws.left (5)

# turtle.done()

wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")
skk = turtle.Turtle()


def sqrfunc(size):
    for i in range(4):
        skk.fd(size)
        skk.left(90)
        size = size + 5

k = 20
for i in range(8):
    sqrfunc(6 + k)
turtle.done()