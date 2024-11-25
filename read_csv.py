import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('StudentsPerformance.csv')
print(df.head())

print(df.describe())
print(df.isnull().sum())

plt.figure(figsize=(12, 8))

plt.subplot(221)
df['gender'].value_counts().plot(kind='bar', title='Gender Distribution')

plt.subplot(222)
df['race/ethnicity'].value_counts().plot(kind='bar', title='Race/Ethnicity Distribution')

plt.subplot(223)
df['lunch'].value_counts().plot(kind='bar', title='Lunch Distribution')

plt.subplot(224)
df['test preparation course'].value_counts().plot(kind='bar', title='Test Preparation CourseDistribution')

plt.tight_layout()
plt.show()

df[['math score', 'reading score', 'writing score']].hist(bins=10, figsize=(12, 8), grid=False)
plt.tight_layout()
plt.show()

corr = df[['math score', 'reading score', 'writing score']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
plt.title("Correlation Heatmap")
plt.show()