import turtle
import  pandas
# from cmd import PROMPT
# from multiprocessing.connection import answer_challenge


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
   answer_state = screen.textinput(title =f"{len(guessed_states)}/50 States Correct" ,
                                   prompt= "what's another state's name?").title()
        # print(answer_state)

   if answer_state == "Exit":
      missing_states = []
      for states in all_states:
         if states not in guessed_states:
            missing_states.append(states)
      new_data = pandas.DataFrame(missing_states)
      new_data.to_csv("states.learn_csv")
      break

   if answer_state in all_states:
      guessed_states.append(answer_state)
      t = turtle.Turtle()
      t.hideturtle()
      t.penup()
      state_data = data[data.state == answer_state]
      t.goto(state_data.x.item(), state_data.y.item())
      t.write(answer_state)



# screen.exitonclick()

