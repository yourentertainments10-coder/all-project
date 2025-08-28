import pandas as pd
company={
"Name":['anuj','Rohit','Krish'],
"Department":['sale','finanace','business'],
"manager":['M1','M2','M3'],
"Salary":[11000,12000,15000] }
df=pd.DataFrame(company)
print(df)

df.loc[df['Name'] == 'Krish', 'Salary'] = 65000
df.loc[df['Name'] == 'Krish', 'manager'] = 'M4'

print("\nUpdated DataFrame (After modifying krish's salary and manager):\n")
print(df)

