from tkinter import Tk, Label, Entry, Button
import bananhack

class BananHackApp:
    def __init__(self, master):
        self.master = master
        self.configure_gui()
        self.create_widgets()

    def configure_gui(self):
        self.master.geometry("300x300")
        self.master.minsize(300, 300)
        self.master.maxsize(300, 300)
        self.master.config(background='#24282b')
        self.master.title("BananHack")

    def create_widgets(self):
        Label(self.master, text="BananHack", font=("Courrier", 30), bg='#24282b', fg='#fbdd11').pack()

        Button(self.master, text="Open website", bg='#343a40', fg='#fbdd11', command=bananhack.open_website).pack()

        Label(self.master, text="Roll amount ", font=("Courrier", 14), bg='#24282b', fg='white').place(x=10, y=86)
        self.entry_maxroll = Entry(self.master)
        self.entry_maxroll.place(x=150, y=91)

        Label(self.master, text="Max loose ", font=("Courrier", 14), bg='#24282b', fg='white').place(x=10, y=119)
        self.entry_maxloose = Entry(self.master)
        self.entry_maxloose.place(x=150, y=124)

        Button(self.master, text="Let's get rich", bg='#fbdd11', fg='#24282b', command=self.launch).pack(side='bottom', pady=50)

    def launch(self):
        n_roll = int(self.entry_maxroll.get() or 10)
        n_loose = int(self.entry_maxloose.get() or 15)
        bananhack.play(n_roll, n_loose)

if __name__ == "__main__":
    root = Tk()
    app = BananHackApp(root)
    root.mainloop()
