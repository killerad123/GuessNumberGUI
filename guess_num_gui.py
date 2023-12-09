from tkinter import *
import random
import tkinter.messagebox as tmsgx


def game_page():
    guess_ans = random.randint(1, 100)
    # print(guess_ans)

    def Hint(event):
        list = [2, 3, 4, 5, 6, 7, 8, 9, 11, 15, 17, 19]
        divisors = []
        for nums in list:
            if (guess_ans % nums == 0):
                divisors.append(nums)
        if (len(divisors)==0):
            print("prime")     
        else:        
            hint_disp_screen.set(f'Ans is divisible by {random.choice(divisors)}')
            # print(f"Hint : Ans is divisible by {random.choice(divisors)}")
        return

    game = Tk()
    '''Game starts from here'''
    game.geometry('900x600')
    game.config(background="white")
    game.title('Just Guess It')
    tmsgx.showinfo('Just Guess It','Random number is chosen , You can start your game by entering number and submitting it .')
    tmsgx.showinfo('Just Guess It','Some instructions :\n1)grey coloured screen will be disappeard after entering first number\n2)At last answer will be displayed')


    head_line = Label(game, text='Your Game is here !!!', font='bold')
    head_line.pack()
    dis_screen = Frame(game,bg='grey' ,width=600, height=300)
    dis_screen.pack(side=BOTTOM, pady=10)
    dial_pad = Frame(game, width=400, height=200)  # borderwidth=10,border=15
    dial_pad.pack(padx=100, side=LEFT, anchor=NW, pady=10)
    dial_pad.config(background="yellow")
    num_set1 = Frame(dial_pad, bg='white', width=150, height=100)
    num_set1.pack(padx=10)
    num_set2 = Frame(dial_pad, bg='white', width=150, height=100)
    num_set2.pack()
    num_set3 = Frame(dial_pad, bg='white', width=150, height=100)
    num_set3.pack()
    num_set4 = Frame(dial_pad, bg='white',)
    # we have set this in dial_pad frame bcoz we want this below the num_sets
    key_set = Frame(game, width=200, height=150)
    key_set.pack(side=RIGHT, anchor=NE, pady=30, padx=20)
    num_set4.pack()
    frame = Frame(key_set)
    frame.pack(side=BOTTOM)


    '''this function will be called when we press any number button'''
    def on_click(event):
        global text
        text = ''
        text = text+event.widget.cget('text')
        num_disp_screen.set(num_disp_screen.get()+text)

    '''Keypad buttons are starting from here'''

    b1 = Button(num_set1, text='1', padx=10, pady=10)
    b1.pack(side=LEFT, padx=5, pady=5)
    b1.bind('<Button-1>', on_click)
    b2 = Button(num_set1, text='2', padx=10, pady=10)
    b2.pack(side=LEFT, padx=5, pady=5)
    b2.bind('<Button-1>', on_click)
    b3 = Button(num_set1, text='3', padx=10, pady=10)
    b3.pack(side=LEFT, padx=5, pady=5)
    b3.bind('<Button-1>', on_click)
    b4 = Button(num_set2, text='4', padx=10, pady=10)
    b4.pack(side=LEFT, padx=5, pady=5)
    b4.bind('<Button-1>', on_click)
    b5 = Button(num_set2, text='5', padx=10, pady=10)
    b5.pack(side=LEFT, padx=5, pady=5)
    b5.bind('<Button-1>', on_click)
    b6 = Button(num_set2, text='6', padx=10, pady=10)
    b6.pack(side=LEFT, padx=5, pady=5)
    b6.bind('<Button-1>', on_click)
    b7 = Button(num_set3, text='7', padx=10, pady=10)
    b7.pack(side=LEFT, padx=5, pady=5)
    b7.bind('<Button-1>', on_click)
    b8 = Button(num_set3, text='8', padx=10, pady=10)
    b8.pack(side=LEFT, padx=5, pady=5)
    b8.bind('<Button-1>', on_click)
    b9 = Button(num_set3, text='9', padx=10, pady=10)
    b9.pack(side=LEFT, padx=5, pady=5)
    b9.bind('<Button-1>', on_click)
    b0 = Button(num_set4, text='0', padx=10, pady=10)
    b0.pack(side=LEFT, padx=5, pady=5)
    b0.bind('<Button-1>', on_click)


    def disp_on_screen(val):
        '''for displaying entered number'''
        # val=int(val)
        dis_screen.config(background="white")  # changing color to white so that though large number is entered grey color will not appear
        Label(dis_screen, text=str(val)).pack()
        
    global counter
    counter = 0        

    def submit(event):
        '''submitting the user response'''
        val = num_disp_screen.get()
        global counter
        counter += 1
        print(counter)
        print(guess_ans)
        if (counter > 10):
            num_disp_screen.set("")
            return    # we are returning here bcoz we dont want to display further iterations
        if (val == str(guess_ans)):
            enter.configure(state=DISABLED)
            val = f'Correct Guess..You won!!'
            disp_on_screen(val)
            counter = 10   # here we are changing value of counter bcoz we dont want to display 'Correct Guess..You won!!' many times
            return

        if (val == ''):
            val = 'No value'
            print(val)
            counter -= 1
            return  # we are returning here bcoz we dont want to display the blank
        if (counter == 10):
            enter.configure(state=DISABLED)
            val = f'Thanks for playing and the answer was {guess_ans}'
            disp_on_screen(val)
            return

        disp_on_screen(val)
        num_disp_screen.set("")   # to clear out screen after submitiing

    '''Buttons for Submitting and for hint'''

    enter = Button(key_set, text='Enter', width=25, background='sky blue')
    # side=RIGHT we can use this in both button's pack if we want both buttons in oneline
    enter.pack(pady=15, padx=150)
    enter.bind('<Button-1>', submit)
    hint = Button(key_set, text='Hint', width=25, background='sky blue')
    hint.pack(pady=15, padx=2)
    hint.bind('<Button-1>', Hint)
    Label(frame, text='Your Entered Number', foreground='blue').pack()
    num_disp_screen = StringVar()
    num_screen = Entry(frame, textvariable=num_disp_screen, width=50)
    num_screen.pack()
    Label(frame, text='Your Hint', foreground='blue').pack()
    hint_disp_screen = StringVar()
    hint_screen = Entry(frame, textvariable=hint_disp_screen, width=50)
    hint_screen.pack(side=BOTTOM)

    '''game ends here'''
    game.mainloop()


txt = tmsgx.askquestion('Just guess It', 'Do you want to start the game ? ')
if txt == 'yes':
    game_page()
else:
    exit()
   












'''
  this logic can be used but all buttons are coming in one line

list=[i for i in range(10)]
print(list)
for button in list:
    b=Button(root,text=f'{button}',padx=10,pady=10)
    b.pack(side=LEFT,padx=5,pady=5)
    b.bind('<Button-1>')'''


'''following code is for home page'''


# def Home_page():
#     root = Tk()
#     root.geometry('600x400')
#     root.title('Just Guess It - Homepage')
#     Label(text='Welcome to !!! ', foreground='black', font='bold').pack()
#     Label(text='Just Guess It game ', foreground='black', font='bold').pack()
#     main=Frame(root)
#     main.pack(pady=100)
#     fline=Label(main,text='Click below to start',foreground='black')
#     fline.pack()
#     start_butt=Button(main,text="Let's start",foreground='blue',font='bold',border=10,command=game_page)
#     start_butt.pack(pady=20)
#     root.mainloop()
# game_page()
