import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# ----------------------------------
# a) Car part cost in last 5 years (Line Chart)
# ----------------------------------
years = [2019, 2020, 2021, 2022, 2023]
engine_cost = [50000, 52000, 54000, 57000, 60000]
tyres_cost = [20000, 21000, 23000, 25000, 27000]

car_cost_df = pd.DataFrame({
    'Year': years,
    'Engine': engine_cost,
    'Tyres': tyres_cost
})

plt.figure(figsize=(8, 5))
sns.lineplot(x='Year', y='Engine', data=car_cost_df, label='Engine Cost', marker='o')
sns.lineplot(x='Year', y='Tyres', data=car_cost_df, label='Tyres Cost', marker='o')
plt.title("Car Part Costs Over Last 5 Years")
plt.ylabel("Cost (INR)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# ----------------------------------
# b) Programming languages learned in BCA (Pie Chart)
# ----------------------------------
languages = ['Python', 'C', 'C++', 'Java', 'HTML', 'JavaScript']
count = [80, 60, 50, 55, 90, 40]

plt.figure(figsize=(7, 7))
plt.pie(count, labels=languages, autopct='%1.1f%%', startangle=140)
plt.title("Programming Languages Learned in BCA")
plt.tight_layout()
plt.show()

# ----------------------------------
# c) Marks in semesters (Scatter Plot)
# ----------------------------------
semesters = [1, 2, 3, 4, 5, 6]
marks = [72, 75, 78, 82, 80, 85]

plt.figure(figsize=(8, 5))
sns.scatterplot(x=semesters, y=marks, s=100, color="orange")
plt.title("Marks in Semesters")
plt.xlabel("Semester")
plt.ylabel("Marks (%)")
plt.grid(True)
plt.tight_layout()
plt.show()
