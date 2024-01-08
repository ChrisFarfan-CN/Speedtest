# pip install speedtest-cli
from concurrent.futures import thread
import speedtest

servers = []
threads = None # `None` will 
num_of_tests = 5
time_between_tests = 60 # seconds

st = speedtest.Speedtest()
st.get_servers(servers)
st.get_best_server()

st.download(threads=threads)
# st.upload(threads=threads,pre_allocate=False)
# st.results.share()

# results_dict = st.results.dict()