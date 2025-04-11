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