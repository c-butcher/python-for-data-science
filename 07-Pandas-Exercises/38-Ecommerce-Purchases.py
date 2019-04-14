import pandas as pd

ecommerce = pd.read_csv('data/Ecommerce Purchases')
print(ecommerce.head())

print()
print('How many rows and columns are there?')
print(ecommerce.info())


print()
print('What is the average Purchase Price?')
print(ecommerce['Purchase Price'].mean())

print()
print('What were the highest and lowest purchase prices?')
print(ecommerce['Purchase Price'].max())
print(ecommerce['Purchase Price'].min())


print()
print("How many people have English 'en' as their Language of choice on the website?")
print(ecommerce[ecommerce['Language'] == 'en'].count())

print()
print('How many people have the job title of "Lawyer" ?')
print(ecommerce[ecommerce['Job'].str.contains('Lawyer', False)].count())

print()
print('How many people made the purchase during the AM and how many people made the purchase during PM ?')
print(ecommerce['AM or PM'].value_counts())

print()
print('What are the 5 most common Job Titles?')
print(ecommerce['Job'].value_counts().head(5))

print()
print('Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction?')
print(ecommerce[ecommerce['Lot'] == '90 WT']['Purchase Price'])

print()
print('What is the email of the person with the following Credit Card Number: 4926535242672853')
print(ecommerce[ecommerce['Credit Card'] == 4926535242672853]['Email'])

print()
print('How many people have American Express as their Credit Card Provider and made a purchase above $95 ?')
print(ecommerce[(ecommerce['CC Provider'] == 'American Express') & (ecommerce['Purchase Price'] > 95)].count())

print()
print('Hard: How many people have a credit card that expires in 2025?')
print(len(ecommerce[ecommerce['CC Exp Date'].str.contains('/25')]))

print()
print('Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)')

hosts = ecommerce['Email'].apply(lambda address: address.split('@')[1]).value_counts()
print(hosts.head(5))
