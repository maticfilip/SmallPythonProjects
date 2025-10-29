import tkinter as tk
from lorem_text import lorem
from wonderwords import RandomWord
import time

class TypingApp:
    def __init__(self, root):
        self.root=root
        root.title("Speed typing text")
        root.geometry("1280x720")

        self.r=RandomWord()
        self.words=[self.r.word(word_min_length=3, word_max_length=8) for i in range(100)]
        self.curr=0
        self.user_input=[]
        self.time_left=60
        self.start_time=None
        self.running=False

        self.label_words=tk.Label(root, text=" ".join(self.words[:100]),wraplength=600)
        self.label_words.pack(pady=10)

        self.entry=tk.Entry(root, width=50)
        self.entry.pack(pady=10)
        self.entry.bind("<space>", self.on_space)

        self.timer_label=tk.Label(root, text="Time left: 60s")
        self.timer_label.pack()

        self.start_button=tk.Button(root, text="Start", command=self.start_test)
        self.start_button.pack(pady=10)

        self.result_label=tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def on_space(self, event):
        if not self.running:
            return
        word=self.entry.get().strip()
        if word:
            self.user_input.append(word)
        self.entry.delete(0, tk.END)

    def start_test(self):
        if not self.running:
            self.running=True
            self.start_time=time.time()
            self.update_timer()
            self.entry.delete(0, tk.END)
            self.entry.focus()

    def update_timer(self):
        if self.time_left>0:
            self.time_left-=1
            self.timer_label.config(text=f"Time left:{self.time_left}s")
            self.root.after(1000, self.update_timer)
        else:
            self.end_test()

    def end_test(self):
        self.running=False
        correct=0
        for i in range(min(len(self.user_input), len(self.words))):
            if self.user_input[i]==self.words[i]:
                correct+=1
        total_typed=len(self.user_input)
        self.result_label.config(text=f"Typed: {total_typed}, Correct: {correct}")
        self.entry.config(state="disabled")

if __name__=="__main__":
    root=tk.Tk()
    app=TypingApp(root)
    root.mainloop()