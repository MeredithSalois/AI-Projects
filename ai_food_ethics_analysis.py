import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset from GitHub CSV file
github_csv_url = "https://raw.githubusercontent.com/MeredithSalois/AI-Projects/main/Auditing%20Let's%20Foodie.csv"
df = pd.read_csv(github_csv_url)

# Ensure necessary columns exist
expected_columns = {'Recipe', 'Cuisine', 'Recommended_Count', 'User_Accepts', 'User_Cultural_Group'}
if not expected_columns.issubset(df.columns):
    raise ValueError("Missing one or more expected columns in dataset")

# Calculate acceptance rate per cuisine
df['Acceptance_Rate'] = df['User_Accepts'] / df['Recommended_Count']

# Plot distribution of recommendations per cuisine
plt.figure(figsize=(10, 6))
sns.barplot(x='Cuisine', y='Recommended_Count', data=df, palette='viridis')
plt.title('Distribution of AI Recipe Recommendations by Cuisine')
plt.xlabel('Cuisine Type')
plt.ylabel('Number of Recommendations')
plt.xticks(rotation=45)
plt.show()

# Plot acceptance rate per cuisine
plt.figure(figsize=(10, 6))
sns.barplot(x='Cuisine', y='Acceptance_Rate', data=df, palette='coolwarm')
plt.title('User Acceptance Rate by Cuisine Type')
plt.xlabel('Cuisine Type')
plt.ylabel('Acceptance Rate')
plt.xticks(rotation=45)
plt.ylim(0, 1)  # Ensure valid y-axis range
plt.show()

# Identify potential cultural insensitivity
cultural_restrictions = {
    'Halal': ['Pork'],
    'Kosher': ['Shellfish'],
    'Vegan': ['Meat']
}

# Function to check for cultural mismatches
def check_cultural_sensitivity(recipe, user_group):
    if user_group == 'Middle Eastern' and 'Pork' in recipe:
        return 'Potentially Inappropriate'
    elif user_group == 'Jewish' and 'Shellfish' in recipe:
        return 'Potentially Inappropriate'
    elif user_group == 'Vegan' and 'Meat' in recipe:
        return 'Potentially Inappropriate'
    return 'Appropriate'

# Apply cultural sensitivity check
df['Cultural_Sensitivity'] = df.apply(lambda x: check_cultural_sensitivity(x['Recipe'], x['User_Cultural_Group']), axis=1)

# Display flagged issues
flagged_issues = df[df['Cultural_Sensitivity'] == 'Potentially Inappropriate']
print("Flagged Cultural Sensitivity Issues:")
print(flagged_issues[['Recipe', 'User_Cultural_Group', 'Cultural_Sensitivity']])