import datasheets

from checkins.config import SPREADSHEET_NAME, SPREADSHEET_TAB

client = datasheets.Client(service=True)


tab = client.fetch_workbook(SPREADSHEET_NAME).fetch_tab(SPREADSHEET_TAB)

# Extract and print all of the values
data = tab.fetch_data(headers=True, fmt="list")
print(data)

tab.append_data([["python", "added this data"]])
