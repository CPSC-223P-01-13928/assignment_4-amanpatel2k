from weather import *

BEGIN = '''\n*** TUFFY TITAN WEATHER LOGGER MAIN MENU

1. Set data filename
2. Add weather data
3. Print daily report
4. Print historical report
9. Exit the program

Enter menu choice: '''

myData = {}
myfile = 'weather.dat'

def filename(): 
    user = input('Enter the filename: ')
    myData.update(read_data(user))

def addweather():
    date = input('Enter date (YYYYMMDD): ')
    time = input('Enter time (HHMMSS): ')
    temperature = input('Enter temperature: ')
    humidity = input('Enter humidity: ')
    rainfall = input('Enter rainfall: ')
    
    weather = {
        date+time:{
            "t": temperature,
            "h": humidity,
            "r": rainfall
        }
    }

    write_data(weather, myfile); 

def daily_report():
    date = input('Enter date (YYYYMMDD): ')
    print(report_daily(myData, date))

def historical_report():
    print(report_historical(myData))

selection = {
    '1': filename,
    '2': addweather,
    '3': daily_report,
    '4': historical_report
}

def main(): 

    user = input(BEGIN)
    while user != '9': 
        if user in selection:
            func = selection[user]
            func()
        user = input(BEGIN)
main()