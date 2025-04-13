import sqlite3

# Function to initialize the database and create tables
def init_db():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()

    # Create tables for each course
    courses = ['FIN-3210-004', 'DS-3620-004', 'LAW-2810-002', 'DS-3850-001', 'DS-3860-001']
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

    # Insert questions for the course "FIN-3210-004"
    course = "FIN-3210-004"
    for question, answers, correct_answer in fin_3210_questions:
        # Ensure there are exactly 4 answers; pad with dummy answers if necessary
        while len(answers) < 4:
            answers.append("N/A")  # Add dummy answers if there are fewer than 4 answers

        cursor.execute(f'''
            INSERT INTO "{course}" (question_text, answer_1, answer_2, answer_3, answer_4, correct_answer)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (question, answers[0], answers[1], answers[2], answers[3], correct_answer))

    # DS-3620-004 (Business Analytics)
    ds_3620_questions = [
        ("What is difficult, if not impossible, to obtain", 
         ["Sample data", "Population data", "Big data", "Meta data"], 
         2),  # Correct answer: b (Index 2)
        
        ("What is time series data", 
         ["Records info in equal time periods", "Records info over time", "Records info from the past times", "Records info far into the future"], 
         2),  # Correct answer: b (Index 2)
        
        ("What is mode", 
         ["The center of data", "The average of data", "The number that occurs the most frequently", "The number that appears the least"], 
         3),  # Correct answer: c (Index 3)
        
        ("Range is the simplest measure of depression", 
         ["True", "False"], 
         1),  # Correct answer: a (Index 1)
        
        ("What is the name of the symbol that represents sample mean", 
         ["X-bar", "Mu", "Alpha", "Lambda"], 
         1),  # Correct answer: a (Index 1)
        
        ("The Greek symbol alpha represents the probability of error or the significance level", 
         ["True", "False"], 
         1),  # Correct answer: a (Index 1)
        
        ("What formula is similar to the regression formula", 
         ["Y = mx-b", "mx = y + b", "B = y + mx", "y = mx +b"], 
         4),  # Correct answer: d (Index 4)
        
        ("What about Regression analysis is false", 
         ["Can have causality", "Can determine important values", "Can predict other values with given data", "Can determine relationship"], 
         1),  # Correct answer: a (Index 1)
        
        ("The letter n represents the sample size", 
         ["True", "False"], 
         1),  # Correct answer: a (Index 1)
        
        ("What IS true of a Bell Curve", 
         ["The curve is NOT symmetrical", "The mean, median, and mode are all the same", "The peak is at the edges"], 
         2)   # Correct answer: b (Index 2)
    ]

    # Insert questions for the course "DS-3620-004"
    course = "DS-3620-004"
    for question, answers, correct_answer in ds_3620_questions:
        # Ensure there are exactly 4 answers; pad with dummy answers if necessary
        while len(answers) < 4:
            answers.append("N/A")  # Add dummy answers if there are fewer than 4 answers

        cursor.execute(f'''
            INSERT INTO "{course}" (question_text, answer_1, answer_2, answer_3, answer_4, correct_answer)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (question, answers[0], answers[1], answers[2], answers[3], correct_answer))

    conn.commit()
    conn.close()

# Call this function to initialize the database and pre-load questions
init_db()  # This will create tables for each course
preload_questions()  # This will insert questions into the tables
