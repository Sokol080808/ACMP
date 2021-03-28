from tkinter import *

root = Tk()
root.title("ACMP 670")

N = StringVar()
get_N_entry = Entry(textvariable = N, width = 25)
get_answer_button = Button(width = 21, text = "Получить ответ", command = lambda: get_answer(int(N.get())))
answer_label = Label(width = 23)

def get_answer(N):
    i = 0
    number = 0
    while i < N:
        number += 1
        if len(str(number)) != len(set(str(number))):
            continue
        i += 1  

    answer_label['text'] = str(number)

    
get_N_entry.pack()
get_answer_button.pack()
answer_label.pack()
root.mainloop()
