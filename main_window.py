from tkinter import *
from scoreboard_screen import ScoreboardScreen
from new_game_screen import NewGameScreen


class StartingScreen:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.geometry("800x600")
        self.window.configure(bg = "#45c3de")
        self.window.resizable(False, False)
        self.window.title("Yahtzee")
        self.window.iconbitmap("unnamed.ico")
    
        canvas = Canvas(
            self.window,
            bg = "#45c3de",
            height = 600,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        img0 = PhotoImage(file = f"img0.png")
        self.b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.show_scoreboard,
            relief = "flat")

        self.b0.place(
            x = 283, y = 276,
            width = 205,
            height = 68)

        img1 = PhotoImage(file = f"img1.png")
        self.b1 = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = quit,
            relief = "flat")

        self.b1.place(
            x = 279, y = 361,
            width = 203,
            height = 55)

        img2 = PhotoImage(file = f"img2.png")
        self.b2 = Button(
            image = img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.start_new_game,
            relief = "flat")

        self.b2.place(
            x = 273, y = 193,
            width = 210,
            height = 66)

        canvas.create_text(
            380.5, 99.0,
            text = "YAHTZEE",
            fill = "#da1f57",
            font = ("TrainOne-Regular", int(48.0)))

        self.window.mainloop()


    def start_new_game(self):
        self.new_game_screen = NewGameScreen()

    def show_scoreboard(self):
        self.scoreboard = ScoreboardScreen(self.window)
    

c=StartingScreen()