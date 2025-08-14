from garminconnect import Garmin
import datetime
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import getpass

if __name__ == "__main__":

    username = input("Enter email address: ")
    password = getpass("Enter password: ")

    api = Garmin(username, password).login()

    activity_start_date = datetime.date(2025, 7, 1)
    activity_end_date = date.today()