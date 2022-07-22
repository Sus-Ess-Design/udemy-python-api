from datetime import date
import gspread
import pandas as pd
from time import sleep
from datetime import datetime
from google.oauth2.service_account import Credentials
from gspread_dataframe import set_with_dataframe

# Google Spreadsheet authetication
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
SP_SHEET = 'new'

sh = gc.open_by_key(SP_SHEET_KEY)
worksheet = sh.worksheet(SP_SHEET)

# Add date and send to Spreadsheet
dt_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
data = [dt_now]
print(data)
worksheet.append_row(data)