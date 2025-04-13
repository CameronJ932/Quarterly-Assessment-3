import sqlite3

# Function to initialize the database and create tables
def init_db():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()

    # Create tables for each course with the full class name format
    courses = [
        'FIN-3210-004(Finance)', 
        'DS-3620-004(Business Analytics)', 
        'LAW-2810-002(Business Legal)',  # Added LAW section
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

    # Insert questions for the course "DS-3620-004(Business Analytics)"
    course = "DS-3620-004(Business Analytics)"
    for question, answers, correct_answer in ds_3620_questions:
        while len(answers) < 4:
            answers.append("N/A")

        cursor.execute(f'''
            INSERT INTO "{course}" (question_text, answer_1, answer_2, answer_3, answer_4, correct_answer)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (question, answers[0], answers[1], answers[2], answers[3], correct_answer))

    # LAW-2810-002 (Business Legal)
    law_2810_questions = [
        ("What type of court jurisdiction has unlimited jurisdiction", 
         ["None", "General", "Probate", "liability"], 
         2),  # Correct answer: b (Index 2)
        
        ("What is the highest court in the US", 
         ["State court", "US Court of Appeals", "Specialized Courts", "Supreme Court"], 
         4),  # Correct answer: d (Index 4)
        
        ("How many justices does the Supreme Court have", 
         ["3", "5", "8", "9"], 
         4),  # Correct answer: d (Index 4)
        
        ("Children (Under the age of 18) can enter contracts", 
         ["True", "False"], 
         1),  # Correct answer: a (Index 1)
        
        ("Children (Under the age of 18) can end contracts at any time", 
         ["True", "False"], 
         1),  # Correct answer: a (Index 1)
        
        ("What is the WARN act", 
         ["An act made to warn employees of potential hiring opportunities", 
          "An act to warn employees of incoming layoffs", 
          "An act made to warn employees of possible workplace hazards", 
          "An act made to help employers warn other employers of troubled employees"], 
         2),  # Correct answer: b (Index 2)
        
        ("What are all executive branch employees", 
         ["Tenured employees", "Executive employees", "At will employees", "Immune employees"], 
         3),  # Correct answer: c (Index 3)
        
        ("Ethics have to do with all of these except what", 
         ["Fairness", "Justness", "Rightness", "Lawfulness"], 
         4),  # Correct answer: d (Index 4)
        
        ("What does IDDR stand for", 
         ["I Desire to Do Right", "I Demand to Deny Rights", "Interdimensional dynamic response", "I desire for doomed rides"], 
         1),  # Correct answer: a (Index 1)
        
        ("Employers cannot be successfully sued for harassment in the workplace if proper action is taken", 
         ["True", "False"], 
         1)   # Correct answer: a (Index 1)
    ]

    # Insert questions for the course "LAW-2810-002(Business Legal)"
    course = "LAW-2810-002(Business Legal)"
    for question, answers, correct_answer in law_2810_questions:
        while len(answers) < 4:
            answers.append("N/A")

        cursor.execute(f'''
            INSERT INTO "{course}" (question_text, answer_1, answer_2, answer_3, answer_4, correct_answer)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (question, answers[0], answers[1], answers[2], answers[3], correct_answer))

    # DS-3850-001 (Database Management)
    ds_3850_questions = [
        ("What is the proper syntax for printing to the terminal in Python", 
         ["print()", "cout >>  “”", "Print  “”", "Cout <<  “”"], 
         1),  # Correct answer: a (Index 1)
        
        ("What is the error   def func()", 
         ["It is missing {}", "It is missing :", "it is missing ;", "It is missing (main)"], 
         2),  # Correct answer: b (Index 2)
        
        ("Which is a proper import statement", 
         ["Import, os:", "sqlite3 import", "import, sqrt from math", "import math"], 
         4),  # Correct answer: d (Index 4)
        
        ("A bool can only have two outputs: True or False", 
         ["True", "False"], 
         1),  # Correct answer: a (Index 1)
        
        ("Num, string, bool, and type are all examples of variables", 
         ["True", "False"], 
         2),  # Correct answer: b (Index 2)
        
        ("A String can ONLY contain characters", 
         ["True", "False"], 
         1),  # Correct answer: a (Index 1)
        
        ("What value for a Float is valid", 
         ["1.a", "3,6,7", "4.5", "1-5"], 
         3),  # Correct answer: c (Index 3)
        
        ("What does != mean", 
         ["Equal to", "Could equal", "Get", "Not equal to"], 
         4),  # Correct answer: d (Index 4)
        
        ("What are the symbols for arithmetic operations", 
         ["!, [, +, -", "+,-,&,^", "+,-,/,*", "*,/,@,#"], 
         3),  # Correct answer: c (Index 3)
        
        ("Can variable names start with number", 
         ["Yes", "No"], 
         2)   # Correct answer: b (Index 2)
    ]

    # Insert questions for the course "DS-3850-001(Database Management)"
    course = "DS-3850-001(Database Management)"
    for question, answers, correct_answer in ds_3850_questions:
        while len(answers) < 4:
            answers.append("N/A")

        cursor.execute(f'''
            INSERT INTO "{course}" (question_text, answer_1, answer_2, answer_3, answer_4, correct_answer)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (question, answers[0], answers[1], answers[2], answers[3], correct_answer))

    # DS-3860-001 (Business Database)
    ds_3860_questions = [
        ("The term NOSQL means that SQL will not be used in the database", 
         ["True", "False"], 
         1),  # Correct answer: a (Index 1)
        
        ("ACID compliance includes all the following except", 
         ["Atomicity", "Consistency", "Isolation", "Density"], 
         4),  # Correct answer: d (Index 4)
        
        ("Which of the following are valid cardinality examples", 
         ["Many:2", "1:1", "1:3", "None:1"], 
         2),  # Correct answer: b (Index 2)
        
        ("What is Normalization", 
         ["Make everything normal", "Putting data into specific tables even if they conflict", 
          "Putting data into the right tables", "Checking data for errors"], 
         3),  # Correct answer: c (Index 3)
        
        ("Entities should not be in a many-to-many relationship", 
         ["True", "False"], 
         1),  # Correct answer: a (Index 1)
        
        ("What does an assumption do in ER models", 
         ["Allow us to make up any info we want to suit our needs", 
          "Pull in data we assume is correct even if it is not", 
          "Lets us pretend aspects of an entity are not true", 
          "It allows us to pull in factual outside knowledge"], 
         4),  # Correct answer: d (Index 4)
        
        ("What is the name of an entity between two many-to-many relationships", 
         ["Break entity", "Skip entity", "Intersection entity", "Ignore entity"], 
         3),  # Correct answer: c (Index 3)
        
        ("Some entity relationships are recursive", 
         ["True", "False"], 
         1),  # Correct answer: a (Index 1)
        
        ("Which of the following are not valid anomalies", 
         ["Insertion", "Deletion", "Modification", "Addition"], 
         4),  # Correct answer: d (Index 4)
        
        ("What is a candidate key", 
         ["The primary key", "A key that could be the Primary key", "A copy of the primary key", "A dead key"], 
         2)   # Correct answer: b (Index 2)
    ]

    # Insert questions for the course "DS-3860-001(Business Database)"
    course = "DS-3860-001(Business Database)"
    for question, answers, correct_answer in ds_3860_questions:
        while len(answers) < 4:
            answers.append("N/A")

        cursor.execute(f'''
            INSERT INTO "{course}" (question_text, answer_1, answer_2, answer_3, answer_4, correct_answer)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (question, answers[0], answers[1], answers[2], answers[3], correct_answer))

    conn.commit()
    conn.close()

# Call this function to initialize the database and pre-load questions
init_db()  # This will create tables for each course
preload_questions()  # This will insert questions into the tables