import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load the data set
df = pd.read_csv("Telco-Customer-Churn.csv")
# Clean the totalCharges column
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(inplace=True)
# Drop non-informative ID column
df.drop(columns=['customerID'], inplace=True)
# Convert Churn to Binary
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
# EDA 1: Churn distribution by tenure
sns.histplot(data=df, x='tenure', hue='Churn', kde=True)
plt.title('Churn Distribution by Tenure')
plt.xlabel('Tenure (Months)')
plt.ylabel('Number of Customers')
plt.savefig("churn_tenure.png")
plt.show()
# EDA 2: Churn by contract type
sns.countplot(data=df, x='Contract', hue='Churn')
plt.title('Churn by Contract Type')
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("churn_contract.png")
plt.show()