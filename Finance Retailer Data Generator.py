

import pandas as pd
import numpy as np
import random
import datetime


# Set random seed for reproducibility
np.random.seed(0)
random.seed(0)


# Generate synthetic customer data
def generate_customer_data(num_customers):
    customers = []
    for i in range(num_customers):
        customer_id = f"C{1000 + i}"
        age = np.random.randint(18, 80)
        gender = np.random.choice(['Male', 'Female'])
        income = np.random.randint(20000, 150000)
        education = np.random.choice(['High School', 'College', 'Graduate'])
        employment_status = np.random.choice(['Employed', 'Unemployed', 'Self-Employed'])
        marital_status = np.random.choice(['Single', 'Married', 'Divorced', 'Widowed'])
        children = np.random.randint(0, 5)
        account_balance = np.random.uniform(100, 10000)
        loan_amount = np.random.uniform(0, 5000)
        loan_status = np.random.choice(['Approved', 'Pending', 'Rejected'])
        
        customers.append([customer_id, age, gender, income, education, employment_status,
                          marital_status, children, account_balance, loan_amount, loan_status])
    
    columns = ['Customer_ID', 'Age', 'Gender', 'Income', 'Education', 'Employment_Status',
               'Marital_Status', 'Children', 'Account_Balance', 'Loan_Amount', 'Loan_Status']
    
    return pd.DataFrame(customers, columns=columns)




# Generate synthetic transaction data
def generate_transaction_data(num_transactions, start_date, end_date):
    transactions = []
    for i in range(num_transactions):
        transaction_id = f"T{1000 + i}"
        customer_id = f"C{np.random.randint(1000, 1100)}"
        transaction_date = np.random.choice(pd.date_range(start_date, end_date))
        transaction_amount = np.random.uniform(1, 1000)
        transaction_type = np.random.choice(['Purchase', 'Withdrawal', 'Deposit'])
        
        transactions.append([transaction_id, customer_id, transaction_date,
                             transaction_amount, transaction_type])
    
    columns = ['Transaction_ID', 'Customer_ID', 'Transaction_Date',
               'Transaction_Amount', 'Transaction_Type']
    
    return pd.DataFrame(transactions, columns=columns)




# Generate synthetic loan data
def generate_loan_data(num_loans):
    loans = []
    for i in range(num_loans):
        loan_id = f"L{1000 + i}"
        customer_id = f"C{np.random.randint(1000, 1100)}"
        loan_amount = np.random.uniform(1000, 50000)
        loan_duration = np.random.randint(12, 60)
        interest_rate = np.random.uniform(5, 15)
        loan_purpose = np.random.choice(['Home Improvement', 'Debt Consolidation', 'Education', 'Medical', 'Other'])
        
        loans.append([loan_id, customer_id, loan_amount, loan_duration,
                      interest_rate, loan_purpose])
    
    columns = ['Loan_ID', 'Customer_ID', 'Loan_Amount', 'Loan_Duration',
               'Interest_Rate', 'Loan_Purpose']
    
    return pd.DataFrame(loans, columns=columns)




# Generate synthetic data for the retail financial institution
num_customers = 100
num_transactions = 1000
num_loans = 50
start_date = datetime.date(2022, 1, 1)
end_date = datetime.date(2022, 12, 31)




customer_data = generate_customer_data(num_customers)
transaction_data = generate_transaction_data(num_transactions, start_date, end_date)
loan_data = generate_loan_data(num_loans)




# Save synthetic data to CSV files
customer_data.to_csv('customer_data.csv', index=False)
transaction_data.to_csv('transaction_data.csv', index=False)
loan_data.to_csv('loan_data.csv', index=False)




# Display sample data
print("Sample Customer Data:")
print(customer_data.head())
print("\nSample Transaction Data:")
print(transaction_data.head())
print("\nSample Loan Data:")
print(loan_data.head())






