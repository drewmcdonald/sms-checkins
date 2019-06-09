import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
from os import getenv

load_dotenv()


# use creds to create a client to interact with the Google Drive API
scope = ["https://www.googleapis.com/auth/spreadsheets"]

service_account_path = getenv("SERVICE_ACCOUNT_JSON_PATH")
print(service_account_path)

creds = ServiceAccountCredentials.from_json_keyfile_name(service_account_path, scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
spreadsheet_name = getenv("SPREADSHEET_NAME")
sheet = client.open(spreadsheet_name).sheet1

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)
