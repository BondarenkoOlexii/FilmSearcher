from tkinter import *
from tkinter import ttk
import main
from main import api_request, films_titles
import random



def submit_button():

    list_of_getting = []
    list_of_var = [var1, var2, var3, var4, var5, var6, var7, var8]
    labels = [28, 18, 35, 12, 14, 53, 99, 10751]
    for i in range(len(list_of_var)):
        if list_of_var[i].get() != 0:
            list_of_getting.append(labels[i])

    js_file = main.api_request(list_of_getting, 1, filter_buttons_check())

    title_list = main.films_titles(js_file)

    list_box(title_list)

    clear_checkbutton()


def clear_checkbutton():
    check_buttons = [checkbutton_1, checkbutton_2, checkbutton_3, checkbutton_4,
                     checkbutton_5, checkbutton_6, checkbutton_7, checkbutton_8,
                    ]

    for btn in check_buttons:
        if btn.winfo_exists():
            btn.deselect()


def list_box(list_of_names_films):
    list_1.delete(0, END)
    for i in list_of_names_films:
        list_1.insert(END, i)

def filter_buttons_check():
    dict_of_filters_var = {
        1: "popularity.desc",
        2: "release_date.desc",
        3: "revenue.desc",
        4: "vote_count.desc"
    }
    filters_to_send = 0
    filter = Var_Filter.get()
    for i in dict_of_filters_var:
        if i == filter:
            filters_to_send = dict_of_filters_var[i]

    return filters_to_send



#  MAIN WINDOW
root = Tk()
root.title("Window")
root.geometry("1280x720")
root.resizable(width=True, height=True)


#  NOTEBOOK AND 3 FRAMES
notes = ttk.Notebook(width=1280)
notes.place(x=50, y=0)

frame_1 = ttk.Frame(notes, width=1280, height=720)
# frame_2 = ttk.Frame(notes, width=600)
# frame_3 = ttk.Frame(notes)

notes.add(frame_1, text="Фрейм 1")
# notes.add(frame_2, text="Фрейм 2")
# notes.add(frame_3, text="Фрейм 3")


# PLACE FOR NAMES FILMS
list_1 = Listbox(frame_1, selectmode=EXTENDED, width=100, height=60, font=7)
list_1.place(x=550, y=0)


# Genres IntVar Checkbuttons
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()

# Filter IntVar Radiobuttons
Var_Filter = IntVar()


# Genres Checkbutton
checkbutton_1 = Checkbutton(frame_1, text="Action", variable=var1, onvalue=1, offvalue=0)
checkbutton_2 = Checkbutton(frame_1, text="Drama", variable=var2, onvalue=1, offvalue=0)
checkbutton_3 = Checkbutton(frame_1, text="Comedy", variable=var3, onvalue=1, offvalue=0)
checkbutton_4 = Checkbutton(frame_1, text="Adventure", variable=var4, onvalue=1, offvalue=0)
checkbutton_5 = Checkbutton(frame_1, text="Fantasy", variable=var5, onvalue=1, offvalue=0)
checkbutton_6 = Checkbutton(frame_1, text="Thriller", variable=var6, onvalue=1, offvalue=0)
checkbutton_7 = Checkbutton(frame_1, text="Sci-Fi", variable=var7, onvalue=1, offvalue=0)
checkbutton_8 = Checkbutton(frame_1, text="Family", variable=var8, onvalue=1, offvalue=0)

checkbutton_1.place(x=40, y=50)
checkbutton_2.place(x=40, y=100)
checkbutton_3.place(x=40, y=150)
checkbutton_4.place(x=40, y=200)
checkbutton_5.place(x=40, y=250)
checkbutton_6.place(x=40, y=300)
checkbutton_7.place(x=40, y=350)
checkbutton_8.place(x=40, y=400)


# Sorter Checkbutton
radio_popular = Radiobutton(frame_1, text='Popular', variable=Var_Filter, value=1, command=filter_buttons_check)
radio_recent = Radiobutton(frame_1, text='Recent', variable=Var_Filter, value=2, command=filter_buttons_check)
radio_votes = Radiobutton(frame_1, text='Most Voted', variable=Var_Filter, value=4, command=filter_buttons_check)


radio_popular.place(x=280, y=200)
radio_recent.place(x=280, y=250)
radio_votes.place(x=280, y=300)


Submit_button = Button(frame_1, text="Submit", command=lambda: submit_button(), width=25, height=10)
Submit_button.place(x=50, y=500)



root.mainloop()