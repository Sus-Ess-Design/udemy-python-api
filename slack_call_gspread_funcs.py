import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
from datetime import datetime

# Google Spreadsheet authetication
def auth():
    SP_CREDENTIAL_FILE = 'plugins/secret.json'
    SP_SCOPE = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
    SP_SHEET_KEY = '1UUntxWif8awnIl0YfRDJsII5Y2wZxqx3OtoOGANHZGc'
    SP_SHEET = 'timesheet'

    credentials = Credentials.from_service_account_file(SP_CREDENTIAL_FILE, scopes=SP_SCOPE)
    gc = gspread.authorize(credentials)

    worksheet = gc.open_by_key(SP_SHEET_KEY).worksheet(SP_SHEET)
    return worksheet
# for auth() test
worksheet = auth()
df = pd.DataFrame(worksheet.get_all_records())
print(df)

# Punch in 
def punch_in():
    print('Regist punch in time')
    worksheet = auth()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    date = timestamp.strftime('%Y/%m/%d')
    punch_in = timestamp.strftime('%H:%M')

    df = df.append({'Date': date, 'Punch in': punch_in, 'Punch out': '00:00'}, ignore_index=True)
    worksheet.update([df.columns.tolist()] + df.values.tolist())
    print('Register complete')
# for punch_in() test
punch_in()

# Punch out
def punch_out():
    print('Regist punch out time')
    worksheet = auth()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    punch_out = timestamp.strftime('%H:%M')

    df.iloc[-1, 2] = punch_out
    worksheet.update([df.columns.tolist()] + df.values.tolist())
    print('Register complete')
# for punch_out() test
punch_out()