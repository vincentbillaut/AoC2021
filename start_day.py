import requests
import os
from datetime import date
import browser_cookie3
import sys

#Get cookies from the browser
cj = browser_cookie3.firefox()
if not (".adventofcode.com" in str(cj)):
    cj = browser_cookie3.chrome()
    
#Get today number of day
day_today = date.today().strftime("%d").lstrip("0")

#If we provide an argument, use it as the desired day. Ex: ./startDay.py 5. Otherwise use day_today
if len(sys.argv) > 1:
    day = int(sys.argv[1])
#     if day<0 or day>31 or day>int(day_today):
#         sys.exit(f"Day is not valid ({day})")
else:
    day = day_today


print(f"Initializing day {day}")

if not os.path.exists(f"day{day}"):
    os.mkdir(f"day{day}")
    os.chdir(f"day{day}")
    r = requests.get(f"https://adventofcode.com/2021/day/{day}/input", cookies = cj)
    with open(f"input{day}","w") as f:
        f.write(r.text)