# Expense Tracker

A simple web-based application to track your expenses. This project allows you to add, view, categorize, update, and delete expenses, with an optional monthly summary feature.

## Features

1. **Add Expenses**
    - Form to input expense amount, category, description, and date.
2. **View Expenses**
    - Display a list of all expenses.
3. **Categorize Expenses**
    - Group expenses by categories like Food, Transport, Entertainment, Clothing, Phone Bills, Internet Bills, Miscellaneous, etc.
4. **Monthly Summary**
    - Calculate total spending for a given month.
5. **Delete/Update Expense**
    - Edit or remove expense entries.

## Technologies

- **Back-end**: Python
- **Database**: SQLite
- **Front-end**: Flask

## Additional Features to Consider

- Add charts using libraries like Matplotlib or Chart.js.
- Enable exporting data to a CSV file.

## Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/expense-tracker.git
    cd expense-tracker
    ```

2. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the application:
    ```sh
    python app.py
    ```

4. Open your web browser and go to `http://127.0.0.1:5000`.

## File Structure

```plaintext
expense-tracker/
├── app.py
├── expense_tracker.py
├── models.py
├── requirements.txt
├── static
│   └── style.css
├── templates
│   ├── base.html
│   ├── index.html
│   ├── add_expense.html
│   ├── edit_expense.html
│   └── view_expenses.html
└── README.md
```

## Contributing

Feel free to fork this project, submit pull requests, or create issues if you find any bugs or have feature suggestions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
