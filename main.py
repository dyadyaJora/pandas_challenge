import pandas as pd
import re


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world[(world['population'] >= 25000000) | (world['area'] >= 3000000)]


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')][['product_id']]


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left')
    df = df[df['customerId'].isna()][['name']]
    return df.rename(columns={'name': 'Customers'})


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id'] == views['viewer_id']]['author_id'].unique()
    df = sorted(df)
    return pd.DataFrame(df, columns=['id'])


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(
        lambda row: row['salary'] if row['employee_id'] % 2 == 1 and not row['name'].startswith('M') else 0, axis=1)
    employees.sort_values(by='employee_id')
    return employees[['employee_id', 'bonus']]


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users.apply(lambda row: row['name'].capitalize(), axis=1)
    users = users.sort_values(by='user_id')
    return users


emails_pattern = r'^[A-Za-z][A-Za-z0-9_.-]*@leetcode[.]com'


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users[users["mail"].str.match(emails_pattern)]


diab_pattern = r'(\s|\b)DIAB1'


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients["conditions"].str.contains(diab_pattern)]


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    ser = sorted(employee['salary'].unique(), reverse=True)
    if len(ser) < N:
        return pd.DataFrame([None], columns=['getNthHighestSalary(' + str(N) + ')'])

    return pd.DataFrame([ser[N-1]], columns=['getNthHighestSalary(' + str(N) + ')'])
