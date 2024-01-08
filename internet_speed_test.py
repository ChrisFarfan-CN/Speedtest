# pip install speedtest-cli
# pip install pandas
# pip install openpyxl
import speedtest, datetime
import pandas as pd

duration = 10 # seconds
results = []

st = speedtest.Speedtest()

time_now = datetime.datetime.now()
target_time = time_now + datetime.timedelta(0,duration)

while datetime.datetime.now() <= target_time:
    down = st.download()
    up = st.upload()
    results.append({"yyyy mm dd hh:mm:ss":datetime.datetime.now(),"down":down,"up":up})

df = pd.DataFrame(results)
print(df.to_string())
df.to_excel("results.xlsx")