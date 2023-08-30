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


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    ser = sorted(employee['salary'].unique(), reverse=True)
    if len(ser) < 2:
        return pd.DataFrame([None], columns=['SecondHighestSalary'])

    return pd.DataFrame([ser[1]], columns=['SecondHighestSalary'])


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df_res = employee.groupby(by=["departmentId"]).max()[['salary']]
    df_res = df_res.merge(employee, on=["departmentId", "salary"])
    df_res = df_res.merge(department, left_on="departmentId", right_on="id")[['name_y', 'name_x', 'salary']]
    return df_res.rename(columns={'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'})


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    scores.sort_values(by=['rank'], inplace=True)
    scores.drop(columns=['id'], inplace=True)
    return scores


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id', inplace=True)
    person.drop(person[person['email'].duplicated()].index, inplace=True)


def delete_duplicate_emails_2(person: pd.DataFrame) -> None:
    person.sort_values(by="id", inplace=True)
    person.drop_duplicates(["email"], inplace=True)


def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    # products = products.fillna(-1)
    products = products.melt(
        id_vars="product_id",
        value_vars=["store1", "store2", "store3"],
        value_name="price",
        var_name="store",
    )
    return products.dropna()


def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    uniq = store[store['amount'] > 500]['customer_id'].unique()
    count = len(uniq)
    return pd.DataFrame([count], columns=['rich_count'])


def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    tmp_count = delivery[delivery['order_date'] == delivery['customer_pref_delivery_date']]['delivery_id'].count()
    d_count = delivery['delivery_id'].count()
    res = round(tmp_count/d_count, 2)
    return pd.DataFrame({'immediate_percentage': [res]})


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
            'category': ['Low Salary', 'Average Salary', 'High Salary'],
            'accounts_count': [
                accounts[accounts.income < 20000].shape[0],
                accounts[(accounts.income >= 20000) & (accounts.income <= 50000)].shape[0],
                accounts[accounts.income > 50000].shape[0],
            ],
        })


def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    return employees.groupby(by=["event_day", "emp_id"]).sum().reset_index()[['event_day', 'emp_id', 'total_time']].rename(columns={'event_day': 'day', })


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return activity.groupby('player_id')['event_date'].min().reset_index().rename(columns={'event_date': 'first_login'})


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    return teacher.groupby('teacher_id')["subject_id"].nunique().reset_index().rename(columns={'subject_id': 'cnt'})


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders.groupby('customer_number').count().reset_index()
    orders.sort_values(by='order_number', inplace=True, ascending=False)
    if orders.shape[0] == 0:
        return orders[['customer_number']]
    return orders[['customer_number']].iloc[[0]]


def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    return daily_sales.groupby(by=['date_id', 'make_name']).nunique().reset_index().rename(columns={'lead_id':'unique_leads', 'partner_id': 'unique_partners'})
