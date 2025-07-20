import pandas as pd

def get_login_data():
    df=pd.read_excel("test_data/test_data_login.xlsx")
    return [(row["username"],row["password"],row["expected"])for _, row in df.iterrows()]
