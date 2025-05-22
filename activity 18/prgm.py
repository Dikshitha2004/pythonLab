import pandas as pd

# 1. Initial E-commerce DataFrame
data = {
    'Order_ID': [101, 102, 103, 104, 105],
    'Customer_Name': ['Alice Johnson', 'Bob Smith', 'Charlie Brown', 'David Wilson', 'Eva Adams'],
    'Product': ['Laptop', 'Headphones', 'Smartphone', 'Tablet', 'Smartwatch'],
    'Category': ['Electronics', 'Accessories', 'Electronics', 'Electronics', 'Wearables'],
    'Price': [800, 50, 600, 300, 150],
    'Quantity': [1, 2, 1, 1, 1]
}

df = pd.DataFrame(data)

# 2. Add new column: Order_Status
df['Order_Status'] = ['Shipped', 'Pending', 'Delivered', 'Shipped', 'Pending']

# 3. Add multiple columns: Shipping_Partner & Review_Rating
df['Shipping_Partner'] = ['FedEx', 'DHL', 'UPS', 'Amazon Logistics', 'Blue Dart']
df['Review_Rating'] = [4.5, 4.0, 3.8, 4.2, 4.7]

# 4. Add column at specific index (index 2): Payment_Method
df.insert(2, 'Payment_Method', ['Credit Card', 'PayPal', 'Debit Card', 'Net Banking', 'UPI'])

# 5. Delete the Review_Rating column
df.drop('Review_Rating', axis=1, inplace=True)

# Display the final DataFrame
print(df)
