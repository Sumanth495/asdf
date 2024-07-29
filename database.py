import sqlite3

def create_connection():
    conn = sqlite3.connect('expense_tracker.db')
    return conn

def create_tables():
    conn = create_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            description TEXT,
            amount REAL
        )
    ''')
    # Renamed 'limit' to 'monthly_limit'
    c.execute('''
        CREATE TABLE IF NOT EXISTS settings (
            id INTEGER PRIMARY KEY,
            month TEXT,
            monthly_limit REAL
        )
    ''')
    conn.commit()
    conn.close()

def insert_expense(date, description, amount):
    conn = create_connection()
    c = conn.cursor()
    c.execute('INSERT INTO expenses (date, description, amount) VALUES (?, ?, ?)', (date, description, amount))
    conn.commit()
    conn.close()

def get_expenses(date):
    conn = create_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM expenses WHERE date LIKE ?', (f"{date}%",))
    rows = c.fetchall()
    conn.close()
    return rows

def get_total_expenses(date):
    conn = create_connection()
    c = conn.cursor()
    c.execute('SELECT SUM(amount) FROM expenses WHERE date LIKE ?', (f"{date}%",))
    total = c.fetchone()[0]
    conn.close()
    return total or 0

def set_monthly_limit(month, limit):
    conn = create_connection()
    c = conn.cursor()
    c.execute('DELETE FROM settings WHERE month = ?', (month,))
    c.execute('INSERT INTO settings (month, monthly_limit) VALUES (?, ?)', (month, limit))
    conn.commit()
    conn.close()

def get_monthly_limit(month):
    conn = create_connection()
    c = conn.cursor()
    c.execute('SELECT monthly_limit FROM settings WHERE month = ?', (month,))
    limit = c.fetchone()
    conn.close()
    return limit[0] if limit else 0
