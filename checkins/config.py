import os

from dotenv import load_dotenv

load_dotenv()

WEBHOOK_URL = os.getenv("WEBHOOK_URL")
SPREADSHEET_NAME = os.getenv("SPREADSHEET_NAME")
SPREADSHEET_TAB = os.getenv("SPREADSHEET_TAB")


__all__ = ["WEBHOOK_URL", "SPREADSHEET_NAME", "SPREADSHEET_TAB"]
