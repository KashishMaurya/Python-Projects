import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# to get coordinates of mouse click
# def get_Mouse(x,y):
#     print(x,y)  
# turtle.onscreenclick(get_Mouse)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="What's another state's name?")
    if answer_state is None:
        break
    answer_state = answer_state.title()
    
    if answer_state == "Exit":
        missing_states = [state for state in all_state if state not in guessed_states]
        # states to learn csv
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # If the answer_state is one of the states in all of the states in csv file
    if answer_state in all_state:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle() 
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())

screen.exitonclick()