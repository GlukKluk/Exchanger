from tkinter import Tk, Label, Entry, Button, PhotoImage
from exchange import trade, backspace

window = Tk()

window.title("Обмінник")
window.geometry("700x500+600+300")
window.resizable(False, False)
window.config(background="#faf9dc")

main_label = Label(
    window,
    text="Обмін валют",
    font=("Bahnschrift Condensed", 50),
    background="#faf9dc"
)
main_label.place(x=200, y=20)

currency_1 = Label(
    window,
    text="USD",
    font=("Bahnschrift Condensed", 35),
    background="#faf9dc"
)
currency_1.place(x=100, y=150)

pole_1 = Entry(
    window,
    width=15,
    font=("Bahnschrift Condensed", 15),
    justify="center"
)
pole_1.place(x=70, y=220)

currency_2 = Label(
    window,
    text="UAH",
    font=("Bahnschrift Condensed", 35),
    background="#faf9dc"
)
currency_2.place(x=500, y=150)

pole_2 = Entry(
    window,
    width=15,
    font=("Bahnschrift Condensed", 15),
    justify="center"
)
pole_2.place(x=475, y=220)

image = PhotoImage(name="strilki", file="strilki.png")
image = image.subsample(7, 7)

image_label = Label(
    window,
    background="#faf9dc",
    text="Конвертувати",
    image=image
)
image_label.place(x=300, y=170)

knopka_obminu = Button(
    window,
    text="Обміняти",
    font=("Bahnschrift Condensed", 30, "bold"),
    command=lambda: [trade(), backspace()]
)
knopka_obminu.place(x=265, y=330)

window.mainloop()
