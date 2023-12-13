



import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Game")
        
        
        self.welcome_label = tk.Label(self.master,text="Welcome To Quiz Game")
        self.welcome_label.pack(pady=15)
        
        self.rules_label= tk.Label(self.master, text = "Rules:\nSelect only one option for each questions and click 'Next' button to proceed next questions")
        self.rules_label.pack(pady=5)
        self.questions = [
            {
                "question": "Where was Gautam Buddha born?",
                "options": ["India", "China", "Nepal", "USA"],
                "answer": "Nepal"
            },
            {
                "question": "Who painted the Mona Lisa?",
                "options": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"],
                "answer": "Leonardo da Vinci"
            },
            {
                "question": "Which team won the Worldcup Cricket 2023?",
                "options": ["India", "Australia", "South Africa", "New-Zealand"],
                "answer": "Australia"
            },
            {
                "question": "Which component is responsible for storing data long-term on a computer?",
                "options": ["RAM", "CPU", "Hard Drive(HDD/SSD)", "GPU"],
                "answer": "Hard Drive(HDD/SSD)"
            },
            {
                "question": "Which protocol is used to send emails over the internet?",
                "options": ["FTP", "SMTP", "HTTP", "TCP/IP"],
                "answer": "SMTP"
            }
        ]

        self.current_question_index = 0
        self.score = 0

        

        self.label_question = tk.Label(self.master, text="", font=("Arial", 12))
        self.label_question.pack(pady=10)


        self.radio_var = tk.StringVar()
        self.radio_buttons = []
        for i in range(4):
            radio_button = tk.Radiobutton(self.master, text="", variable=self.radio_var, value="", command=self.select_option)
            radio_button.pack(anchor=tk.W)
            self.radio_buttons.append(radio_button)

        self.button_next = tk.Button(self.master, text="Next", command=self.next_question)
        self.button_next.pack(pady=10)

        self.display_next_question()

    def display_next_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.label_question.config(text=question_data["question"])

            for i, option in enumerate(question_data["options"]):
                self.radio_buttons[i].config(text=option, value=option)
                self.radio_buttons[i].deselect()

            self.button_next.config(state=tk.DISABLED)
        else:
            self.show_results()

    def select_option(self):
        selected_option = self.radio_var.get()
        correct_answer = self.questions[self.current_question_index]["answer"]

        if selected_option == correct_answer:
            self.score += 1

        self.button_next.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question_index += 1
        self.display_next_question()

    def show_results(self):
        messagebox.showinfo("Quiz Complete", f"Your score: {self.score}/{len(self.questions)}")
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    quiz_game = QuizGame(root)
    root.mainloop()
    
    
    