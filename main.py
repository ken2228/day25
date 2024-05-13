from turtle import Screen
import pandas

states_data = pandas.read_csv("50_states.csv")

screen = Screen()

screen.setup(725, 491)
screen.bgpic("blank_states_img.gif")
screen.title("Name the states")


answer_state = screen.textinput(title="Guess the next State",
                                prompt="What's another states name?").capitalize()

if states_data["state"] == answer_state:
    print("found!")
else:
    print("not here")



screen.exitonclick()
