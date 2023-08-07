# import the functions we need
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

# create, name and format the tkinter window
window = Tk()
window.title("Spot the Differences Game")
window.geometry("640x640")
window.configure(bg="#CACAFF")

# create a style that will be needed for the different pages of the game
style = Style()
style.configure("colour.TFrame", background="#CACAFF")

# create all the different pages as frames
page1 = Frame(master=window)
page2 = Frame(master=window)
page3 = Frame(master=window)
page4 = Frame(master=window)

# create a list of pages in order to iterate through it
pages = [page1, page2, page3, page4]

# create a first iteration with the for statement to apply the same style to all pages
for page in pages:
    page.config(style="colour.TFrame")

# create a second iteration with the for statement to manage the layout of all the frames within the window
for page in pages:
    page.grid(row=0, column=0, sticky="nesw")

# create the prompts in label widgets that indicate the player what to do on all pages
prompt_1 = Label(master=page1, text="Spot the differences. How many are there?", background="#CACAFF")
prompt_1.pack()

prompt_2 = Label(master=page2, text="Spot the differences. How many are there?", background="#CACAFF")
prompt_2.pack()

prompt_3 = Label(master=page3, text="Spot the differences. How many are there?", background="#CACAFF")
prompt_3.pack()

prompt_4 = Label(master=page4, text="You have successfully completed the game.", background="#CACAFF")
prompt_4.pack()

# create entry widgets that will collect user input from the player on pages 1, 2 and 3
entry1 = Entry(master=page1)
entry1.pack()

entry2 = Entry(master=page2)
entry2.pack()

entry3 = Entry(master=page3)
entry3.pack()

# import the images for the game and display them in label widgets on pages 1, 2 and 3
first_image = Image.open("spot_the_differences_1.jpeg")
first_pic = ImageTk.PhotoImage(first_image)

image_1 = Label(master=page1, image=first_pic)
image_1.pack()

second_image = Image.open("spot_the_differences_2.png")
second_pic = ImageTk.PhotoImage(second_image)

image_2 = Label(master=page2, image=second_pic)
image_2.pack()

third_image = Image.open("spot_the_differences_3.jpg")
third_pic = ImageTk.PhotoImage(third_image)

image_3 = Label(master=page3, image=third_pic)
image_3.pack()

# create an empty label widget in order to display the feedback to the player's guess
comment_1 = Label(master=page1, text="", background="#CACAFF")
comment_1.pack()


# declare a function which contains a selection statement with if and else in order to
# retrieve user input and give feedback accordingly
# the function also binds the event of the correct answer to button_1_1 which allows
# the 'next' button to activate
# this will be repeated for each page as the answer to the game will be different
def feedback1():

    if entry1.get().strip() == "5":
        comment_1.config(text="Correct!")
        button_1_1.config(command=lambda: page2.tkraise())

    else:
        comment_1.config(text="Wrong!")
        button_1_1.config(command="")


# create button widgets that the player can click on to get feedback and to proceed to the next page
button_1 = Button(master=page1, text="Check your answer", command=feedback1)
button_1.pack()

button_1_1 = Button(master=page1, text="Next")
button_1_1.pack()

# repetition of the process explained above for page 2
comment_2 = Label(master=page2, text="", background="#CACAFF")
comment_2.pack()


def feedback2():

    if entry2.get().strip() == "3":
        comment_2.config(text="Correct!")
        button_2_1.config(command=lambda: page3.tkraise())

    else:
        comment_2.config(text="Wrong!")
        button_2_1.config(command="")


button_2 = Button(master=page2, text="Check your answer", command=feedback2)
button_2.pack()

button_2_1 = Button(master=page2, text="Next")
button_2_1.pack()

# repetition of the process explained above for page 3
comment_3 = Label(master=page3, text="", background="#CACAFF")
comment_3.pack()


def feedback3():

    if entry3.get().strip() == "5":
        comment_3.config(text="Correct!")
        button_3_1.config(command=lambda: page4.tkraise())

    else:
        comment_3.config(text="Wrong!")
        button_3_1.config(command="")


button_3 = Button(master=page3, text="Check your answer", command=feedback3)
button_3.pack()

button_3_1 = Button(master=page3, text="Finish")
button_3_1.pack()

# create lists to display compliments (and format them) to the player for completing the game
compliments = ["Well done!", "Congratulations!", "Bravo!"]
colours = ["#F0F080", "#FF0000", "#00FF00"]


# declare a function containing an iteration with while in order to display all the different compliments
def get_compliment():
    i = 0
    while i < len(compliments):
        Label(master=page4, text=compliments[i], background=colours[i], font=('Helvetica bold', 26)).pack()
        i += 1


# create a button widget that will activate the final compliments upon click
button_4 = Button(master=page4, text="Click for a surprise", command=get_compliment)
button_4.pack()

# this allows page 1 to appear first when starting the game (otherwise the last page created appears first)
page1.tkraise()

# this will allow Python to run the Tkinter event loop
window.mainloop()
