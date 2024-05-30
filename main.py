import tkinter
from tkinter import *
from tkinter import messagebox

from base import questions, anwsers, nr, possible_signs


class GUI_methods:
    k = 0

    def increase_k(self):
        if self.k <= nr - 2:
            self.k = self.k + 1
            return self.k
        else:
            return self.k

    def decrease_k(self):
        if 0 < self.k < nr:
            self.k = self.k - 1
            return self.k
        else:
            return self.k


g = GUI_methods()


def increase_question():
    question_place.config(state='normal')
    k = g.increase_k()
    question_place.delete(1.0, "end")
    question_place.insert(1.0, questions[k])
    question_place.config(state=DISABLED)


def decrease_question():
    question_place.config(state='normal')
    k = g.decrease_k()
    question_place.delete(1.0, "end")
    question_place.insert(1.0, questions[k])
    question_place.config(state=DISABLED)


users_anwsers = [None for x in range(nr)]


def error_message():
    sign = anwser_place.get("1.0")
    if possible_signs(sign) is False:
        messagebox.showwarning("UWAGA", "Nie wybrałeś opcji a,b,c")
        # messagebox.showinfo("Nie wybrałeś opcji a,b lub c")
    else:
        users_anwsers[g.k] = sign.lower()


def show_result():
    user_score = 0
    for i in range(anwsers.__len__()):
        if anwsers[i] == users_anwsers[i]:
            user_score += 1
    messagebox.showinfo('Wynik', f'Twój wynik to : {user_score} na {nr} mozliwych ')


window = tkinter.Tk()

window.minsize(700, 400)
window.maxsize(700, 400)
width = 700
height = 400

window.geometry("%dx%d" % (width, height))
bgimg = PhotoImage(file="bg.png")
img_bg = Canvas(window, width=window.winfo_width(), height=window.winfo_height())
img_bg.pack(fill='both', expand=True)
img_bg.create_image(0, 0, image=bgimg, anchor='nw')

question_place = Text(window, height=10,  # changed from window
                      width=80,
                      fg='purple',
                      bg='pink'
                      )
question_place.insert(END, questions[0])
question_place.config(state=DISABLED)
question_place.place(x=30, y=50)

anwsers_place = Text(window, height=1,
                     width=23, bg="pink", fg='purple')
anwsers_place.insert(END, "Miejsce na odpowiedź: ")
anwsers_place.config(state=DISABLED)
anwsers_place.place(x=20, y=220)

anwser_place = Text(window, height=1, width=1, bg='pink')
anwser_place.place(x=200, y=220)

check_anwser = Button(window, text="Zatwierdź", width=8, command=lambda: error_message())
check_anwser.place(x=220, y=218)

x_pl = 290

next_quesiton = Button(window, text="nastepne pytanie", width=14, command=lambda: increase_question())
next_quesiton.place(x=x_pl, y=218)


previous_case = Button(window, text="poprzednie pytanie", width=14, command=lambda: decrease_question())
previous_case.place(x=x_pl + 110, y=218)

score = Button(window, text="Wyswietl wynik:", width=14, command=lambda: show_result())
score.place(x=x_pl + 220, y=218)
window.mainloop()
