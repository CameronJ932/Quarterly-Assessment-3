import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to initialize the database and create tables
def init_db():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()

    # Create tables for each course with the full class name format
    courses = [
        'FIN-3210-004(Finance)', 
        'DS-3620-004(Business Analytics)', 
        'LAW-2810-002(Business Legal)',  
        'DS-3850-001(Database Management)', 
        'DS-3860-001(Business Database)'
    ]
    
    for course in courses:
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS "{course}" (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question_text TEXT NOT NULL,
                answer_1 TEXT NOT NULL,
                answer_2 TEXT NOT NULL,
                answer_3 TEXT NOT NULL,
                answer_4 TEXT NOT NULL,
                correct_answer INTEGER NOT NULL
            )
        ''')

    conn.commit()
    conn.close()

# Fetch questions from the database for a specific class
def get_questions_for_class(course):
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()

    cursor.execute(f'SELECT * FROM "{course}"')
    questions = cursor.fetchall()

    conn.close()

    return questions  # Returns a list of questions from the database

# Function to validate admin login
def validate_admin_login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "admin":
        open_admin_dashboard()
    else:
        messagebox.showerror("Invalid Credentials", "Incorrect username or password")

# Function to validate student login
def validate_student_login():
    student_window.quit()
    student_window.destroy()

    show_class_selection_window()  # Show the class selection window after successful login

# Function to show the class selection window
def show_class_selection_window():
    global class_selection_window, selected_class
    class_selection_window = tk.Tk()
    class_selection_window.title("Class Selection")
    class_selection_window.geometry("800x500")  # Increased window size
    class_selection_window.config(bg="lightblue")

    class_label = tk.Label(class_selection_window, text="Select Your Class", font=("Arial", 16), bg="lightblue")
    class_label.pack(pady=20)

    class_options = [
        "FIN-3210-004(Finance)", 
        "DS-3620-004(Business Analytics)", 
        "LAW-2810-002(Business Legal)", 
        "DS-3850-001(Database Management)", 
        "DS-3860-001(Business Database)"
    ]

    selected_class = tk.StringVar()
    selected_class.set(class_options[0])  # Default to first option

    class_dropdown = tk.OptionMenu(class_selection_window, selected_class, *class_options)
    class_dropdown.pack(pady=10)

    start_button = tk.Button(class_selection_window, text="Select", font=("Arial", 14), bg="green", fg="white", command=start_quiz)
    start_button.pack(pady=20)

    class_selection_window.mainloop()

# Function to start the quiz based on the selected class
def start_quiz():
    class_selection_window.quit()
    class_selection_window.destroy()

    selected_class_name = selected_class.get()  # Get the selected class
    questions = get_questions_for_class(selected_class_name)

    open_quiz_window(questions)

# Function to start the quiz window and display the questions
def open_quiz_window(questions):
    global score, current_question  # Declare as global to modify within the function
    score = 0
    current_question = 0  # Start from the first question
    quiz_window = tk.Tk()
    quiz_window.title("Quiz")
    quiz_window.geometry("800x500")  # Increased window size
    quiz_window.config(bg="lightblue")

    def show_next_question():
        global current_question  # Use global to update the index

        if current_question < len(questions):
            question_data = questions[current_question]
            
            question_text = question_data[1]
            answers = [question_data[2], question_data[3], question_data[4], question_data[5]]
            correct_answer_index = question_data[6]

            label_question.config(text=question_text)

            for i, answer in enumerate(answers):
                radio_buttons[i].config(text=answer)

            # Store the correct answer index in the radio button value
            var.set(0)  # Reset the radio button selection for the new question
            
            submit_button.config(command=lambda: check_answer(correct_answer_index))

        else:
            # If no more questions are left, show the final score and exit the quiz
            messagebox.showinfo("Quiz Complete", f"Your final score is: {score} out of 10")
            quiz_window.quit()
            quiz_window.destroy()  # Close the quiz window

            # Restart the quiz by going back to the class selection screen
            show_class_selection_window()

    def check_answer(correct_answer_index):
        global score, current_question

        selected_answer = var.get()
        if selected_answer == correct_answer_index:
            score += 1
            messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", "Sorry, that's incorrect.")

        score_label.config(text=f"Current Score: {score}")

        # Move to the next question
        current_question += 1
        show_next_question()  # Display the next question

    # Display the first question
    label_question = tk.Label(quiz_window, text="", font=("Arial", 16), bg="lightblue", fg="black", wraplength=400)
    label_question.pack(pady=10)

    var = tk.IntVar()

    radio_buttons = []
    for i in range(4):  # Create 4 radio buttons for each answer option
        radio_button = tk.Radiobutton(quiz_window, variable=var, value=i+1, indicatoron=0, font=("Arial", 12), bg="lightblue", fg="black")
        radio_button.pack(fill='both', pady=5)
        radio_buttons.append(radio_button)

    # Submit button to check the answer
    submit_button = tk.Button(quiz_window, text="Submit Answer", font=("Arial", 14), bg="green", fg="white")
    submit_button.pack(pady=20)

    score_label = tk.Label(quiz_window, text=f"Current Score: {score}", font=("Arial", 14), bg="lightblue", fg="black")
    score_label.pack(pady=10)

    # Start by displaying the first question
    show_next_question()

    quiz_window.mainloop()

# Function to start the admin dashboard
def open_admin_dashboard():
    global admin_dashboard, selected_class_for_admin
    admin_dashboard = tk.Tk()
    admin_dashboard.title("Admin Dashboard")
    admin_dashboard.geometry("600x500")  # Increased window size
    
    label_dashboard = tk.Label(admin_dashboard, text="Welcome to Admin Dashboard", font=("Arial", 16))
    label_dashboard.pack(pady=30)

    class_label = tk.Label(admin_dashboard, text="Select Class to Manage", font=("Arial", 14))
    class_label.pack(pady=10)

    class_options = [
        "FIN-3210-004(Finance)", 
        "DS-3620-004(Business Analytics)", 
        "LAW-2810-002(Business Legal)", 
        "DS-3850-001(Database Management)", 
        "DS-3860-001(Business Database)"
    ]

    selected_class_for_admin = tk.StringVar()
    selected_class_for_admin.set(class_options[0])  # Default to first option

    class_dropdown = tk.OptionMenu(admin_dashboard, selected_class_for_admin, *class_options)
    class_dropdown.pack(pady=10)

    # Buttons to manage questions
    add_button = tk.Button(admin_dashboard, text="Add Question", font=("Arial", 14), command=open_add_question_window)
    add_button.pack(pady=10)

    edit_button = tk.Button(admin_dashboard, text="Edit Question", font=("Arial", 14), command=open_edit_question_window)
    edit_button.pack(pady=10)

    delete_button = tk.Button(admin_dashboard, text="Delete Question", font=("Arial", 14), command=open_delete_question_window)
    delete_button.pack(pady=10)

    # Button to go back to login screen
    back_button = tk.Button(admin_dashboard, text="Back to Login", font=("Arial", 14), command=go_back_to_login)
    back_button.pack(pady=20)

    admin_dashboard.mainloop()

# Function to add a question
def open_add_question_window():
    global selected_class_for_admin
    selected_class_for_admin = selected_class_for_admin.get()
    add_question_window = tk.Tk()
    add_question_window.title("Add Question")
    add_question_window.geometry("800x500")

    label = tk.Label(add_question_window, text="Enter the question and answers")
    label.pack(pady=10)

    question_entry = tk.Entry(add_question_window, width=40)
    question_entry.pack(pady=5)

    answer1_entry = tk.Entry(add_question_window, width=40)
    answer1_entry.pack(pady=5)

    answer2_entry = tk.Entry(add_question_window, width=40)
    answer2_entry.pack(pady=5)

    answer3_entry = tk.Entry(add_question_window, width=40)
    answer3_entry.pack(pady=5)

    answer4_entry = tk.Entry(add_question_window, width=40)
    answer4_entry.pack(pady=5)

    correct_answer_entry = tk.Entry(add_question_window, width=40)
    correct_answer_entry.pack(pady=5)

    # Button to add the question to the database
    def add_question():
        question = question_entry.get()
        answer1 = answer1_entry.get()
        answer2 = answer2_entry.get()
        answer3 = answer3_entry.get()
        answer4 = answer4_entry.get()
        correct_answer = correct_answer_entry.get()

        if not all([question, answer1, answer2, answer3, answer4, correct_answer]):
            messagebox.showerror("Error", "Please fill out all fields.")
            return

        conn = sqlite3.connect('quiz.db')
        cursor = conn.cursor()

        cursor.execute(f'''INSERT INTO "{selected_class_for_admin}" (question_text, answer_1, answer_2, answer_3, answer_4, correct_answer)
                          VALUES (?, ?, ?, ?, ?, ?)''', (question, answer1, answer2, answer3, answer4, correct_answer))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Question added successfully.")
        add_question_window.quit()

    add_button = tk.Button(add_question_window, text="Add Question", font=("Arial", 12), command=add_question)
    add_button.pack(pady=10)

    add_question_window.mainloop()

# Function to edit a question
def open_edit_question_window():
    global selected_class_for_admin
    selected_class_for_admin = selected_class_for_admin.get()
    edit_question_window = tk.Tk()
    edit_question_window.title("Edit Question")
    edit_question_window.geometry("800x500")

    label = tk.Label(edit_question_window, text="Enter the question ID to edit")
    label.pack(pady=10)

    question_id_entry = tk.Entry(edit_question_window, width=40)
    question_id_entry.pack(pady=5)

    # Function to fetch and display the question to edit
    def fetch_and_edit():
        question_id = question_id_entry.get()
        
        if not question_id.isdigit():
            messagebox.showerror("Error", "Please enter a valid question ID.")
            return

        conn = sqlite3.connect('quiz.db')
        cursor = conn.cursor()

        cursor.execute(f'''SELECT * FROM "{selected_class_for_admin}" WHERE id = ?''', (question_id,))
        question = cursor.fetchone()

        if not question:
            messagebox.showerror("Error", "Question not found.")
            return

        question_entry.delete(0, tk.END)
        question_entry.insert(0, question[1])

        answer1_entry.delete(0, tk.END)
        answer1_entry.insert(0, question[2])

        answer2_entry.delete(0, tk.END)
        answer2_entry.insert(0, question[3])

        answer3_entry.delete(0, tk.END)
        answer3_entry.insert(0, question[4])

        answer4_entry.delete(0, tk.END)
        answer4_entry.insert(0, question[5])

        correct_answer_entry.delete(0, tk.END)
        correct_answer_entry.insert(0, question[6])

    question_entry = tk.Entry(edit_question_window, width=40)
    question_entry.pack(pady=5)

    answer1_entry = tk.Entry(edit_question_window, width=40)
    answer1_entry.pack(pady=5)

    answer2_entry = tk.Entry(edit_question_window, width=40)
    answer2_entry.pack(pady=5)

    answer3_entry = tk.Entry(edit_question_window, width=40)
    answer3_entry.pack(pady=5)

    answer4_entry = tk.Entry(edit_question_window, width=40)
    answer4_entry.pack(pady=5)

    correct_answer_entry = tk.Entry(edit_question_window, width=40)
    correct_answer_entry.pack(pady=5)

    fetch_button = tk.Button(edit_question_window, text="Fetch Question", font=("Arial", 12), command=fetch_and_edit)
    fetch_button.pack(pady=10)

    def save_edited_question():
        question_id = question_id_entry.get()
        question_text = question_entry.get()
        answer1 = answer1_entry.get()
        answer2 = answer2_entry.get()
        answer3 = answer3_entry.get()
        answer4 = answer4_entry.get()
        correct_answer = correct_answer_entry.get()

        if not all([question_text, answer1, answer2, answer3, answer4, correct_answer]):
            messagebox.showerror("Error", "Please fill out all fields.")
            return

        conn = sqlite3.connect('quiz.db')
        cursor = conn.cursor()

        cursor.execute(f'''UPDATE "{selected_class_for_admin}" SET question_text = ?, answer_1 = ?, answer_2 = ?, answer_3 = ?, answer_4 = ?, correct_answer = ? 
                          WHERE id = ?''', (question_text, answer1, answer2, answer3, answer4, correct_answer, question_id))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Question updated successfully.")
        edit_question_window.quit()

    save_button = tk.Button(edit_question_window, text="Save Changes", font=("Arial", 12), command=save_edited_question)
    save_button.pack(pady=10)

    edit_question_window.mainloop()

# Function to delete a question
def open_delete_question_window():
    global selected_class_for_admin
    selected_class_for_admin = selected_class_for_admin.get()
    delete_question_window = tk.Tk()
    delete_question_window.title("Delete Question")
    delete_question_window.geometry("800x500")

    label = tk.Label(delete_question_window, text="Enter the question ID to delete")
    label.pack(pady=10)

    question_id_entry = tk.Entry(delete_question_window, width=40)
    question_id_entry.pack(pady=5)

    def delete_question():
        question_id = question_id_entry.get()
        
        if not question_id.isdigit():
            messagebox.showerror("Error", "Please enter a valid question ID.")
            return

        conn = sqlite3.connect('quiz.db')
        cursor = conn.cursor()

        cursor.execute(f'''DELETE FROM "{selected_class_for_admin}" WHERE id = ?''', (question_id,))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Question deleted successfully.")
        delete_question_window.quit()

    delete_button = tk.Button(delete_question_window, text="Delete Question", font=("Arial", 12), command=delete_question)
    delete_button.pack(pady=10)

    delete_question_window.mainloop()

# Go back to the login screen from the admin dashboard
def go_back_to_login():
    admin_dashboard.quit()
    admin_dashboard.destroy()
    login_screen()

# Function to start the login screendis
def login_screen():
    global student_window, entry_username, entry_password
    student_window = tk.Tk()
    student_window.title("Student Login")
    student_window.geometry("800x500")  # Increased window size
    student_window.config(bg="lightblue")

    label_username = tk.Label(student_window, text="Username:", font=("Arial", 14), bg="lightblue")
    label_username.pack(pady=10)

    entry_username = tk.Entry(student_window, font=("Arial", 14))
    entry_username.pack(pady=10)

    label_password = tk.Label(student_window, text="Password:", font=("Arial", 14), bg="lightblue")
    label_password.pack(pady=10)

    entry_password = tk.Entry(student_window, font=("Arial", 14), show="*")
    entry_password.pack(pady=10)

    login_button = tk.Button(student_window, text="Login as Student \n(No Authentication required)", font=("Arial", 14), bg="green", fg="white", command=validate_student_login)
    login_button.pack(pady=20)

    admin_button = tk.Button(student_window, text="Login as Admin", font=("Arial", 14), bg="green", fg="white", command=validate_admin_login)
    admin_button.pack(pady=10)

    student_window.mainloop()

# Run the login screen function
init_db()  # Initialize the database with tables
login_screen()  # Start the login screen
