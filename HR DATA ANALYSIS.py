import pandas as pd

df = pd.read_csv('HR Data.csv')
print(df)

# Drop unnecessary columns

df_cleand = df.drop(['EmployeeCount', 'Over18', 'StandardHours'], axis=1)

# Rename columns
new_column_names = {
    'Age': 'Age',
    'Attrition': 'Attrition',
    'BusinessTravel': 'BusinessTravel',
    'DailyRate': 'DailyRate',
    'Department': 'Department',
}

df_cleaned = df_cleand.rename(columns=new_column_names)

#Remoove duplicate entries

df_cleaned = df_cleaned.drop_duplicates()

#Sanitize specific columns (Example : convert BusinessTravel values to lowercase)

df_cleand['BusinessTravel'] = df_cleaned['BusinessTravel'].str.lower()

#check for NaN values and drop rows with Nan values
df_cleaned = df_cleaned.dropna()

# Perform additional data cleaning or transformations as needed
# Example: Convert categorical variables to numerical using one-hot encoding
df_encoded = pd.get_dummies(df_cleaned, columns=['BusinessTravel', 'Department', 'Gender', 'MaritalStatus', 'JobRole'])

# Export the cleaned DataFrame to a CSV file
df_cleaned.to_csv(r'C:\Users\ajayk\Desktop\cleaned_data.csv', index=False)


