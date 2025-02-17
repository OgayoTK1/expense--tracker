from flask import Flask, render_template, request, redirect, url_for
from models import db, Expense
from expense_tracker import ExpenseTracker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
db.init_app(app)
tracker = ExpenseTracker()

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        amount = request.form['amount']
        category = request.form['category']
        description = request.form['description']
        date = request.form['date']
        tracker.add_expense(amount, category, description, date)
        return redirect(url_for('view_expenses'))
    return render_template('add_expense.html')

@app.route('/expenses')
def view_expenses():
    expenses = tracker.get_expenses()
    return render_template('view_expenses.html', expenses=expenses)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_expense(id):
    expense = Expense.query.get(id)
    if request.method == 'POST':
        expense.amount = request.form['amount']
        expense.category = request.form['category']
        expense.description = request.form['description']
        expense.date = request.form['date']
        db.session.commit()
        return redirect(url_for('view_expenses'))
    return render_template('edit_expense.html', expense=expense)

@app.route('/delete/<int:id>')
def delete_expense(id):
    tracker.delete_expense(id)
    return redirect(url_for('view_expenses'))

if __name__ == "__main__":
    app.run(debug=True)
