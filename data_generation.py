import pandas as pd
import random
from faker import Faker
from datetime import timedelta

# Initialize Faker with Indian locale
fake = Faker('en_IN')

# Define dataset parameters
categories = ['Road Construction', 'Sewerage', 'Street Light', 'Water Supply', 'Garbage Collection']
areas = ['Indra Nagar', 'Civil Lines', 'Basharatpur', 'Mohaddipur', 'Golghar']
statuses = ['Resolved', 'Pending', 'In-Progress']

data = []

# Define the total number of records to generate
total_records = 50000

for i in range(total_records):
    complaint_id = f"CMPL-{10000+i}"
    category = random.choice(categories)
    area = random.choice(areas)
    status = random.choice(statuses)
    priority = random.choice(['High', 'Medium', 'Low'])

    # Generate a filing date within the past 2 years
    filing_date = fake.date_between(start_date='-2y', end_date='today')

    # Logic to simulate realistic resolution delays
    if status == 'Resolved':
        if category == 'Road Construction':
            delay_days = random.randint(30, 180)
        elif category == 'Street Light':
            delay_days = random.randint(1, 15)
        else:
            delay_days = random.randint(5, 60)
            
        resolution_date = filing_date + timedelta(days=delay_days)
    else:
        resolution_date = None

    data.append([complaint_id, category, area, priority, status, filing_date, resolution_date])

# Convert to Pandas DataFrame
df = pd.DataFrame(data, columns=[
    'Complaint_ID', 'Category', 'Area', 'Priority', 'Status', 'Filing_Date', 'Resolution_Date'
])

# Export to CSV
output_filename = 'civic_complaints_data.csv'
df.to_csv(output_filename, index=False)

# Console confirmation
print(f"Data generation complete. Successfully exported {total_records} records to '{output_filename}'.")