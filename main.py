from tkinter import *
import pandas
import random
import time
FONT = "Ariel"

BACKGROUND_COLOR = "#B1DDC6"

currentCard = {}
toLearn ={}

# ------------------Read Data------------------#
try:
    data = pandas.read_csv("data/wordsToLearn.csv")
except FileNotFoundError:
    originalData = pandas.read_csv("data/french_words.csv")
    toLearn = originalData.to_dict(orient="records")
else:
    toLearn = data.to_dict(orient="records")


def changeWord():
    global currentCard, flipTimer
    window.after_cancel(flipTimer)
    currentCard = random.choice(toLearn)
    canvas.itemconfig(canvasImage,image=cardFront)
    canvas.itemconfig(language,text="French",fill="Black")
    canvas.itemconfig(word,text=currentCard['French'],fill="Black")
    flipTimer = window.after(3000,flipCard)



def flipCard():
    canvas.itemconfig(canvasImage,image=cardBack)
    canvas.itemconfig(language, text="English",fill="White")
    canvas.itemconfig(word, text=currentCard['English'],fill="White")

def isKnown():
    toLearn.remove(currentCard)
    wordData = pandas.DataFrame(toLearn)
    wordData.to_csv("wordsToLearn.csv")
    changeWord()


# ------------------UI SETUP------------------#
window = Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flipTimer = window.after(3000,flipCard)

canvas = Canvas(width = 800, height = 526,bg=BACKGROUND_COLOR,highlightthickness=0)
cardFront = PhotoImage(file="images/card_front.png")
cardBack = PhotoImage(file="images/card_back.png")
canvasImage = canvas.create_image(400,263,image = cardFront)
language = canvas.create_text(400,150, text = "French", fill="Black", font=(FONT,40,"italic"))
word = canvas.create_text(400,263, text = "trouve", fill="Black", font=(FONT,60,"bold"))




wrong = PhotoImage(file="images/wrong.png")
wrongBtn = Button(image=wrong, highlightthickness=0,command=changeWord)
correct = PhotoImage(file="images/right.png")
correctBtn = Button(image=correct, highlightthickness=0,command=isKnown)

canvas.grid(column=0,row=0,columnspan=2)
wrongBtn.grid(column=0,row=1)
correctBtn.grid(column=1,row=1)


changeWord()

window.mainloop()