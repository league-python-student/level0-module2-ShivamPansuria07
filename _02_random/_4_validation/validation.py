import random
from tkinter import messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()





    # TODO 1) Use each value of random_number to give the user a random compliment
    for i in range(10):
        random_number = random.randint(1, 5)
        if random_number==1:
            print("You are good at coding!")
        elif random_number==2:
            print("You are going to be great at everything you do!")
        elif random_number==3:
            print("You look great today!")
        elif random_number==4:
            print("I hope you have a great day!")
        else:
            print("You are going to to amazing things in you're life")
        print(random_number)
    # TODO 2) Repeat all the code above 10 times

    # TODO 3) Find someone to test out your program. They will like it :)
