from main import *


def big_countries_test() -> pd.DataFrame:
    data = [['Afghanistan', 'Asia', 652230, 25500100, 20343000000], ['Albania', 'Europe', 28748, 2831741, 12960000000],
            ['Algeria', 'Africa', 2381741, 37100000, 188681000000], ['Andorra', 'Europe', 468, 78115, 3712000000],
            ['Angola', 'Africa', 1246700, 20609294, 100990000000]]
    World = pd.DataFrame(data, columns=['name', 'continent', 'area', 'population', 'gdp']).astype(
        {'name': 'object', 'continent': 'object', 'area': 'Int64', 'population': 'Int64', 'gdp': 'Int64'})
    return big_countries(World)


def find_products_test() -> pd.DataFrame:
    data = [['0', 'Y', 'N'], ['1', 'Y', 'Y'], ['2', 'N', 'Y'], ['3', 'Y', 'Y'], ['4', 'N', 'N']]
    Products = pd.DataFrame(data, columns=['product_id', 'low_fats', 'recyclable']).astype(
        {'product_id': 'int64', 'low_fats': 'category', 'recyclable': 'category'})
    return find_products(Products)


def find_customers_test() -> pd.DataFrame:
    data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
    Customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id': 'Int64', 'name': 'object'})
    data = [[1, 3], [2, 1]]
    Orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id': 'Int64', 'customerId': 'Int64'})
    return find_customers(Customers, Orders)


def article_views_test():
    data = [[1, 3, 5, '2019-08-01'], [1, 3, 6, '2019-08-02'], [2, 7, 7, '2019-08-01'], [2, 7, 6, '2019-08-02'],
            [4, 7, 1, '2019-07-22'], [3, 4, 4, '2019-07-21'], [3, 4, 4, '2019-07-21']]
    Views = pd.DataFrame(data, columns=['article_id', 'author_id', 'viewer_id', 'view_date']).astype(
        {'article_id': 'Int64', 'author_id': 'Int64', 'viewer_id': 'Int64', 'view_date': 'datetime64[ns]'})
    return article_views(Views)


def calculate_special_bonus_test():
    data = [[2, 'Meir', 3000], [3, 'Michael', 3800], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700]]
    Employees = pd.DataFrame(data, columns=['employee_id', 'name', 'salary']).astype(
        {'employee_id': 'int64', 'name': 'object', 'salary': 'int64'})
    return calculate_special_bonus(Employees)


def fix_names_test() -> pd.DataFrame:
    data = [[1, 'aLice'], [2, 'bOB']]
    Users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id': 'Int64', 'name': 'object'})
    return fix_names(Users)


def valid_emails_test() -> pd.DataFrame:
    data = [[1, 'Winston', 'winston@leetcode.com'], [2, 'Jonathan', 'jonathanisgreat'],
            [3, 'Annabelle', 'bella-@leetcode.com'], [4, 'Sally', 'sally.come@leetcode.com'],
            [5, 'Marwan', 'quarz#2020@leetcode.com'], [6, 'David', 'david69@gmail.com'],
            [7, 'Shapiro', '.shapo@leetcode.com']]
    Users = pd.DataFrame(data, columns=['user_id', 'name', 'mail']).astype(
        {'user_id': 'int64', 'name': 'object', 'mail': 'object'})
    return valid_emails(Users)


def find_patients_test() -> pd.DataFrame:
    data = [[1, 'Daniel', 'YFEV COUGH'], [2, 'Alice', ''], [3, 'Bob', 'DIAB100 MYOP'], [4, 'George', 'ACNE DIAB100'],
            [5, 'Alain', 'DIAB201'], [6, 'Tmp', 'SDIAB201'], [7, 'Tmp2', 'DATA SDIAB201']]
    Patients = pd.DataFrame(data, columns=['patient_id', 'patient_name', 'conditions']).astype(
        {'patient_id': 'int64', 'patient_name': 'object', 'conditions': 'object'})
    return find_patients(Patients)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    df = find_patients_test()
    print(df.head())