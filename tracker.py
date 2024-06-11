import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Function to collect expenses from the user
def collect_expenses():
    expenses = []
    while True:
        category = input("Enter expense category (or type 'done' to finish): ")
        if category.lower() == 'done':
            break
        amount = float(input("Enter expense amount: "))
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        expenses.append((date, category, amount))
    return expenses

# Function to save expenses to an Excel file
def save_to_excel(expenses):
    df = pd.DataFrame(expenses, columns=['Date', 'Category', 'Amount'])
    df.to_excel('expenses.xlsx', index=False)

# Function to create Bar Chart for Expense Categories
def create_bar_chart(expenses):
    df = pd.DataFrame(expenses, columns=['Date', 'Category', 'Amount'])
    category_total = df.groupby('Category')['Amount'].sum()
    category_total.plot(kind='bar', rot=45)
    plt.title('Expense Categories')
    plt.xlabel('Category')
    plt.ylabel('Total Amount')
    plt.tight_layout()
    plt.show()

# Function to create Time Series Plot for Expenses Over Time
def create_time_series_plot(expenses):
    df = pd.DataFrame(expenses, columns=['Date', 'Category', 'Amount'])
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df.resample('D').sum().plot()
    plt.title('Expenses Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Amount')
    plt.tight_layout()
    plt.show()

# Function to create Pie Chart for Expense Distribution
def create_pie_chart(expenses):
    df = pd.DataFrame(expenses, columns=['Date', 'Category', 'Amount'])
    category_total = df.groupby('Category')['Amount'].sum()
    category_total.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Expense Distribution')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()

# Main function
def main():
    expenses = collect_expenses()
    save_to_excel(expenses)
    create_bar_chart(expenses)
    create_time_series_plot(expenses)
    create_pie_chart(expenses)

if __name__ == "__main__":
    main()
