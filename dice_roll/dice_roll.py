import tkinter 
from PIL import Image, ImageTk
import random

root=tkinter.Tk()
root.geometry('400x400')
root.title('Dice Roll')

BlackLine=tkinter.Label(root,text='')
BlackLine.pack()

HeadingLabel=tkinter.Label(root,text='Roll The Dices',
                           fg='Dark Green',
                           bg='Light yellow',
                           font='Helvetica 16 bold italic'
                           )
HeadingLabel.pack()

dice = ['C:\\Users\\shubh\\Documents\\COLLEGE\\Capstone\\dice_roll\\dice1.png', 'C:\\Users\\shubh\\Documents\\COLLEGE\\Capstone\\dice_roll\\dice2.png', 'C:\\Users\\shubh\\Documents\\COLLEGE\\Capstone\\dice_roll\\dice3.png','C:\\Users\\shubh\\Documents\\COLLEGE\\Capstone\\dice_roll\\die4.png', 'C:\\Users\\shubh\\Documents\\COLLEGE\\Capstone\\dice_roll\\dice5.png', 'C:\\Users\\shubh\\Documents\\COLLEGE\\Capstone\\dice_roll\\die6.png']

originalImage=Image.open(random.choice(dice))

originalImage=originalImage.resize((200,200))

DiceImage=ImageTk.PhotoImage(originalImage)


ImageLabel=tkinter.Label(root,image=DiceImage)

ImageLabel.image=DiceImage

ImageLabel.pack()

def Roll_dice():
    originalImage=Image.open(random.choice(dice))
    originalImage=originalImage.resize((200,200))
    DiceImage=ImageTk.PhotoImage(originalImage)


    # DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    ImageLabel.configure(image=DiceImage)
    # keep a reference
    ImageLabel.image = DiceImage


button=tkinter.Button(root,text='Roll',fg='Light Blue',command=Roll_dice)
button.pack()
root.mainloop()
