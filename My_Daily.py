import requests
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import date



url_1="https://news.google.com/covid19/map?hl=en-IN&mid=%2Fm%2F03rk0&gl=IN&ceid=IN%3Aen"
url_2="https://weather.com/en-IN/weather/today/l/9.97,76.31?par=google"

def covid():
    r = requests.get(url_1)
    soup1 =BeautifulSoup(r.content, 'html.parser')
    total=soup1.find_all(class_='UvMayb')
    print("   -------- Covid19 update ----------  ")
    print()
    print("Total cases in India: ",total[0].findAll(text=True))
    print()
    print("Total Deaths in India: ",total[1].findAll(text=True))
    print()
    print("Total vaccine doses given: ",total[2].findAll(text=True)," ,  Fully vaccinated people",total[3].findAll(text=True))
    print("\n")

    #      -----------Covid Report -------end------------------


#        ----------Weather Report-----------
def weather():
    r = requests.get(url_2)
    soup2 =BeautifulSoup(r.content, 'html.parser')

    temp_detail=soup2.find(class_='CurrentConditions--CurrentConditions--1swR9')
    temp=temp_detail.find(class_='CurrentConditions--tempValue--3a50n')
    detail=temp_detail.find(class_='CurrentConditions--phraseValue--2Z18W')
    prep_detail=temp_detail.find(class_='CurrentConditions--precipValue--3nxCj')


    print("\n      ---- Today's Weather ----")
    print()
    print("Current Temperature in Kochi: ",temp.findAll(text=True))
    print()
    print("               - - Sky: ",detail.findAll(text=True))
    print()
    print(" Precipitation Today ",prep_detail.findAll(text=True),"\n")

    full_detail=soup2.find(class_='WeatherTable--columns--OWgEl WeatherTable--wide--3dFXu')
    day_part=full_detail.find_all(class_='Column--column--1p659')
    part=['Morning','Afternoon','Evening','Night']
    for i in range(0,4):
        part_1_temp=day_part[i].find(class_='Column--temp--5hqI_')
        part_1_prep=day_part[i].find(class_='Column--precip--2ck8J')
        print()
        print("Today",part[i],"-> Temperature:",part_1_temp.findAll(text=True),"C")
        print("               -> Precipitation:",part_1_prep.findAll(text=True))
        print()

#- --------------------Weather Report---------end-----------

# Main

if __name__=="__main__":
    print("\n\n")
    print("    ---- Hey Good Morning Anshuman -----")
    print()
    today = date.today()
    print("Date: ",today.strftime("%B %d, %Y"))
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    print("\n")

    # Options

    covid_updates="Y"
    weather_updates="Y"
    #--------------------------

    if covid_updates in ["Y","y"]: covid()
    if weather_updates in ["Y","y"]: weather()
