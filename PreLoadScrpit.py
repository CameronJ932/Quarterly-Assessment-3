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

# Pre-load questions into the database for a specific course
def preload_questions():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()

    # Predefined questions and answers for the courses

    # FIN-3210-004 (Finance)
    fin_3210_questions = [
        ("A Financial report holds 4 basic financial statements", 
         ["Balance sheet, Income statement, Statement of cashflows, statement of stockholder’s equity", 
          "Owners’ Equity sheet, Income statement, Statement of cashflows, statement of stockholder’s equity", 
          "Balance sheet, debt sheet, current assets, statement of stockholder’s equity", 
          "Owners’ equity sheet, Income statement, Statement of cashflows, Net capital"], 
         1),  # Correct answer: a (Index 1)
        
        ("What is the formula for Net Working Capital", 
         ["= Liabilities – owners’ equity", 
          "= current assets + EBIT * debt – debt", 
          "= current assets – current liabilities", 
          "= current assets / current liabilities - debt"], 
         3),  # Correct answer: c (Index 3)
        
        ("What is depreciation", 
         ["Gain of value over time", 
          "Loss of total equity", 
          "Loss of debt", 
          "Loss of value of tangible assets"], 
         4),  # Correct answer: d (Index 4)
        
        ("What is the marginal tax rate", 
         ["The tax rate on the next dollar of income", 
          "Taxes paid divided by taxable income"], 
         1),  # Correct answer: a (Index 1)
        
        ("Capital gain means you sold an asset for more than you paid for it", 
         ["True", "False"], 
         1),  # Correct answer: a (Index 1)
        
        ("When must you report earnings to the IRS (Ignoring special considerations)", 
         ["Any amount", "$500 or more", "$1000 or more", "$2000 or more"], 
         1),  # Correct answer: a (Index 1)
        
        ("What does NPV stand for", 
         ["New present value", "Net percent value", "Net present value", "Newguard percentile variable"], 
         3),  # Correct answer: c (Index 3)
        
        ("Who controls the creation of money in the US", 
         ["The Federal Government", "The Courts", "Congress", "The Federal Reserve"], 
         4),  # Correct answer: d (Index 4)
        
        ("What drives the Stock Market", 
         ["Investors", "Buyers", "The Government", "The Bond Market"], 
         4),  # Correct answer: d (Index 4)
        
        ("Investors like return NOT risk", 
         ["True", "False"], 
         1)   # Correct answer: a (Index 1)
    ]

    # Insert questions for the course "FIN-3210-004(Finance)"
    course = "FIN-3210-004(Finance)"
    for question, answers, correct_answer in fin_3210_questions:
        # Ensure there are exactly 4 answers; pad with dummy answers if necessary
        while len(answers) < 4:
            answers.append("N/A")  # Add dummy answers if there are fewer than 4 answers

        cursor.execute(f'''
            INSERT INTO "{course}" (question_text, answer_1, answer_2, answer_3, answer_4, correct_answer)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (question, answers[0], answers[1], answers[2], answers[3], correct_answer))

    # Repeat the same process for other courses, like DS-3620-004, DS-3850-001, etc.
    # Example for DS-3620-004
    ds_3620_questions = [
        ("What is difficult, if not impossible, to obtain", 
         ["Sample data", "Population data", "Big data", "Meta data"], 
         2),  # Correct answer: b (Index 2)
        
        ("What is time series data", 
         ["Records info in equal time periods", "Records info over time", "Records info from the past times", "Records info far into the future"], 
         2),  # Correct answer: b (Index 2)
        
        # More questions...
    ]

    # Insert questions for the course "DS-3620-004(Business Analytics)"
    course = "DS-3620-004(Business Analytics)"
    for question, answers, correct_answer in ds_3620_questions:
        while len(answers) < 4:
            answers.append("N/A")

        cursor.execute(f'''
            INSERT INTO "{course}" (question_text, answer_1, answer_2, answer_3, answer_4, correct_answer)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (question, answers[0], answers[1], answers[2], answers[3], correct_answer))

    # Repeat for other courses...

    conn.commit()
    conn.close()

# Call this function to initialize the database and pre-load questions
init_db()  # This will create tables for each course
preload_questions()  # This will insert questions into the tables
