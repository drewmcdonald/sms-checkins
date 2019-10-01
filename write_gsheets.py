from os import getenv

import datasheets
from dotenv import load_dotenv

load_dotenv()

client = datasheets.Client(service=True)


spreadsheet_name = getenv("SPREADSHEET_NAME")
tab_name = getenv("SPREADSHEET_TAB")
tab = client.fetch_workbook(spreadsheet_name).fetch_tab(tab_name)

# Extract and print all of the values
data = tab.fetch_data(headers=True, fmt="list")
print(data)

tab.append_data([["python", "added this data"]])
