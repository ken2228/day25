from turtle import Screen, Turtle
import pandas

states_data = pandas.read_csv("50_states.csv")


def get_coords_from_state(state_name: str, dataset: pandas.DataFrame):
    """ Returns a tuple with the x and y coordinate of a given state name
        Does not check if the state exists in the dataset"""
    row = dataset.loc[dataset["state"] == state_name]
    return row.iloc[0, 1], row.iloc[0, 2]


screen = Screen()
t = Turtle()
states_found = 0

# setup screen
screen.setup(725, 491)
screen.bgpic("blank_states_img.gif")
screen.title("Name the states")
# setup turtle
t.hideturtle()
t.pu()


def write_name_at_location(state: str, location: tuple[float, float]):
    t.goto(location)
    t.write(arg=state)


while states_found < 50:
    answer_state = screen.textinput(title=f"{states_found} of 50 states found",
                                    prompt="What's another states name?").title()

    if answer_state == "Exit":
        break
    # check if the user gave us a valid state
    elif answer_state in states_data["state"].values:  # == answer_state:
        print(f"found! {answer_state}")
        coords = get_coords_from_state(answer_state, states_data)
        write_name_at_location(answer_state.capitalize(), coords)
        # states_data =
        states_data = states_data.drop(states_data[(states_data.state == answer_state)].index)
        states_found += 1
    else:
        print("not here")

header = ["state"]
# states_to_learn.csv
states_data.to_csv("states_to_learn.csv", columns=header, index=False, header=False)
# screen.exitonclick()
