import time
from random import choice
from tkinter import *
from tkinter import ttk




class Game:

    GAME_TITLE = "Пятнашки"
    MENU_WINDOW_SIZE = "700x900"
    GAME_WINDOW_SIZE = "500x600"

    RESULTS_WINDOW_TITLE = "Резульаты"
    RESULTS_WINDOW_SIZE = "500x600"

    DIFFICULTY_LEVEL = ["Easy","Normal", "Hard"]

    def __init__(self) -> None:
        self.time_game = 0

        self.buttons = []
        self.play_area = [i for i in range(0 ,16*10, 10)]

        self.open_menu()

    def open_menu(self) -> None:
        self.window = Tk(self.GAME_TITLE)
        self.window.config(bg="black")
        self.window.geometry(self.MENU_WINDOW_SIZE)
        self.window.resizable(False, False)

        self.label = Label(text="Hello student!", fg="green", bg="black").place(x=self.convert_to_int(self.MENU_WINDOW_SIZE)[0]//2, y=100)

        self.combobox = ttk.Combobox(values=self.DIFFICULTY_LEVEL, width=10)
        self.combobox.place(x=self.convert_to_int(self.MENU_WINDOW_SIZE)[0]//2, y=150)

        self.button1 = Button(text="Начать игру",command=self.complexity, fg="green", bg="black")
        self.button1.place(x=self.convert_to_int(self.MENU_WINDOW_SIZE)[0]//2, y=280)

        self.button2 = Button(text="Результаты", command=self.complexity, fg="green", bg="black", width=12)
        self.button2.place(x=self.convert_to_int(self.MENU_WINDOW_SIZE)[0]//2, y=0)

        self.window.mainloop()

    def open_game(self) -> None:
        self.window.destroy()
        self.window = Tk(self.GAME_TITLE)
        self.window.geometry(self.GAME_WINDOW_SIZE)

        self.minute = IntVar()
        self.second = IntVar()
        self.minute.set(self.time_game)
        self.second.set(0)

        self.mins_tf = Label(bg="navy blue",fg="red",textvariable=self.minute)
        self.mins_tf.pack(side=TOP, expand=YES, fill=BOTH)

        self.sec_tf = Label(textvariable=self.second,bg="navy blue",fg="red")
        self.sec_tf.pack(side=TOP, expand=YES, fill=BOTH)

        for i in range(0, 4):
            frm = Frame(self.window)
            frm.pack(expand=YES, fill=BOTH)
            for j in range(0, 4):
                self.buttons += [Button(frm, text=self.play_area[i * 4 + j], font=('mono', 20, 'bold',),bg="navy blue",fg="red",
                            width=1, height=1,
                            command=lambda n=i * 4 + j: self.play(n))]
                self.buttons[i * 4 + j].pack(side=LEFT, expand=YES, fill=BOTH)

        for i in range(0, 3000):
            self.play(choice(range(0, 16)))

        self.update_clock()
        self.window.mainloop()

    def open_results(self, result: bool = False) -> None:

        # self.results_surf = Tk("Результаты")
        # self.results_surf.geometry(self.RESULTS_WINDOW_SIZE)

        if result:
            self.results_label = Label(text="Victory").pack()
        else:
            self.results_label = Label(text="Game over.", height=10).pack()

        # self.results_surf.mainloop()

    def complexity(self) -> None:
        match self.combobox.get():
            case "Easy": 
                self.time_game = 20
            case "Normal": 
                self.time_game = 15
            case "Hard": 
                self.time_game = 1
            case _: pass

        self.open_game()

    def operation(self) -> None:
        if self.buttons == sorted(self.buttons):
            self.open_results(True)
        elif self.second.get() == 0 and self.minute.get() == 0:
            self.open_results(False)

    def update_clock(self) -> None:
        if self.second.get() == 0 and self.minute.get() > 0:
            self.minute.set(self.minute.get()-1)
            self.second.set(59)
        elif self.second.get() == 0 and self.minute.get() == 0: self.operation()
        else: self.second.set(self.second.get()-1)

        self.mins_tf.configure(text=self.minute)
        self.sec_tf.configure(text=self.second)
        self.window.after(1000, self.update_clock)

    def play(self, n) -> None:
        m = self.play_area.index(0)
        if abs(m - n) == 1 and n // 4 == m // 4 or abs(m - n) == 4:
            self.play_area[m], self.play_area[n] = self.play_area[n], self.play_area[m]
            self.buttons[m].config(text=self.play_area[m])
            self.buttons[n].config(text=" ")

    def convert_to_int(self, obj: str) -> list[int, int]:
        if isinstance(obj, str):
            x, y = int(obj[:obj.find('x')]), int(obj[obj.find('x')+1:])

        return [x, y]


        
if __name__ == "__main__": Game()

