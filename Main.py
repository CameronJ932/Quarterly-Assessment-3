import sqlite3
import tkinter as tk
from tkinter import messagebox

# admin credentials
admin_username = "admin"
admin_password = "password"

# Styling constants
FONT = ("Helvetica", 14)
BUTTON_FONT = ("Helvetica", 12, "bold")
BACKGROUND_COLOR = "#f0f0f0"
BUTTON_COLOR = "#4CAF50"
TEXT_COLOR = "#333333"

# gloabl vars for admin
entry_username = None
entry_password = None
score = 0

# Function to validate admin login
def validate_admin_login():
    global entry_username, entry_password  
    username = entry_username.get()
    password = entry_password.get()

    if username == admin_username and password == admin_password:
        open_admin_dashboard()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# validate student login
def validate_student_login():
    global score
    score = 0  # Reset score at the start
    open_quiz_window()

# open admin dashboard after login
def open_admin_dashboard():
    admin_login_window.quit()  
    admin_login_window.destroy()  
    create_admin_dashboard()  

# login window with student and admin 
def create_login_window():
    global login_window
    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("400x400")
    login_window.config(bg=BACKGROUND_COLOR)

    login_student_button = tk.Button(login_window, text="Student Login", font=BUTTON_FONT, bg=BUTTON_COLOR, fg="white", command=validate_student_login, width=20, height=2)
    login_student_button.pack(pady=10, fill="x")

    login_admin_button = tk.Button(login_window, text="Admin Login", font=BUTTON_FONT, bg=BUTTON_COLOR, fg="white", command=open_admin_login_form, width=20, height=2)
    login_admin_button.pack(pady=10, fill="x")

    login_window.mainloop()

# Admin login window
def open_admin_login_form():
    global entry_username, entry_password 
    login_window.quit()
    login_window.destroy()

    global admin_login_window
    admin_login_window = tk.Tk()
    admin_login_window.title("Admin Login")
    admin_login_window.geometry("400x300")
    admin_login_window.config(bg=BACKGROUND_COLOR)

    label_username = tk.Label(admin_login_window, text="Username:", font=FONT, bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
    label_username.pack(pady=10)
    entry_username = tk.Entry(admin_login_window, font=FONT)
    entry_username.pack(pady=5)

    label_password = tk.Label(admin_login_window, text="Password:", font=FONT, bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
    label_password.pack(pady=10)
    entry_password = tk.Entry(admin_login_window, show="*", font=FONT)
    entry_password.pack(pady=5)

    login_button = tk.Button(admin_login_window, text="Login", font=BUTTON_FONT, bg=BUTTON_COLOR, fg="white", command=validate_admin_login, width=20, height=2)
    login_button.pack(pady=20, fill="x")

    admin_login_window.mainloop()

# Admin dashboard window for questions
def create_admin_dashboard():
    dashboard_window = tk.Tk()
    dashboard_window.title("Admin Dashboard")
    dashboard_window.geometry("400x400")
    dashboard_window.config(bg=BACKGROUND_COLOR)

    button_add_question = tk.Button(dashboard_window, text="Add New Question", font=BUTTON_FONT, bg=BUTTON_COLOR, fg="white")
    button_add_question.pack(pady=15, fill="x")

    button_view_questions = tk.Button(dashboard_window, text="View Existing Questions", font=BUTTON_FONT, bg=BUTTON_COLOR, fg="white")
    button_view_questions.pack(pady=15, fill="x")

    button_modify_question = tk.Button(dashboard_window, text="Modify/Delete Question", font=BUTTON_FONT, bg=BUTTON_COLOR, fg="white")
    button_modify_question.pack(pady=15, fill="x")

    dashboard_window.mainloop()

# student quiz window
def open_quiz_window():
    global score
    quiz_window = tk.Tk()
    quiz_window.title("Quiz")
    quiz_window.geometry("500x400")
    quiz_window.config(bg=BACKGROUND_COLOR)

    question = "Placeholder Question"
    answers = ["Answer 1", "Answer 2", "Answer 3", "Answer 4"]
    correct_answer_index = 1

    # Display the question
    label_question = tk.Label(quiz_window, text=question, font=FONT, bg=BACKGROUND_COLOR, fg=TEXT_COLOR, wraplength=400)
    label_question.pack(pady=10)

    var = tk.IntVar()

    # Display the multiple choice answers
    for i, answer in enumerate(answers):
        tk.Radiobutton(quiz_window, text=answer, variable=var, value=i+1, indicatoron=0, font=FONT, bg=BACKGROUND_COLOR, fg=TEXT_COLOR).pack(fill='both', pady=5)

    # Function to check the answer
    def check_answer():
        global score
        selected_answer = var.get()
        if selected_answer == correct_answer_index:
            score += 1 
            messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", "Sorry, that's incorrect.")

        score_label.config(text=f"Current Score: {score}")

        messagebox.showinfo("Quiz Complete", f"Your final score is: {score}")
        quiz_window.quit()  # End quiz

    # Submit button
    submit_button = tk.Button(quiz_window, text="Submit Answer", font=BUTTON_FONT, bg=BUTTON_COLOR, fg="white", command=check_answer)
    submit_button.pack(pady=20)

    score_label = tk.Label(quiz_window, text=f"Current Score: {score}", font=FONT, bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
    score_label.pack(pady=10)

    quiz_window.mainloop()

# Run the login window
create_login_window()