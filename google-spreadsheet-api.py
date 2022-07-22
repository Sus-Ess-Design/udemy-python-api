import gspread
import pandas as pd
from google.oauth2.service_account import Credentials
from gspread_dataframe import set_with_dataframe

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(
    'secret.json',
    scopes=scopes
)

gc = gspread.authorize(credentials)

SP_SHEET_KEY = '1UUntxWif8awnIl0YfRDJsII5Y2wZxqx3OtoOGANHZGc'
SP_SHEET = 'demo'

sh = gc.open_by_key(SP_SHEET_KEY)
worksheet = sh.worksheet(SP_SHEET)
data = worksheet.get_all_values()
df = pd.DataFrame(data[2:], columns=data[1])
df = df.drop(df.columns[[0]], axis=1)
print(df)
print(df.shape)

print(df.dtypes)
df = df.astype({'年齢': int, '社員ID': int})
print(df.dtypes)
pivot = df.pivot_table(index=['所属'], values=['年齢'], aggfunc='mean')
pivot['年齢'] = pivot['年齢'].round()
print(pivot)
pivot = pivot.reset_index()
print(pivot)

new_worksheet = sh.add_worksheet(title='new', rows=100, cols=100)
first_row = 2
first_col = 2
set_with_dataframe(new_worksheet, pivot, row=first_row, col=first_col)