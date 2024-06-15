import tkinter as tk
import random

# Answer Bank
Answers = {
    "hello": "hola",
    "dog": "perro",
    "cat": "gato",
    "well": "bien",
    "us": "nos",
    "nothing": "nada",
    "house": "casa",
    "time": "tiempo"
}

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Code in Place 2024 Quiz")
        
        self.canvas = tk.Canvas(root, width=450, height=300)
        self.canvas.pack()
        
        self.question_label = self.canvas.create_text(10, 50, anchor='nw', font=("Arial", 14))
        
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry_window = self.canvas.create_window(10, 150, anchor='nw', window=self.entry)
        
        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer, font=("Arial", 14))
        self.button_window = self.canvas.create_window(220, 150, anchor='nw', window=self.submit_button)
        
        self.feedback_label = self.canvas.create_text(10, 200, anchor='nw', font=("Arial", 14))
        
        self.words = list(Answers.keys())
        random.shuffle(self.words)
        self.total_words = len(self.words)
        self.correct_count = 0
        self.next_question()
    
    def next_question(self):
        if self.words:
            self.current_word = self.words.pop()
            self.canvas.itemconfig(self.question_label, text=f"What is the Spanish translation for '{self.current_word}'?")
            self.canvas.itemconfig(self.feedback_label, text="")
            self.entry.delete(0, tk.END)
        else:
            self.canvas.itemconfig(self.question_label, text=f"You got {self.correct_count}/{self.total_words} words correct, good luck for the next attempt")
            self.entry.destroy()
            self.submit_button.destroy()
    
    def check_answer(self):
        user_answer = self.entry.get().strip().lower()
        if user_answer == translations[self.current_word]:
            self.canvas.itemconfig(self.feedback_label, text="That is correct!", fill="green")
            self.correct_count += 1
        else:
            self.canvas.itemconfig(self.feedback_label, text=f"That is incorrect, the correct answer is {translations[self.current_word]}.", fill="red")
        self.root.after(1000, self.next_question)  # Wait 1 second before showing the next question

if __name__ == '__main__':
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
