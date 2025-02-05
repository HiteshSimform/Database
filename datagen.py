import json
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

def generate_records(num_records=100):
    records = []
    start_date = datetime.now()
    
    for i in range(1, num_records + 1):
        registration_date = start_date - timedelta(days=random.randint(0, 365))
        last_login_date = registration_date + timedelta(days=random.randint(0, 365))
        
        record = {
            "id": i,
            "name": fake.name(),
            "email": fake.email(),
            "age": random.randint(22, 55),
            "city": fake.city(),
            "country": fake.country(),
            "profession": fake.job(),
            "salary": random.randint(50000, 150000),
            "isActive": random.choice([True, False]),
            "registrationDate": registration_date.strftime('%Y-%m-%d'),
            "lastLoginDate": last_login_date.strftime('%Y-%m-%d'),
            "accountCreated": {
                "timestamp": registration_date.isoformat(),
                "timezone": "UTC"
            },
            "metadata": {
                "createdAt": registration_date.timestamp(),
                "updatedAt": last_login_date.timestamp()
            }
        }
        records.append(record)
    
    return records

# Generate and save records
records = generate_records()
with open('mongodb_dynamic_dates.json', 'w') as f:
    json.dump(records, f, indent=2)
