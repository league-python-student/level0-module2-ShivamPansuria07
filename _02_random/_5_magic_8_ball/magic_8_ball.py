import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    simpledialog.askstring("Magic 8 ball", "Enter a question:")
    # Make a variable and initialize it to a random number between 0 and 3
    randnum = random.randint(0, 3)
    # If the random number is 0
    if randnum==0:
        # tell the user "Yes"
        print("Yes")
    # If the random number is 1
    if randnum == 1:
        # tell the user "No"
        print("No")
    # If the random number is 2
    if randnum == 2:
        # tell the user "Maybe you should ask Google?"
        print("Maybe you should ask Google?")
    # If the random number is 3
    if randnum == 3:
        # write your own answer
        print("That question is too difficult for me to answer")