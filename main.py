import tkinter
from PIL import Image, ImageTk
import random

# adding main window application
root = tkinter.Tk()
root.geometry('400x400')
root.title('Roll the dice')

# add a label to the frame in order for the HeadingLabel line to be lower
BlankLine = tkinter.Label(root, text="")
BlankLine.pack()

HeadingLabel = tkinter.Label(
    root,
    text="Try your luck!",
    fg="light green",
    bg="dark green",
    font="Helvetica 16 bold italic"
)
HeadingLabel.pack()
# create a list of dice image paths in the project folder
dice_images = ['./dice_images/die1.png', './dice_images/die2.png', './dice_images/die3.png',
               './dice_images/die4.png', './dice_images/die5.png', './dice_images/die6.png']
# simulate a random dice image between 0 and 6
random_dice_image = ImageTk.PhotoImage(Image.open(random.choice(dice_images)))

# constructing an Image widget for tkinter window
ImageLabel = tkinter.Label(root, image=random_dice_image)
ImageLabel.image = random_dice_image
# packing it into the window
ImageLabel.pack(expand=True)




if __name__ == '__main__':
    root.mainloop()
