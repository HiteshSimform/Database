# from pymongo import MongoClient
# import random
# from datetime import datetime

# class EmployeeDataGenerator:
#     def __init__(self):
#         # MongoDB Connection
#         self.client = MongoClient('mongodb+srv://hiteshjethava:Hitesh1593@cluster0.jspdn.mongodb.net/')
#         self.db = self.client['employeeDB']
#         self.collection = self.db['employees']

#         # Configuration Arrays
#         self.departments = [
#             'Sales', 'Marketing', 'Engineering', 
#             'Human Resources', 'Finance', 'Customer Support', 
#             'Product Management', 'Design', 'Operations'
#         ]

#         self.skills = [
#             'communication', 'leadership', 'problem-solving', 
#             'teamwork', 'data analysis', 'project management', 
#             'coding', 'design', 'marketing', 'sales strategy'
#         ]

#     def generate_salary(self):
#         """Generate salary based on different levels"""
#         salary_ranges = {
#             'Entry Level': (800000, 1500000),
#             'Mid Level': (1500000, 2500000),
#             'Senior Level': (2500000, 4500000),
#             'Executive Level': (4500000, 7500000)
#         }

#         level = random.choice(list(salary_ranges.keys()))
#         min_salary, max_salary = salary_ranges[level]
#         return random.randint(min_salary, max_salary)

#     def generate_employee(self, index):
#         """Generate a single employee document"""
#         salary = self.generate_salary()

#         return {
#             'employeeId': f'EMP-{str(index + 1).zfill(3)}',
#             'name': f'Employee {index + 1}',
#             'department': random.choice(self.departments),
#             'salary': salary,
#             'skills': random.sample(self.skills, 3),
#             'status': random.choice(['active', 'inactive']),
#             'contact': {
#                 'email': f'employee{index + 1}@company.com',
#                 'phone': f'+91-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}'
#             },
#             'performance': {
#                 'rating': round(random.uniform(0, 5), 2)
#             },
#             'metadata': {
#                 'createdAt': datetime.now()
#             }
#         }

#     def insert_employees_batch(self, count=200, batch_size=50):
#         """Insert employees in batches"""
#         self.collection.delete_many({})  # Clear existing data

#         for i in range(0, count, batch_size):
#             batch = [
#                 self.generate_employee(index) 
#                 for index in range(i, min(i + batch_size, count))
#             ]
            
#             try:
#                 result = self.collection.insert_many(batch)
#                 print(f"Inserted batch starting from index {i}")
#             except Exception as e:
#                 print(f"Error in batch starting from index {i}: {e}")

#     def create_indexes(self):
#         """Create indexes on specific fields"""
#         self.collection.create_indexes([
#             ('department', 1),
#             ('salary', 1),
#             ('contact.email', 1)
#         ])
#         print("Indexes created successfully")

#     def validate_insertion(self):
#         """Validate data insertion and provide statistics"""
#         total_count = self.collection.count_documents({})
#         print(f"Total Employees Inserted: {total_count}")

#         department_stats = list(self.collection.aggregate([
#             {
#                 '$group': {
#                     '_id': '$department',
#                     'count': {'$sum': 1},
#                     'avgSalary': {'$avg': '$salary'}
#                 }
#             }
#         ]))

#         print("Department Statistics:")
#         for stat in department_stats:
#             print(f"Department: {stat['_id']}")
#             print(f"Count: {stat['count']}")
#             print(f"Average Salary: {stat['avgSalary']:,.2f}")
#             print("---")

# def main():
#     generator = EmployeeDataGenerator()
#     generator.insert_employees_batch(200)
#     # generator.create_indexes()
#     # generator.validate_insertion()

# if __name__ == "__main__":
#     main()

from pymongo import MongoClient
import random
from datetime import datetime
import faker
from pymongo import IndexModel, ASCENDING
from pymongo.errors import PyMongoError


