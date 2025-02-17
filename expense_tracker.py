import sqlite3
from datetime import datetime

class ExpenseTracker:
    def __init__(self, db_name='expenses.db'):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY,
                    amount REAL,
                    category TEXT,
                    description TEXT,
                    date TEXT
                )
            """)

    def add_expense(self, amount, category, description, date):
        with self.conn:
            self.conn.execute("""
                INSERT INTO expenses (amount, category, description, date)
                VALUES (?, ?, ?, ?)
            """, (amount, category, description, date))

    def get_expenses(self):
        with self.conn:
            return self.conn.execute("SELECT * FROM expenses").fetchall()

    def get_expenses_by_category(self, category):
        with self.conn:
            return self.conn.execute("SELECT * FROM expenses WHERE category = ?", (category,)).fetchall()

    def get_monthly_summary(self, month, year):
        with self.conn:
            return self.conn.execute("""
                SELECT SUM(amount) FROM expenses
                WHERE strftime('%m', date) = ? AND strftime('%Y', date) = ?
            """, (month, year)).fetchone()[0]

    def update_expense(self, expense_id, amount, category, description, date):
        with self.conn:
            self.conn.execute("""
                UPDATE expenses
                SET amount = ?, category = ?, description = ?, date = ?
                WHERE id = ?
            """, (amount, category, description, date, expense_id))

    def delete_expense(self, expense_id):
        with self.conn:
            self.conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
