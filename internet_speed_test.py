# pip install speedtest-cli pandas
import speedtest, datetime
import pandas as pd

duration = 300 # seconds
results = []

st = speedtest.Speedtest()

time_now = datetime.datetime.now()
target_time = time_now + datetime.timedelta(0,duration)

while datetime.datetime.now() <= target_time:
    down = st.download()
    up = st.upload()
    results.append({"time":datetime.datetime.now(),"down":down,"up":up})

df = pd.DataFrame(results)
print(df.to_string())
df.to_excel("results.xlsx")

# st.upload(threads=threads,pre_allocate=False)
# st.results.share()

# results_dict = st.results.dict()