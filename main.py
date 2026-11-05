
import sqlite3

# STEP 1: Create a sample customer sales dataset
customers = [
    (101, "Arun", "arun@gmail.com", "9876543210", 5000),
    (102, "Priya", "priya@gmail.com", "8765432109", 7000),
    (103, "Karthik", "karthik@gmail.com", "7654321098", 3000),
    (104, "Divya", "divya@gmail.com", "6543210987", 4500),
    (105, "Rahul", "rahul@gmail.com", "9123456780", 6000)
]

# STEP 2: Create SQLite database
connection = sqlite3.connect("sales.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    phone TEXT,
    sales_amount REAL
)
""")

# Insert sample data
cursor.executemany("""
INSERT OR REPLACE INTO sales
(customer_id, name, email, phone, sales_amount)
VALUES (?, ?, ?, ?, ?)
""", customers)

connection.commit()


# STEP 3: Secure parameterized SQL query
def secure_query(customer_id):
    query = """
    SELECT customer_id, name, email, phone, sales_amount
    FROM sales
    WHERE customer_id = ?
    """

    cursor.execute(query, (customer_id,))
    return cursor.fetchall()


# STEP 4: Data masking functions
def mask_name(name):
    return name[0] + "*" * (len(name) - 1)


def mask_email(email):
    username, domain = email.split("@")
    return username[0] + "***@" + domain


def mask_phone(phone):
    return "*" * (len(phone) - 4) + phone[-4:]



# STEP 5: Role-Based Access Control

def get_customer_data(customer_id, role):

    records = secure_query(customer_id)

    if role == "admin":
        return records

    elif role == "analyst":
        masked_records = []

        for row in records:
            masked_data = (
                row[0],
                mask_name(row[1]),
                mask_email(row[2]),
                mask_phone(row[3]),
                row[4]
            )
            masked_records.append(masked_data)

        return masked_records

    else:
        raise PermissionError("Access Denied!")


# STEP 6: Display data based on user roles

print("\n===== ADMIN ACCESS =====")

for customer_id in range(101, 106):
    print(get_customer_data(customer_id, "admin"))

print("\n===== ANALYST ACCESS =====")

for customer_id in range(101, 106):
    print(get_customer_data(customer_id, "analyst"))


# Test unauthorized access
print("\n===== UNAUTHORIZED ACCESS TEST =====")

try:
    get_customer_data(101, "guest")
except PermissionError as error:
    print(error)




# STEP 6: Test SQL Injection Protection
print("\n===== SQL INJECTION TEST =====")

malicious_input = "101 OR 1=1"

result = secure_query(malicious_input)

if len(result) == 0:
    print("SQL Injection prevented successfully!")
else:
    print("Security test failed!")


# STEP 6: Close database connection
connection.close()

print("\nData security pipeline completed successfully!")
