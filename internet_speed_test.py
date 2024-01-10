# pip install speedtest-cli
# pip install pandas
# pip install openpyxl

import speedtest, datetime # import `speedtest` and `datetime`.
import pandas as pd # import `pandas` as `pd` for dataframes and `to_excel()`.

duration = 1200 #? {seconds} How long do you want to test for?

st = speedtest.Speedtest() # Create the speedtest object.
df = pd.DataFrame(columns = ["date-time","download (b/s)","upload (b/s)"]) # Make our DataFrame with columns.

time_now = datetime.datetime.now() # Fetch the current time.
target_time = time_now + datetime.timedelta(0,duration) # Calculate the time we should stop at.

print("Starting tests:")
while time_now <= target_time: # While we still have time to run:
    print(f"> Estimate: {(target_time - time_now).seconds} seconds left\n> Download test started...")
    down = st.download() # Do the download test.
    time_now = datetime.datetime.now() # Check the time.
    print(f"> Estimate: {(target_time - time_now).seconds} seconds left\n> Upload test started...")
    up = st.upload() # Do the upload test.
    df.loc[len(df.index)] = [
        ((datetime.datetime.now()).strftime("%Y/%m/%d %H:%M")),
        down,
        up
    ] # Create a new entry containing the time and results.
    time_now = datetime.datetime.now() # Check the time.

print(df) # Print the results to the terminal.

df.to_excel(f"results{time_now.year}-{time_now.month}-{time_now.day}-{time_now.hour}:{time_now.second}.xlsx") # Export the results to a spreadsheet.