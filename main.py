from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard


def game_start():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("SnAkE GaMe")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    score = Scoreboard()

    screen.listen()
    screen.onkey(fun=snake.up, key="Up")
    screen.onkey(fun=snake.down, key="Down")
    screen.onkey(fun=snake.right, key="Right")
    screen.onkey(fun=snake.left, key="Left")

    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.increase_score()

        # Detect collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_is_on = False
            score.game_over()
            time.sleep(1)
            user_input = screen.textinput(title="Play again?", prompt="do you want to play again? Type 'yes' or 'no'")
            if user_input == "yes":
                screen.clear()
                game_start()
            else:
                screen.bye()

        # Detect Collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                score.game_over()
                time.sleep(1)
                user_input = screen.textinput(title="Play again?",
                                              prompt="do you want to play again? Type 'yes' or 'no'")
                if user_input == "yes":
                    screen.clear()
                    game_start()
                else:
                    screen.bye()


game_start()
