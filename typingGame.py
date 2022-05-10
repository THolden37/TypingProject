import tkinter
from tkinter import *
from tkinter import messagebox
import random
import keyboard
import time
import pickle


class TypingGame:
    def __init__(self, master, difficulty):

        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        # initialization of variables for use by program
        self.difficulty = difficulty
        self.game = tkinter.Toplevel(master)
        self.game.title('Speed Typing Test')
        self.game.resizable(False, False)
        self.game.geometry("850x400")
        self.quit_button = tkinter.Button(self.game, text='Quit', font='Arial 20', command=self.game.destroy)
        self.quit_button.place(x=450, y=300)
        self.i = 0
        self.count = 0
        self.new_str = ''
        self.index = 0
        self.length = 0
        self.typing_str = ''
        self.start_time = 0
        self.end_time = 0
        self.x = 0
        self.gen_typing_str()
        self.typing_game()

    def typing_game(self):
        text = tkinter.Text(self.game, wrap=WORD, height=5, width=50, font="Arial 20")
        text.insert(END, self.typing_str)
        text.place(x=60, y=30)

        def callback():  # I used https://ishwargautam.blogspot.com/2021/10/typing-speed-application-using-python.html
            if txt.get() != ' ':  # as a basis for the logic in this section of the code
                if self.x == 0:  # checks to see if callback has been called before and starts time
                    self.start_time = time.time()
                    self.x = 1
                if keyboard.is_pressed('space'):  # checks for press of space to initiate logic
                    try:
                        a = txt.get().split()[-1]  # variable is filled with last word typed
                        b = self.typing_str.split()[self.i]  # variable is filled with corresponding word
                        if a == b:
                            self.count += 1
                            self.new_str = self.new_str + b + ' '
                            c = self.new_str + ' '.join(self.typing_str.split()[self.i+1:])

                            # get index to know what part to highlight
                            self.index = self.typing_str.index(b, self.index + self.length)
                            self.length = len(str(b))

                            # deletes current text and replaces with one word highlighted
                            text.delete("0."+str(self.index), END)
                            text.insert(END, c)

                            text.tag_add("start", "1."+str(self.index), "1."+str(self.index+self.length))
                            text.tag_config("start", foreground="#000fff000")
                        else:
                            # follows from the same logic of the previous if statement
                            self.new_str = self.new_str + b + ' '
                            c = self.new_str + ' '.join(self.typing_str.split()[self.i+1:])

                            # get index to know what part to highlight
                            self.index = self.typing_str.index(b, self.index + self.length)
                            self.length = len(str(b))

                            text.delete("0."+str(self.index), END)
                            text.insert(END, c)

                            text.tag_add("start", "1."+str(self.index), "1."+str(self.index + self.length))
                            text.tag_config("start", foreground="red")

                            # stopping condition for code
                        if (self.index + self.length) == len(self.typing_str):
                            # ends timer and calculates important values
                            self.end_time = time.time()
                            typed_entries = len(' '.join(txt.get().split()))
                            time_in_min = (self.end_time-self.start_time)/60
                            #  finds word per minute by dividing by average length of a word 5
                            result = int((typed_entries/5)/time_in_min)
                            messagebox.showinfo('Result', "Typing speed = "+str(result) + " wpm"
                                                + " Accuracy =" + format(self.count/20, '.2%'))
                            self.save_score(result)

                        self.i += 1
                    except IndexError:
                        pass
            return True
        # creation of variable to store user entered string and repeatedly validate it upon all key presses
        txt = StringVar()
        entry = tkinter.Entry(self.game, width=40, font="Verdana 15", textvariable=txt,
                              validate='all', validatecommand=callback)
        entry.place(x=200, y=225)
        label_widget = tkinter.Label(self.game, text="Start Typing", font="Arial 20")
        label_widget.place(x=10, y=220)

    # reads data from the #_most_common_words files and stores it into typing_string
    def gen_typing_str(self):
        try:
            temp_list = []
            if self.difficulty == 1:
                input_file = open("1000_most_common_words.txt", 'r')
                for line in input_file:
                    temp_list.append(line.rstrip('\n'))
                input_file.close()
            elif self.difficulty == 2:
                input_file = open("5000_most_common_words.txt", 'r')
                for line in input_file:
                    temp_list.append(line.rstrip('\n'))
                input_file.close()
            else:
                input_file = open("10000_most_common_words.txt", 'r')
                for line in input_file:
                    temp_list.append(line.rstrip('\n'))
                input_file.close()
            counter = 0
            while counter < 20:
                number = random.randint(0, len(temp_list) - 1)
                self.typing_str = self.typing_str + str(temp_list[number]) + ' '
                counter += 1
            self.typing_str = "".join(self.typing_str.rstrip())
        except IOError:
            print("The word file was unable to be opened")
            self.end_game()

    # saves the score of the most previous test
    def save_score(self, my_result):
        found = 0
        accuracy = self.count/20
        if accuracy >= .85:
            if self.difficulty == 1:
                try:
                    in_file = open("easy_scores.dat", "rb")
                    scores = pickle.load(in_file)
                    in_file.close()
                    counter = 0
                    # reads a score that is larger than a previous score and then stops replacing scores and sorts
                    for num in scores:
                        if my_result > num and found != 1:
                            scores[counter] = my_result
                            found = 1
                        counter += 1
                    scores.sort()
                    out_file = open("easy_scores.dat", "wb")
                    pickle.dump(scores, out_file)
                    out_file.close()
                except IOError:
                    # if the file has not been created yet the file is made
                    # with the top score and 0 for the other two scores
                    output_file = open("easy_scores.dat", "wb")
                    scores = [0, 0, my_result]
                    pickle.dump(scores, output_file)
                    output_file.close()
            elif self.difficulty == 2:  # this statement follows from the first if
                try:
                    in_file = open("medium_scores.dat", "rb")
                    scores = pickle.load(in_file)
                    in_file.close()
                    counter = 0
                    for num in scores:
                        if my_result > num and found != 1:
                            scores[counter] = my_result
                            found = 1
                        counter += 1
                    scores.sort()
                    out_file = open("medium_scores.dat", "wb")
                    pickle.dump(scores, out_file)
                    out_file.close()
                except IOError:
                    output_file = open("medium_scores.dat", "wb")
                    scores = [0, 0, my_result]
                    pickle.dump(scores, output_file)
                    output_file.close()
            else:  # this statement follows from the first if
                try:
                    in_file = open("difficult_scores.dat", "rb")
                    scores = pickle.load(in_file)
                    in_file.close()
                    counter = 0
                    for num in scores:
                        if my_result > num and found != 1:
                            scores[counter] = my_result
                            found = 1
                        counter += 1
                    scores.sort()
                    out_file = open("difficult_scores.dat", "wb")
                    pickle.dump(scores, out_file)
                    out_file.close()
                except IOError:
                    output_file = open("difficult_scores.dat", "wb")
                    scores = [0, 0, my_result]
                    pickle.dump(scores, output_file)
                    output_file.close()
        self.end_game()

    def end_game(self):
        self.game.destroy()
