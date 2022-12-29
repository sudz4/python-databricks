import pandas as pd
import random
from datetime import datetime, timedelta

# Generate data for 1000 transactions
transaction_descriptions = ["Meal with client", "Air travel", "Hotel stay", "Car rental", "Office supplies", "Entertainment"]
amounts = [random.uniform(50, 200) for _ in range(1000)]

# Generate random transaction and submitted dates
min_date = datetime.strptime("2022-01-01", "%Y-%m-%d")
max_date = datetime.strptime("2022-12-31", "%Y-%m-%d")
delta = max_date - min_date
transaction_dates = [min_date + timedelta(days=random.randint(0, delta.days)) for _ in range(1000)]
submitted_dates = [date + timedelta(days=random.randint(1, 14)) for date in transaction_dates]

# Create DataFrame
data = {'TransactionDescription': [random.choice(transaction_descriptions) for _ in range(1000)],
        'TransactionDate': transaction_dates,
        'SubmittedDate': submitted_dates,
        'Amount': amounts}
trans_df = pd.DataFrame(data)

# round the amount column to two decimal places (currency)

trans_df['Amount'] = trans_df['Amount'].round(2)

print(trans_df)


