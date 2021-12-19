import requests
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import date
import calendar
import re



url_1="https://news.google.com/covid19/map?hl=en-IN&mid=%2Fm%2F03rk0&gl=IN&ceid=IN%3Aen"
url_2="https://weather.com/en-IN/weather/today/l/9.97,76.31?par=google"

def covid():
    try:
        r = requests.get(url_1)
        soup1 =BeautifulSoup(r.content, 'html.parser')
        total=soup1.find_all(class_='UvMayb')
        yest=soup1.find_all(class_='tIUMlb')

        # daily_cov=re.compile(r'+\d\d\d\d')
        # daily_ded=re.compile(r'+\d\d\d')
        # tot_vacc=re.compile(r'%\d\d')

        # daily_cov=daily_cov.search(yest)
        # daily_ded=daily_ded.search(yest)
        # tot_vacc=tot_vacc.search(yest)

        print("   -------- Covid19 update ----------  ")
        print()
        print("Total cases in India: ",total[0].get_text())
        print("Covid cases",yest[0].get_text())
        print()
        print("Total Deaths in India: ",total[1].get_text())
        print("Deaths",yest[1].get_text())
        print()
        print("Total vaccine doses given: ",total[2].get_text()," ,  Fully vaccinated people",total[3].get_text())
        print("Fully vaccinated",yest[3].get_text())
        print("\n")
    except:
        print("Unable to show Covid Details")
    #      -----------Covid Report -------end------------------

def part(n):
    if n<12 and n>3:
        return("Morning")
    elif n<17 and n>=12:
        return("Afternoon")
    elif n>=17 and n<20:
        return("Evening")
    elif n>=20 and n<=24:
        return("Night")


#        ----------Weather Report-----------
def weather():
    try:
        r = requests.get(url_2)
        soup2 =BeautifulSoup(r.content, 'html.parser')

        temp_detail=soup2.find(class_='CurrentConditions--CurrentConditions--1swR9')
        temp=temp_detail.find(class_='CurrentConditions--tempValue--3a50n')
        detail=temp_detail.find(class_='CurrentConditions--phraseValue--2Z18W')
        prep_detail=temp_detail.find(class_='CurrentConditions--precipValue--3nxCj')


        print("\n      ---- Today's Weather ----")
        print()
        print("Current Temperature in Kochi: ",temp.get_text())
        print()
        print("               - - Sky:",detail.get_text())
        print()
        print(" Precipitation Today ",prep_detail.get_text(),"\n")

        full_detail=soup2.find(class_='WeatherTable--columns--OWgEl WeatherTable--wide--3dFXu')
        day_part=full_detail.find_all(class_='Column--column--1p659')
        part=['Morning','Afternoon','Evening','Overnight']
        for i in range(0,4):
            part_1_temp=day_part[i].find(class_='Column--temp--5hqI_')
            part_1_prep=day_part[i].find(class_='Column--precip--2ck8J')
            print()
            print("Today",part[i],"-> Temperature:",part_1_temp.get_text(),"C")
            print("               -> Precipitation:",(part_1_prep.span).get_text())
            print()
    except:
        print("Unable to show weather report")
        
#- --------------------Weather Report---------end-----------

# Main

if __name__=="__main__":
    today = date.today()
    now = datetime.now()
    d=part(now.hour)
    print("\n\n")
    print("    ---- Hey Good",d,"Anshuman -----")
    print()
    print("Date: ",today.strftime("%B %d, %Y"),"",calendar.day_name[today.weekday()])
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
