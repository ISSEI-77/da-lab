import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("healthcare_data.csv")
print("\n🔍 Sample Data:")
print(df.head())

print("\n📊 Summary Statistics:")
print(df.describe())

# Include categorical stats
print("\n🧾 Categorical Summary:")
print(df.describe(include='object'))

print("\n🔢 Diagnosis Frequency:")
print(df['Diagnosis'].value_counts())

print("\n🔢 Outcome Frequency:")
print(df['Outcome'].value_counts())

print("\n📈 Age Statistics:")
print("Mean Age:", df['Age'].mean())
print("Median Age:", df['Age'].median())
print("Mode Age:", df['Age'].mode()[0])


# a. Diagnosis Distribution - Bar Chart
plt.figure(figsize=(6,4))
df['Diagnosis'].value_counts().plot(kind='bar', color='skyblue')
plt.title("Diagnosis Distribution")
plt.ylabel("Number of Patients")
plt.xlabel("Diagnosis")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# b. Age Distribution - Histogram
plt.figure(figsize=(6,4))
plt.hist(df['Age'], bins=5, color='lightgreen', edgecolor='black')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Patients")
plt.grid(True)
plt.tight_layout()
plt.show()

# d. Box Plot of BP by Diagnosis
plt.figure(figsize=(6,4))
sns.boxplot(x='Diagnosis', y='BP', data=df, hue='Diagnosis', palette='Set2', legend=False)
plt.title("Blood Pressure by Diagnosis")
plt.ylabel("BP (mmHg)")
plt.tight_layout()
plt.show()


