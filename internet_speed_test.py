# pip install speedtest-cli
import speedtest, datetime

duration = 330 # seconds
results = []

st = speedtest.Speedtest()

time_now = datetime.datetime.now()
target_time = time_now + datetime.timedelta(0,duration)

while datetime.datetime.now() <= target_time:
    down = st.download()
    up = st.upload()
    results.append({"time":datetime.datetime.now(),"down":down,"up":up})

for result in results:
    print(result)

# st.upload(threads=threads,pre_allocate=False)
# st.results.share()

# results_dict = st.results.dict()