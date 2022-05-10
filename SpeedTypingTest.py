import typingGame
import scoreBoard
import tkinter


# main (root) GUI menu
class MainMenu:
    def __init__(self, master):
        self.master = master
        self.master.title('Menu')

        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # create the label for the game
        self.game_label = tkinter.Label(self.top_frame, text='Speed Typing Test', font=('Helvetica', 14))

        # create the radio buttons that will allow the user to select a difficulty
        #  this   is the pool of words that the randomizer draws from
        self.easy_difficulty = tkinter.Radiobutton(self.top_frame, text='Easy',
                                                   variable=self.radio_var, value=1, font=('Helvetica', 14))
        self.medium_difficulty = tkinter.Radiobutton(self.top_frame, text='Medium',
                                                     variable=self.radio_var, value=2, font=('Helvetica', 14))
        self.difficult_difficulty = tkinter.Radiobutton(self.top_frame, text='Difficult',
                                                        variable=self.radio_var, value=3, font=('Helvetica', 14))

        # pack the radio buttons and the label
        self.game_label.pack()
        self.easy_difficulty.pack()
        self.medium_difficulty.pack()
        self.difficult_difficulty.pack()

        # create ok and quit buttons
        self.start_button = tkinter.Button(self.bottom_frame, text='Start', command=self.start_game)
        self.scoreboard_button = tkinter.Button(self.bottom_frame, text='Scoreboard', command=self.open_scoreboard)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.master.destroy)

        # pack the buttons
        self.start_button.pack(side='left', pady=20)
        self.scoreboard_button.pack(side='left', pady=20)
        self.quit_button.pack(side='left', pady=20)

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

    def start_game(self):
        _ = typingGame.TypingGame(self.master, self.radio_var.get())

    def open_scoreboard(self):
        _ = scoreBoard.ScoreBoard(self.master)


def main():
    # create a window
    root = tkinter.Tk()
    root.geometry("470x200")
    _ = MainMenu(root)
    # control the mainloop from main instead of the class
    # controlling the loop like this makes calling toplevel classes easier
    root.mainloop()


main()
