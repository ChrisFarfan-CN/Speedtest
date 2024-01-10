
#* First we need to install `speedtest-cli` to our virtual environment (venv) by using this command in our terminal:
# pip install speedtest-cli

#* Then we can import it!

from turtle import up
import speedtest

#* Next we need to make an empty Speedtest object:

st = speedtest.Speedtest()

#* Then we can run our tests:

down = st.download() # Returns a Float containing the number of bits/sec
upload = st.upload() # Returns a Float containing the number of bits/sec

#* Then we can do whatever we like with the results:

print(f"Download:{down/1000} Kb/s")
print(f"  Upload:{upload/1000} Kb/s")