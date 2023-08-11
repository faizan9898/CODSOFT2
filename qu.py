import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "Berlin", "Madrid", "London"],
                "answer": "Paris"
            },
            {
                "question": "Which planet is known as the 'Red Planet'?",
                "options": ["Mars", "Venus", "Jupiter", "Mercury"],
                "answer": "Mars"
            },
            {
                "question": "Taj Mahal locate in ?",
                "options": ["Agra", "Mumbai", "Gujrat", "Delhi"],
                "answer": "Agra"
            },    
            # Add more questions
        ]
        
        self.current_question = 0
        self.score = 0
        
        self.name_label = tk.Label(root, text="Enter your name:")
        self.name_label.pack()
        
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()
        
        self.start_button = tk.Button(root, text="Start", command=self.start_quiz)
        self.start_button.pack(pady=10)
        
    def start_quiz(self):
        self.player_name = self.name_entry.get()
        if not self.player_name:
            messagebox.showinfo("Error", "Please enter your name.")
            return
        
        self.name_label.destroy()
        self.name_entry.destroy()
        self.start_button.destroy()
        
        self.show_question()
    
    def show_question(self):
        if self.current_question < len(self.questions):
            question_frame = tk.Frame(root)
            question_frame.pack(pady=20)
            
            question_label = tk.Label(question_frame, text=self.questions[self.current_question]["question"])
            question_label.pack()
            
            self.options_var = tk.StringVar()
            for i, option in enumerate(self.questions[self.current_question]["options"]):
                tk.Radiobutton(question_frame, text=option, variable=self.options_var, value=option).pack(pady=5)
            
            submit_button = tk.Button(question_frame, text="Submit", command=self.check_answer)
            submit_button.pack(pady=10)
        else:
            self.show_result()
    
    def check_answer(self):
        user_answer = self.options_var.get()
        correct_answer = self.questions[self.current_question]["answer"]
        
        if user_answer == correct_answer:
            self.score += 1
        
        self.current_question += 1
        
        self.destroy_current_frame()
        self.show_question()
    
    def show_result(self):
        result_label = tk.Label(root, text=f"Quiz completed, {self.player_name}!")
        result_label.pack(pady=20)
        
        score_label = tk.Label(root, text=f"Your score: {self.score}/{len(self.questions)}")
        score_label.pack(pady=10)
        
        play_again_button = tk.Button(root, text="Play Again", command=self.restart_game)
        play_again_button.pack()
    
    def destroy_current_frame(self):
        for widget in root.winfo_children():
            widget.destroy()
        
    def restart_game(self):
        self.current_question = 0
        self.score = 0
        self.destroy_current_frame()
        self.show_question()

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
