from tkinter import *

root = Tk()
root.title("ACMP 253")

start_time = StringVar()
end_time = StringVar()

start_time_entry = Entry(textvariable = start_time, width = 25)
end_time_entry = Entry(textvariable = end_time, width = 25)
get_answer_button = Button(width = 21, text = "Получить ответ", command = lambda: get_answer(list(map(int, start_time.get().split())), list(map(int, end_time.get().split()))))
answer_label = Label(width = 23)

def get_answer(start_time, end_time):
    if 0 <= start_time[0] < 24 and 0 <= start_time[1] < 60 and 0 <= end_time[0] < 24 and 0 <= end_time[1] < 60:
        counter = 0

        time1 = start_time[0] * 60 + start_time[1]
        time1_1 = time1 + (0 - time1 % 30) % 30
        time2 = end_time[0] * 60 + end_time[1]

        if time1 <= time2 and time1_1 > time2:
            answer_label['text'] = "0"
        else:
            time1 = time1_1
            if time2 < time1:
                time2 += 60 * 24
            for i in range(time1, time2 + 1, 30):
                if i % 60 == 30:
                    counter += 1
                else:
                    if (i//60) % 12 != 0:
                        counter += (i // 60) % 12
                    else:
                        counter += 12

            answer_label['text'] = str(counter)
    else:
        answer_label['text'] = "Неправильно введено время"

start_time_entry.pack()
end_time_entry.pack()
get_answer_button.pack()
answer_label.pack()
root.mainloop()
