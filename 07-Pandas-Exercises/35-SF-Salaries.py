import pandas as pd

# Read the salary data into our data-frame.
salaries = pd.read_csv('data/Salaries.csv')

print('Use the .head() method to make sure it is loaded...')
head = salaries.head()
print(head)

print()
print('Use the .info() method to find out how many entries there are...')
info = salaries.info()
print(info)

print()
print('What is the average BasePay?')
average_base_pay = salaries['BasePay'].mean()
print(average_base_pay)


print()
print('What is the highest amount of OvertimePay in the dataset?')
highest_overtime_pay = salaries['OvertimePay'].max()
print(highest_overtime_pay)

print()
print('What is the job title of JOSEPH DRISCOLL')
joseph = salaries[salaries['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']
print(joseph)

print()
print('How much does JOSEPH DRISCOLL make (including benefits)?')
joseph = salaries[salaries['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']
print(joseph)

# Could have used the argmax() method to retreive it also...
# salaries.iloc[salaries['TotalPayBenefits'].argmax()]
print()
print('What is the name of the highest paid person (including benefits)?')
highest_paid = salaries.sort_values('TotalPayBenefits').loc[0]
print(highest_paid)

# Could have used the argmax() method to retreive it also...
# salaries.iloc[salaries['TotalPayBenefits'].argmin()]
print()
print('What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?')
lowest_paid = salaries[salaries['TotalPayBenefits'] == salaries['TotalPayBenefits'].min()]
print(lowest_paid)

print()
print('What was the average (mean) BasePay of all employees per year? (2011-2014) ?')
average_pay_by_year = salaries.groupby('Year')['BasePay'].mean()
print(average_pay_by_year)

print()
print('How many unique job titles are there?')
num_unique_titles = salaries['JobTitle'].nunique()
print(num_unique_titles)

print()
print('What are the top 5 most common jobs?')
job_count = salaries['JobTitle'].value_counts()
print(job_count.head())

print()
print('How many Job Titles were represented by only one person in 2013?')
job_counts_for_2013 = salaries[salaries['Year'] == 2013]['JobTitle'].value_counts()
single_person_job_count = job_counts_for_2013[job_counts_for_2013 == 1].count()
print(single_person_job_count)

print()
print('How many people have the word Chief in their job title?')
jobs_with_chief_in_title = salaries['JobTitle'].str.contains('chief', False).sum()
print(jobs_with_chief_in_title)

print()
print('Bonus: Is there a correlation between length of the Job Title string and Salary?')
salaries['title_len'] = salaries['JobTitle'].str.len()
correlation = salaries[['title_len', 'TotalPayBenefits']].corr()
print(correlation)
