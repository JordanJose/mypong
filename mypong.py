# Jucimar Jr 2019
# pong em turtle python https://docs.python.org/3.3/library/turtle.html
# baseado em http://christianthompson.com/node/51
# fonte Press Start 2P https://www.fontspace.com/codeman38/press-start-2p
# som pontuação https://freesound.org/people/Kodack/sounds/258020/

from sys import argv
import turtle
import os
from random import randint

# Velocidade inicial
INITIAL_SPEED = 0.5
# A cada rebatida a bola aumenta em 3,25% a velocidade
SPEED_INCREASE = 0.0075

# desenhar tela de jogo
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# desenhar tela de inicio

begin = turtle.Turtle()
begin.shape("square")
begin.color("white")
begin.shapesize(stretch_wid=10, stretch_len=5)
begin.speed(0)
begin.penup()
begin.hideturtle()
sec = 2
begin.write("Press [ENTER] to start a game", align="center",
            font=("Press Start 2P", 16, "normal"))

screen.textinput("BEGIN", "Press ENTER")
screen.reset()

# desenhar raquete 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

# desenhar raquete 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# desenhar bola
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = INITIAL_SPEED
ball.dy = INITIAL_SPEED

# pontuação
score_1 = 0
score_2 = 0

# head-up display da pontuação
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 260)
hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))

# Tela de vitória
win = turtle.Turtle()
win.speed(0)
win.shape("square")
win.color("white")
win.shapesize(stretch_wid=10, stretch_len=5)
win.penup()
win.hideturtle()
win.goto(0, 0)


# mover raquete 1
def paddle_1_up():
    y = paddle_1.ycor()
    if y < 250:
        y += 20
    else:
        y = 250
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor()
    if y > -250:
        y += -20
    else:
        y = -250
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    if y < 250:
        y += 20
    else:
        y = 250
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    if y > -250:
        y += -20
    else:
        y = -250
    paddle_2.sety(y)

# mapeando as teclas
screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
if len(argv) < 2:
    screen.onkeypress(paddle_2_up, "Up")
    screen.onkeypress(paddle_2_down, "Down")

while True:
    screen.update()

    # movimentação da bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Pegando posições da bola e da segunda raquete
    ball_position = ball.ycor()
    paddle_2_position = paddle_2.ycor()

    # colisão com parede superior
    if ball.ycor() > 290:
        os.system("aplay bounce.wav&")
        ball.sety(290)
        ball.dy *= -1

    # colisão com parede inferior
    if ball.ycor() < -280:
        os.system("aplay bounce.wav&")
        ball.sety(-280)
        ball.dy *= -1

    # colisão com parede esquerda
    if ball.xcor() < -390:
        score_2 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=(
            "Press Start 2P", 16, "normal"))
        os.system("aplay 258020__kodack__arcade-bleep-sound.wav&")
        ball.goto(0, 0)
        # Reiniciando a velocidade
        ball.dx = INITIAL_SPEED
        ball.dy = INITIAL_SPEED
        # Inicio do jogo aleatorio
        ball.dx *= 1
        if randint(0, 1) == 0:
            ball.dy *= -1

    # colisão com parede direita
    if ball.xcor() > 390:
        score_1 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=(
            "Press Start 2P", 16, "normal"))
        os.system("aplay 258020__kodack__arcade-bleep-sound.wav&")
        ball.goto(0, 0)
        # Reiniciando a velocidade
        ball.dx = INITIAL_SPEED
        ball.dy = INITIAL_SPEED
        ball.dx *= -1
        if randint(0, 1) == 0:
            ball.dy *= -1

    # colisão com raquete 1
    if (ball.xcor() < -330 and ball.ycor() < paddle_1.ycor() + 50 and
            ball.ycor() > paddle_1.ycor() - 50):
        division_paddle = (abs(ball.ycor()) - abs(paddle_1.ycor()))
        pos_neg = 1 if ball.dy >= 0 else -1
        if division_paddle < 1 and division_paddle > 0:  # caso a bola bata no meio da raquete
            ball.dy = 0
        else:
            # Usando 12.5 pois eh o resultado de 100/8
            division_paddle //= 12.5  # divisao inteira
            # com isso saberei qual quadrante da bola bateu
            division_paddle += 1
            if division_paddle == 1:
                ball.dy = pos_neg*0.02
            elif division_paddle == 2:
                ball.dy = pos_neg*0.07
            elif division_paddle == 3:
                ball.dy = pos_neg*0.1
            elif division_paddle == 4:
                ball.dy = pos_neg*0.2
            else:
                ball.dy = pos_neg*0.3
        ball.dx *= -1
        ball.setx(-330)
        if (ball.dx < 0):
            ball.dx -= SPEED_INCREASE
        else:
            ball.dx += SPEED_INCREASE
        os.system("aplay bounce.wav&")

    # colisão com raquete 2
    if (ball.xcor() > 330 and ball.ycor() < paddle_2.ycor() + 50 and
            ball.ycor() > paddle_2.ycor() - 50):
        division_paddle = (abs(ball.ycor()) - abs(paddle_2.ycor()))
        pos_neg = 1 if ball.dy >= 0 else -1
        if division_paddle < 1 and division_paddle > 0:
            ball.dy = 0
        else:
            division_paddle //= 12.5
            division_paddle += 1
            if division_paddle == 1:
                ball.dy = pos_neg*0.02
            elif division_paddle == 2:
                ball.dy = pos_neg*0.07
            elif division_paddle == 3:
                ball.dy = pos_neg*0.1
            elif division_paddle == 4:
                ball.dy = pos_neg*0.2
            else:
                ball.dy = pos_neg*0.3
        ball.setx(330)
        ball.dx *= -1
        if (ball.dx < 0):
            ball.dx -= SPEED_INCREASE
        else:
            ball.dx += SPEED_INCREASE
        os.system("aplay bounce.wav&")

    # Pontuação limite
    if score_1 == 5 or score_2 == 5:
        winner = 'player 1' if score_1 > score_2 else 'player 2'
        score_1 = score_2 = 0
        win.write("Vitoria {}".format(winner), align="center",
                  font=("Press Start 2P", 16, "normal"))
        screen.textinput("Vitoria {}".format(winner),
                         "Press [ENTER] to restart")
        win.clear()
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=(
            "Press Start 2P", 24, "normal"))
        screen.listen()

    # módulo 1 jogador
    if len(argv) == 2:
        if str(argv[1]) == "-1":
            if ball_position > paddle_2_position:
                if paddle_2_position > 250:
                    paddle_2.sety(paddle_2.ycor() + 0)
                else:
                    paddle_2.sety(paddle_2.ycor() + 0.3)
            elif ball_position == paddle_2_position:
                paddle_2.sety(paddle_2.ycor())
            else:
                if paddle_2_position < -250:
                    paddle_2.sety(paddle_2.ycor() + 0)
                else:
                    paddle_2.sety(paddle_2.ycor() + -0.3)
