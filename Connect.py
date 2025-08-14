from garminconnect import Garmin
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import getpass

TEST_DATE = datetime.date(2025, 8, 12)

if __name__ == "__main__":

    #username = input("Enter email address: ")
    #password = getpass("Enter password: ")

    username = "EJTriem@outlook.com"
    password = "Ou812@atm8023"

    api = Garmin(username, password)
    api.login()

    activity_start_date = datetime.date(2025, 7, 1)
    activity_end_date = datetime.date.today()

    activities = api.get_activities_by_date(
                activity_start_date.isoformat(),
                activity_end_date.isoformat()
    )

    activity_df = pd.DataFrame(activities)

    sleep = api.get_sleep_data(TEST_DATE) 

    #while activity_start_date <= activity_end_date:


    print(sleep["summary"]["overallScore"]["value"])