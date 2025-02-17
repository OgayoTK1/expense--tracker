# Expense Tracker

A simple command-line application to track your expenses. This project allows you to add, view, and remove expenses, storing them in a JSON file.

## Features

- **Add Expense**: Record a new expense with an amount, category, and optional description.
- **View Expenses**: Display all recorded expenses with details such as date, amount, category, and description.
- **Remove Expense**: Remove a specific expense by its index.

## Requirements

- Python 3.x

## Installation

1. Clone the repository or download the `expense_tracker.py` file.
2. Ensure you have Python 3 installed on your system.

## Usage

1. Open your terminal or command prompt.
2. Navigate to the directory where `expense_tracker.py` is saved.
3. Run the script using the command: 
    ```
    python expense_tracker.py
    ```
4. Follow the on-screen prompts to add, view, or remove expenses.

## Example

```sh
$ python expense_tracker.py

Expense Tracker
1. Add Expense
2. View Expenses
3. Remove Expense
4. Exit
Choose an option: 1
Enter the amount: 50.75
Enter the category: Food
Enter a description (optional): Lunch at restaurant
Expense added successfully!

Expense Tracker
1. Add Expense
2. View Expenses
3. Remove Expense
4. Exit
Choose an option: 2

Date: 2025-02-17 10:21:38, Amount: 50.75, Category: Food, Description: Lunch at restaurant
```

## File Structure

```plaintext
.
├── README.md
└── expense_tracker.py
```

## Contributing

Feel free to fork this project, submit pull requests, or create issues if you find any bugs or have feature suggestions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```` ▋
