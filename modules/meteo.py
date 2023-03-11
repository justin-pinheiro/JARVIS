import requests as rs
from time import localtime
from datetime import datetime, timedelta
import statistics as st


def roundTimeHours(dt, hours=1):
    return datetime.min+round((dt-datetime.min)/timedelta(hours=hours))*timedelta(hours=hours)


def getWeather(lat=47.39, lon=0.7, ndays=1):
    current_time = datetime(*(localtime()[0:6]))
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&timezone=CET&hourly=temperature_2m,apparent_temperature,precipitation_probability,rain,showers,snowfall,cloudcover,visibility,windspeed_10m,winddirection_10m"
    r = rs.get(url)
    units = r.json()['hourly_units']
    res = {}
    data = r.json()["hourly"]
    # try:
    # current_index = data['time'] \
    #     .index(roundTimeHours(current_time, 1)
    #            .strftime("%Y-%m-%dT%H:%M"))
    # except ValueError:
    #     raise ValueError("The api response does not contain current date.")
    data_today = {k: [v[i] for i in range(len(v)) if datetime(data['time'][i])-datetime.min > curr]#.startswith(current_time.strftime("%Y-%m-%d"))]
                  for (k, v) in data.items()}
    data_tomorow = {k: [v[i] for i in range(len(v)) if data['time'][i].startswith((current_time+timedelta(days=1)).strftime("%Y-%m-%d"))]
                  for (k, v) in data.items()}
    # data_next_24h = {k: [v[current_index:current_index+24]]
    #                 for (k, v) in data.items()}
    # print(units)
    print('\n'.join([f"{k[:4]} :\t"+'\t'.join([str(w) for w in v]) for (k, v) in data_today.items()]))
    print('\n'.join([f"{k[:4]} :\t"+'\t'.join([str(w) for w in v]) for (k, v) in data_tomorow.items()]))


    # infos on today / tomorrow
    # clouds (0-10) (10-50) (50-90) (90-100)
    # visibility (0-12k) (12k-18k) (18-25)


    # res['temperature']
    # res['precipitation'] = (data['precipitation_probability'][0], \
    #                         max(data['rain']), \
    #                         max(data['showers']), \
    #                         max(data['snowfall']))

    # print(st.mean(data['rain']), st.median(data['rain']), st.mode(data['rain']), st.stdev(data['rain']), )


def getWeatherAsSentence(lat=47.39, lon=0.7, ndays=None):
    pass


getWeather()
