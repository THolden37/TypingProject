import tkinter
import pickle


class ScoreBoard:
    def __init__(self, master):
        #  initializes all the scores into lists from the files created in TypingGame and show the result to the user
        self.score_board = tkinter.Toplevel(master)
        self.score_board.title('Scoreboard')
        self.score_board.resizable(False, False)
        self.score_board.geometry("800x270")
        self.easy_scores = [0, 0, 0]
        self.medium_scores = [0, 0, 0]
        self.difficult_scores = [0, 0, 0]
        self.get_scores()
        # creation of all widgets
        self.title = tkinter.Label(self.score_board, text='Scores (WPM)', font='Arial 30')
        self.headers = tkinter.Label(self.score_board, text='Easy        \tMedium\t       Difficult', font='Arial 30')
        self.scores_one = tkinter.Label(self.score_board, font='Arial 20', text=(str(self.easy_scores[2]) + '\t\t'
                                                                                 + str(self.medium_scores[2]) + '\t\t'
                                                                                 + str(self.difficult_scores[2])))
        self.scores_two = tkinter.Label(self.score_board, font='Arial 20', text=(str(self.easy_scores[1]) + '\t\t'
                                                                                 + str(self.medium_scores[1]) + '\t\t'
                                                                                 + str(self.difficult_scores[1])))
        self.scores_three = tkinter.Label(self.score_board, font='Arial 20', text=(str(self.easy_scores[0]) + '\t\t'
                                                                                   + str(self.medium_scores[0]) + '\t\t'
                                                                                   + str(self.difficult_scores[0])))
        self.quit_button = tkinter.Button(self.score_board, text='Quit', command=self.score_board.destroy,
                                          font='Arial 20')
        # packing of all widgets
        self.title.pack()
        self.headers.pack()
        self.scores_one.pack()
        self.scores_two.pack()
        self.scores_three.pack()
        self.quit_button.pack()

    # reads from files and fills up the list within variable associated with the class
    def get_scores(self):
        try:
            input_file = open('easy_scores.dat', 'rb')
            temp_list = pickle.load(input_file)
            counter = 0
            for num in temp_list:
                self.easy_scores[counter] = num
                counter += 1
            input_file.close()
        except IOError:
            pass
        try:
            input_file = open('medium_scores.dat', 'rb')
            temp_list = pickle.load(input_file)
            counter = 0
            for num in temp_list:
                self.medium_scores[counter] = num
                counter += 1
            input_file.close()
        except IOError:
            pass
        try:
            input_file = open('difficult_scores.dat', 'rb')
            temp_list = pickle.load(input_file)
            counter = 0
            for num in temp_list:
                self.difficult_scores[counter] = num
                counter += 1
            input_file.close()
        except IOError:
            pass
