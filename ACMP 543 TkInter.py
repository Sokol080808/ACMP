from tkinter import *

root = Tk()
root.title("ACMP 543")

def get_answer(variables):
    N, w, d, P = map(int, variables.split())
    correct_weight = N * (N - 1) * w // 2
    error = correct_weight - P
    if error == 0:
        answer = N
    else:
        answer = error//d
    answer_label['text'] = str(answer)

variables = StringVar()
get_variables_entry = Entry(textvariable = variables, width = 25)
get_answer_button = Button(width = 21, text = "Получить ответ", command = lambda: get_answer(variables.get()))
answer_label = Label(width = 23)


get_variables_entry.pack()
get_answer_button.pack()
answer_label.pack()
root.mainloop()
