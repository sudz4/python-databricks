"""
Create a sample employee database
"""

import pandas as pd

# Generate data for 100 employees
employee_ids = [f"{i:04d}" for i in range(1, 101)]
first_names = ["John", "Jane", "Bob", "Alice", "Mike", "Emily", "David", "Ashley", "James", "Samantha",
               "Chris", "Emma", "Steven", "Sara", "Daniel", "Rachel", "Andrew", "Olivia", "Benjamin", "Ava"] * 5
last_names = ["Smith", "Doe", "Williams", "Johnson", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez",
              "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Jackson", "White", "Harris"] * 5
usernames = [f"{first_name[0]}{last_name}" for first_name, last_name in zip(first_names, last_names)]

# Create DataFrame
data = {'EmployeeID': employee_ids, 'FirstName': first_names, 'LastName': last_names, 'Username': usernames}
employee_df = pd.DataFrame(data)

print(employee_df)
