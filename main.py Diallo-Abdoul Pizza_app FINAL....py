# Abdoul Diallo
# Final Project Pizza application
# This code creates a simple GUI pizza application with a listbox of
# available pizza, radio buttons to select the pizza size, the pizza toppings,
# an order button to place the order, and a label to show the order summary.
# When the user clicks the order button, the order will retrieve the summary of the order.

from tkinter import *
from tkinter import messagebox
# Creation of the main window of the pizza app.
pizza=Tk()
pizza.geometry("600x500")
pizza.title("My pizza app")

# Creation of the space name entry for the individual order.
name_label = Label(pizza, text="What is your name?: ")
name_label.grid(row=0, column=0)

name_entry = Entry(pizza, width=30)
name_entry.grid(row=0, column=1)

# Creation of the address space for the individual address entry.
address_label = Label(pizza, text="What is your address?: ")
address_label.grid(row=1, column=0)

address_entry = Entry(pizza, width=30)
address_entry.grid(row=1, column=1)

# Creation of phone number entry for the individual order.
phone_label = Label(pizza, text="What is your phone number?: ")
phone_label.grid(row=2, column=0)

phone_entry = Entry(pizza, width=30)
phone_entry.grid(row=2, column=1)

# Creation of the pizza list entry choices ( pizza list box).
my_pizza_list = ["pepperoni", "Cheese", "Mushroom", "steak", "Garlic"]

# Creation of buttons selection and background app.
pizza_list = Listbox(pizza, selectmode=MULTIPLE, bg="black", fg="red")
pizza_list.grid(row=4, column=1)
for item in my_pizza_list:
    pizza_list.insert(0, item)

# definition of pizza list items.
def add_pizza():
    result = ""
    for item in pizza_list.curselection():
        result = result + str(pizza_list.get(item)) + "\n"

        add_lbl.config(text = "your pizza selection: " + "\n" + result)

add_lbl = Label(pizza, text="")
add_lbl.grid(row=5, column=1)

# Creation of pizza command buttons
add_button = Button(pizza, text="add pizza", command= add_pizza)
add_button.grid(row=5, column=0)

# definition of name, address, and phone number entry.
def check():
    text1= name_entry.get()
    new_lbl = Label(pizza, text="Name: " + text1)
    new_lbl.grid(row=5, column=2)
# Definition of address text entry
    text2 = address_entry.get()
    new_lbl2 = Label(pizza, text="Address" + text2)
    new_lbl2.grid(row=6, column=2)
# Definition of phone text entry
    text3 = phone_entry.get()
    new_lbl3 = Label(pizza, text="Phone number: " + text3)
    new_lbl3.grid(row=7, column=2)
# Definition of check button command.
check_button =Button(pizza, text="checkout", command= check)
check_button.grid(row=6, column=0)

# Definition of delete or cancel button.
def deleteme():
    pizza_list.delete(0,5)
del_button = Button(pizza, text="delete pizza", command= deleteme)
del_button.grid(row=7, column=0)

# Drinks variables selection set to choose
drinks = StringVar()
drinks.set("choose a drink")
drink = OptionMenu(pizza, drinks, "Cola", "Fanta", "Sprite", "Mango")
drink.grid(row=8, column=0)

# Definition of the exit button.
# if (yes) press you will exit if no you will return to the main menu of the app.
def exitme():
    answer = messagebox.askyesno("hi", "are you sure to exit?")
    if answer == 1:
        pizza.destroy()
    else:
        return
exit_button = Button(pizza,text="exit me", command=exitme)
exit_button.grid(row=4, column=7)

# Definition of the program loop.
pizza.mainloop()

