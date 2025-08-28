import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set(style="whitegrid")

# USING MATPLOTLIB

# Line Plot using matplotlib
years = [2019, 2020, 2021, 2022, 2023]
costs = [15000, 16000, 17500, 18000, 19500]

plt.figure(figsize=(6, 4))
plt.plot(years, costs, marker='o', color='blue', label='Part Cost')
plt.title('Car Part Cost Over Years (Matplotlib)')
plt.xlabel('Year')
plt.ylabel('Cost (₹)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Pie Chart using matplotlib
languages = ['C', 'C++', 'Python', 'Java', 'JavaScript']
students = [40, 35, 80, 60, 25]

plt.figure(figsize=(6, 6))
plt.pie(students, labels=languages, autopct='%1.1f%%', startangle=140)
plt.title('Programming Languages in BCA (Matplotlib)')
plt.axis('equal')
plt.tight_layout()
plt.show()

# Scatter Plot using matplotlib
semesters = [1, 2, 3, 4, 5, 6]
marks = [65, 70, 68, 75, 80, 85]

plt.figure(figsize=(6, 4))
plt.scatter(semesters, marks, color='green', s=100)
plt.title('Marks in Each Semester (Matplotlib)')
plt.xlabel('Semester')
plt.ylabel('Marks')
plt.xticks(semesters)
plt.tight_layout()
plt.show()

# USING SEABORN

# Line Plot using seaborn
line_data = pd.DataFrame({
    'Year': years,
    'Cost': costs
})

plt.figure(figsize=(6, 4))
sns.lineplot(data=line_data, x='Year', y='Cost', marker='o', color='blue', label='Part Cost')
plt.title('Car Part Cost Over Years (Seaborn)')
plt.xlabel('Year')
plt.ylabel('Cost (₹)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Scatter Plot using seaborn
scatter_data = pd.DataFrame({
    'Semester': semesters,
    'Marks': marks
})

plt.figure(figsize=(6, 4))
sns.scatterplot(data=scatter_data, x='Semester', y='Marks', color='green', s=100)
plt.title('Marks in Each Semester (Seaborn)')
plt.xlabel('Semester')
plt.ylabel('Marks')
plt.xticks(scatter_data['Semester'])
plt.tight_layout()
plt.show()

# Pie Chart (no seaborn version — still uses matplotlib)
plt.figure(figsize=(6, 6))
plt.pie(students, labels=languages, autopct='%1.1f%%', startangle=140)
plt.title('Programming Languages in BCA (Seaborn Practical - Pie via Matplotlib)')
plt.axis('equal')
plt.tight_layout()
plt.show()