class EmployeeDataGenerator:
    def __init__(self):
        # MongoDB Connection
        self.client = MongoClient('mongodb+srv://hiteshjethava:Hitesh1593@cluster0.jspdn.mongodb.net/')
        self.db = self.client['employeeDB']
        self.collection = self.db['employees']
        
        # Faker for more realistic data
        self.fake = faker.Faker('en_IN')

        # Configuration Arrays
        self.departments = [
            'Sales', 'Marketing', 'Engineering', 
            'Human Resources', 'Finance', 'Customer Support', 
            'Product Management', 'Design', 'Operations'
        ]

        self.skills = [
            'communication', 'leadership', 'problem-solving', 
            'teamwork', 'data analysis', 'project management', 
            'coding', 'design', 'marketing', 'sales strategy'
        ]

    def generate_salary(self, level):
        """Generate more realistic salary based on levels"""
        salary_ranges = {
            'Entry Level': (50000, 100000),
            'Mid Level': (100000, 250000),
            'Senior Level': (250000, 500000),
            'Executive Level': (500000, 1000000)
        }

        min_salary, max_salary = salary_ranges[level]
        return random.randint(min_salary, max_salary)

    def generate_employee(self, index):
        """Generate a single employee document with more realistic data"""
        # Introduce controlled duplicates
        levels = ['Entry Level', 'Mid Level', 'Senior Level', 'Executive Level']
        level = levels[index % len(levels)]
        
        salary = self.generate_salary(level)

        return {
            'employeeId': f'EMP-{str(index + 1).zfill(3)}',
            'name': self.fake.name(),  # More realistic names
            'department': self.departments[index % len(self.departments)],  # Controlled department assignment
            'salary': salary,
            'skills': random.sample(self.skills, 3),
            'status': ['active', 'inactive'][index % 2],  # Controlled status
            'contact': {
                'email': f'employee{(index % 10) + 1}@company.com',  # Introduce duplicates
                'phone': self.fake.phone_number()
            },
            'performance': {
                'rating': round(random.uniform(1, 5), 2)
            },
            'metadata': {
                'createdAt': datetime.now(),
                'level': level  # Added employment level
            }
        }

    def insert_employees_batch(self, count=200, batch_size=50):
        """Insert employees in batches with duplicate strategy"""
        # Clear existing data
        self.collection.delete_many({})  

        for i in range(0, count, batch_size):
            batch = [
                self.generate_employee(index) 
                for index in range(i, min(i + batch_size, count))
            ]
            
            try:
                result = self.collection.insert_many(batch)
                print(f"Inserted batch starting from index {i}")
            except Exception as e:
                print(f"Error in batch starting from index {i}: {e}")

    # def create_indexes(self):
    #     """Create indexes on specific fields"""
    #     self.collection.create_indexes([
    #         ('department', 1),
    #         ('salary', 1),
    #         ('contact.email', 1)
    #     ])
    #     print("Indexes created successfully")
    def create_indexes(self):
        """Create indexes on specific fields"""
        try:
            # Create index models
            indexes = [
                IndexModel([('department', ASCENDING)], name='department_index'),
                IndexModel([('salary', ASCENDING)], name='salary_index'),
                IndexModel([('contact.email', ASCENDING)], name='email_index')
            ]
            
            # Create indexes
            result = self.collection.create_indexes(indexes)
            print("Indexes created successfully")
            print("Created indexes:", result)
        except PyMongoError as e:
            print(f"Error creating indexes: {e}")

    def find_duplicates(self):
        """Find duplicate emails using aggregation"""
        duplicate_emails = list(self.collection.aggregate([
            {
                '$group': {
                    '_id': '$contact.email',
                    'count': {'$sum': 1},
                    'employees': {'$push': '$name'}
                }
            },
            {
                '$match': {
                    'count': {'$gt': 1}
                }
            },
            {
                '$project': {
                    'email': '$_id',
                    'count': 1,
                    'employees': 1
                }
            }
        ]))

        print("\nDuplicate Email Analysis:")
        for dup in duplicate_emails:
            print(f"Email: {dup['email']}")
            print(f"Duplicate Count: {dup['count']}")
            print(f"Employees: {dup['employees']}")
            print("---")

    def validate_insertion(self):
        """Validate data insertion and provide statistics"""
        total_count = self.collection.count_documents({})
        print(f"Total Employees Inserted: {total_count}")

        department_stats = list(self.collection.aggregate([
            {
                '$group': {
                    '_id': '$department',
                    'count': {'$sum': 1},
                    'avgSalary': {'$avg': '$salary'}
                }
            }
        ]))

        print("\nDepartment Statistics:")
        for stat in department_stats:
            print(f"Department: {stat['_id']}")
            print(f"Count: {stat['count']}")
            print(f"Average Salary: {stat['avgSalary']:,.2f}")
            print("---")

def main():
    generator = EmployeeDataGenerator()
    # generator.insert_employees_batch(200)
    generator.create_indexes()
    # generator.validate_insertion()
    # generator.find_duplicates()

if __name__ == "__main__":
    main()
