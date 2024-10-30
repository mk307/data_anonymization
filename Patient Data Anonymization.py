from faker import Faker
import pandas as pd

# Initializing Faker library to generate synthetic data
fake = Faker()

def anonymize_data(df):
    # Replacing each column's real data with generated fake data to anonymize patient information
    df['Name'] = [fake.name() for _ in range(len(df))]        # Generating fake names
    df['Address'] = [fake.address() for _ in range(len(df))]  # Generating fake addresses
    df['Phone'] = [fake.phone_number() for _ in range(len(df))]  # Generating fake phone numbers
    return df

# Sampling DataFrame to represent original patient data
data = {
    'Name': ['John Doe', 'Jane Smith'], 
    'Address': ['123 Main St', '456 Elm St'], 
    'Phone': ['555-1234', '555-5678']
}
df = pd.DataFrame(data)

# Applying anonymization function to the DataFrame and print the results
anonymized_df = anonymize_data(df)
print(anonymized_df)