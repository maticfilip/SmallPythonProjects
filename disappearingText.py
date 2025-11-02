import tkinter as tk

class TextEditor:
    def __init__(self, master):
        self.master = master
        master.title("Text Editor")

        self.text_widget = tk.Text(master)
        self.text_widget.pack()

        self.status_label = tk.Label(master, text="Typing...")
        self.status_label.pack()

        self.after_id = None 

        self.text_widget.bind("<KeyRelease>", self.on_key_release)

    def on_key_release(self, event):
        if self.after_id:
            self.master.after_cancel(self.after_id)

        self.status_label.config(text="Typing...")

        self.after_id = self.master.after(5000, self.on_typing_stopped)

    def on_typing_stopped(self):
        self.status_label.config(text="Typing stopped.")
        self.after_id = None
        self.text_widget.delete('1.0', tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()