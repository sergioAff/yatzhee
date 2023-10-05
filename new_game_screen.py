from tkinter import *
import tkinter.messagebox
from playing_game_screen import PlayingGameScreen

class NewGameScreen:
    def __init__(self) -> None:
        self.window = Toplevel()
        self.window.configure(bg = "#45c3de")
        self.window.geometry("400x300")
        self.window.resizable(False, False)
        self.new_game_frame = Frame(self.window)
        self.new_game_frame.configure(bg="#45c3de")
        self.player_name_entries = []
        self.player_name_labels=[]
        self.window.grab_set()
        self.window.iconbitmap("unnamed.ico")

        self.amount_of_players_label=Label(self.new_game_frame, text='Cantidad de jugadores: ',bg = "#45c3de")

        self.spPlayers= Spinbox(self.new_game_frame,from_=1, to=8, wrap =True,state="readonly")

        self.amount_of_players_ok_btn = Button(self.new_game_frame, text='OK', command=self.create_player_names_entries,bg="maroon1", fg="snow")
        self.start_game_btn = Button(self.new_game_frame, text='Iniciar', command=self.start_game,bg="maroon1", fg="snow")

        self.amount_of_players_label.grid(row=0, column=0)
        self.spPlayers.grid(row=0, column=1)
      
        self.amount_of_players_ok_btn.grid(row=0, column=2)


        self.new_game_frame.place(relx=0.5, rely=0.5, anchor=CENTER)


    def create_player_names_entries(self):
        amount_of_players = int(self.spPlayers.get())
        if len(self.player_name_entries)!=0:
            for i in self.player_name_labels:
                i.grid_forget()
            self.player_name_labels.clear()
            for i in self.player_name_entries:
                i.grid_forget()
            self.player_name_entries.clear()

        for i in range(amount_of_players):
            entry = Entry(self.new_game_frame)
            label=Label(self.new_game_frame,text=f"Jugador {i+1}: ",bg = "#45c3de")
            entry.grid(row=i+1, column=1)
            label.grid(row=i+1,column=0)
            self.player_name_entries.append(entry)
            self.player_name_labels.append(label)
            print(self.player_name_entries)
        
        self.start_game_btn.grid(row=amount_of_players+1, column=2)
        
    def start_game(self):
        for i in self.player_name_entries:
            s=i.get()
            s=s.strip()
            if s=="":
                tkinter.messagebox.showinfo("Error","Por favor, rellene todos los campos.")
                raise Exception("casilla vacia")
            if len(s)>7:
                 tkinter.messagebox.showinfo("Error","El nombre no puede tener más de 7 caracteres.")
                 raise Exception("el nombre es muy largo")    
        player_names = list(map(lambda entry: entry.get(), self.player_name_entries))
        playing_game_screen = PlayingGameScreen( player_names)
        
