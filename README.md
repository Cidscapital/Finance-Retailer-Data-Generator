# Finance-Retailer-Data-Generator
This tool generates synthetic data for simulating customer information, transaction history, and loan data for a retail financial institution. The generated data can be used for various purposes such as customer relationship management (CRM), predictive modeling, and data analysis.

## Demo

[https://cidscapital.github.io/Finance-Retailer-Data-Generator/](Demo) 

## Features
- Generates synthetic customer data including demographics, income, education level, etc.
- Simulates transaction history data with details such as transaction amount, date, and type.
- Generates loan data with attributes including loan amount, duration, interest rate, etc.
- Allows customization of data size and distribution parameters.
- Outputs data in CSV format for easy integration with data analysis tools.

## Installation
1. Clone or download the repository.
2. Ensure Python 3.x is installed on your system.
3. Install required dependencies using the following command:

```
pip install -r requirements.txt
```

## Usage
1. Run the `Finance Retailer Data Generator.py` script.
2. Edit the code to specify data size and distribution parameters.
3. The generated data will be saved in CSV files in the specified directory.

## Example
To generate data with default settings:

```
python Finance_Retailer_Data_Generator.py
```

- You can open the `Finance Retailer Data Generator.ipynb` to for jupyter notebook users.
  
## Data Description
The generated data includes three CSV files:
- `customer_data.csv`: Contains synthetic customer information such as Customer_ID, Age, Gender, Income, Education, etc.
- `transaction_data.csv`: Simulates transaction history with attributes like Transaction_ID, Customer_ID, Transaction_Date, Transaction_Amount, etc.
- `loan_data.csv`: Generates loan data including Loan_ID, Customer_ID, Loan_Amount, Loan_Duration, Interest_Rate, etc.

## Acknowledgements
This tool utilizes the Faker library for generating synthetic data. Credits to the Faker development team for their contribution.

## License
This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](LICENSE) file for details.
