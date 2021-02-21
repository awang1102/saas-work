import requests
import json
from datetime import datetime

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# response = requests.get("http://api.open-notify.org/astros.json")
# print(response.json())

parameters = {
    "lat": 40.71,
    "lon": -74
}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

pass_times = response.json()['response']
# jprint(pass_times)

risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

times = []

for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)