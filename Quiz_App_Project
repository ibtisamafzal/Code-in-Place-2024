import tkinter as tk
import random

# Dictionary of questions and answers about computer science
questions = {
    "Main memory is also called?": "ram",
    "Primary language used for web development?": "html",
    "'CPU' stands for?": "central processing unit",
    "Common method for storing data persistently?": "database",
    "ROM stands for?": "read only memory",
    "'HTTP' is a?": "protocol",
    "Reusable piece of code is called?": "function",
    "Loop that runs as long as a condition is true?": "while",
    "Data structure that stores key-value pairs?": "dictionary",
    "Primary language for Android development?": "java",
}

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CIP-24 Computer Science Quiz")
        
        self.canvas = tk.Canvas(root, width=450, height=300)
        self.canvas.pack()
        
        self.question_label = self.canvas.create_text(10, 50, anchor='nw', font=("Arial", 14))
        
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry_window = self.canvas.create_window(10, 150, anchor='nw', window=self.entry)
        
        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer, font=("Arial", 14))
        self.button_window = self.canvas.create_window(220, 150, anchor='nw', window=self.submit_button)
        
        self.feedback_label = self.canvas.create_text(10, 200, anchor='nw', font=("Arial", 14))
        
        self.questions = list(questions.keys())
        random.shuffle(self.questions)
        self.total_questions = len(self.questions)
        self.correct_count = 0
        self.next_question()
    
    def next_question(self):
        if self.questions:
            self.current_question = self.questions.pop()
            self.canvas.itemconfig(self.question_label, text=f"{self.current_question}")
            self.canvas.itemconfig(self.feedback_label, text="")
            self.entry.delete(0, tk.END)
        else:
            self.canvas.itemconfig(self.question_label, text=f"You got {self.correct_count}/{self.total_questions} questions correct, Good Luck!")
            self.entry.destroy()
            self.submit_button.destroy()
    
    def check_answer(self):
        user_answer = self.entry.get().strip().lower()
        correct_answer = questions[self.current_question].strip().lower()
        if user_answer == correct_answer:
            self.canvas.itemconfig(self.feedback_label, text="That is correct!", fill="green")
            self.correct_count += 1
        else:
            self.canvas.itemconfig(self.feedback_label, text=f"That is incorrect, the correct answer is '{questions[self.current_question]}'.", fill="red")
        self.root.after(1000, self.next_question)  # Wait 1 second before showing the next question

if __name__ == '__main__':
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
