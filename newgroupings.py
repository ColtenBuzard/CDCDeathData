# This library faciliates 2-dimensional array operations and visualization
import pandas as pd

#This code adds the custom groupings to the 

excel_file_path = 'G:/1. Death Data/CDCDeathData/2018-2021 UCD.xlsx'
mapping_path = 'G:/1. Death Data/CDCDeathData/updated_customgroupings.xlsx'
# Specify the engine as 'openpyxl'
df = pd.read_excel(excel_file_path, engine='openpyxl')
mapping_df = pd.read_excel(mapping_path, engine='openpyxl')

# Step 1: Create a mapping dictionary
grouping_dict = pd.Series(mapping_df['Grouping Name'].values, index=mapping_df['ICD-10 Code']).to_dict()

# Assuming your original DataFrame is 'df' and it has a column 'ICD_Code'
# Step 2: Map Groupings to Original DataFrame
df['Grouping'] = df['Cause of death Code'].map(grouping_dict)

# Step 3: Handle Missing Mappings (if any ICD codes are not in your mapping dictionary)
# Replace NaN in 'Grouping' with 'Other' or any default category
df['Grouping'].fillna('Other', inplace=True)

# Display the updated DataFrame
df.head()

# Display the first few rows to verify
# Replace 'df' with the name of your DataFrame
cause_of_death_codes = df[df['Grouping'] == 'Other']['Cause of death Code']

# Displaying the result
cause_of_death_codes.head()

excel_file_path = 'G:/1. Death Data/CDCDeathData/2018-2021groupings.xlsx'  # Specify your desired file path and name

# Saving the DataFrame to an Excel file
df.to_excel(excel_file_path, index=False)