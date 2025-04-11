import sqlite3
import tkinter as tk
from tkinter import messagebox

#Login and Password
admin_username = "admin"
admin_password = "password"

# Styling constants
FONT = ("Helvetica", 14)
BUTTON_FONT = ("Helvetica", 12, "bold")
BACKGROUND_COLOR = "#f0f0f0"
BUTTON_COLOR = "#4CAF50"
TEXT_COLOR = "#333333"


# window for student and admin login
def create_login_window():
    global login_window
    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("400x400")
    login_window.config(bg=BACKGROUND_COLOR)

    # Create the student and admin buttons
    login_student_button = tk.Button(login_window, text="Student Login", font=BUTTON_FONT, bg=BUTTON_COLOR, fg="white", command=validate_student_login)
    login_student_button.pack(pady=10, fill="x")

    login_admin_button = tk.Button(login_window, text="Admin Login", font=BUTTON_FONT, bg=BUTTON_COLOR, fg="white", command=open_admin_login_form)
    login_admin_button.pack(pady=10, fill="x")

    login_window.mainloop()

#Admin login form where user is promted for username and password
def open_admin_login_form():

    global entry_username, entry_password
    login_window.quit()
    login_window.destroy()

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

    login_button = tk.Button(admin_login_window, text="Login", font=BUTTON_FONT, bg=BUTTON_COLOR, fg="white", command=validate_admin_login)
    login_button.pack(pady=20, fill="x")

    admin_login_window.mainloop()

# Admin dashboard window for managing questions
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