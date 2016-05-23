#return weather infos
import json

from music_weather_influence.Core import basic_functions


def url_weather_daily(date, city):
    api_key = 'key=7116777f16944d56898110307161205'
    api_url = 'https://api.worldweatheronline.com/premium/v1/past-weather.ashx?'
    url = api_url + api_key + '&q=' + city + '&date=2016-' + date + '&tp=24&format=json'
    return url

#days group by weeks number
def calendar(week):
    return {
        14: ['04-04', '04-05', '04-06', '04-07', '04-08', '04-09', '04-10'],
        15: ['04-11', '04-12', '04-13', '04-14', '04-15', '04-16', '04-17'],
        16: ['04-18', '04-19', '04-20', '04-21', '04-22', '04-23', '04-24'],
        17: ['04-25', '04-26', '04-27', '04-28', '04-29', '04-30', '05-01'],
        18: ['05-02', '05-03', '05-04', '04-05', '04-06', '04-07', '05-08'],
        19: ['05-09', '05-10', '05-11', '04-12', '04-13', '04-14', '05-15'],
        20: ['05-16', '05-17', '05-18', '04-19', '04-20', '04-21', '05-22'],
    }[week]


def get_weather(city):
    week_list = [20,19,18,17,16,15,14]
    weather = {}
    weather["City"] = city
    for week in week_list:
        weather["week-"+str(week)] = []
        for date in calendar(week):
            url = url_weather_daily(date, city)
            data = basic_functions.get_Json_From_URL(url)
            wea_temp = data["data"]["weather"][0]["hourly"][0]["tempC"]
            wea_cloud = data["data"]["weather"][0]["hourly"][0]["cloudcover"]
            wea_descr = data["data"]["weather"][0]["hourly"][0]["weatherDesc"][0]["value"]
            weather_info = {"Date": date ,"Temperature": wea_temp, "Cloud": wea_cloud, "Description": wea_descr}
            weather["week-" + str(week)].append(weather_info)
    #print weather
    basic_functions.save_Json_To_File("../Rsc/Data/weather/", "test_json_"+city, weather)

get_weather("Geneva")
get_weather("Zurich")
get_weather("Innsbruck")
#aha