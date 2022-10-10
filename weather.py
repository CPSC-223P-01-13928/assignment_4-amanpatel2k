import json
import calendar

# Open the filename in read mode 
# Return a dictionary of the JSON decoded content of the file 
def read_data(filename): 
    try: 
        with open(filename, 'r') as f: 
            return json.load(f)
    except FileNotFoundError:
        return {}

# Write data to the file 
def write_data(data, filename): 
    with open(filename, 'w') as f: 
        return json.dump(data, f)

def max_temperature(data, date): 
    x = 0
    for key in data: 
        if date == key[0:8]: 
            if data[key]['t'] > x: 
                x = data[key]['t']
    return x
    
def min_temperature(data, date): 
    min_val = 9999
    for key in data: 
        if date == key[0:8]: 
            if data[key]['t'] < min_val: 
                min_val = data[key]['t']
    return min_val

def max_humidity(data, date): 
    max_val = 0
    for key in data: 
        if date == key[0:8]: 
            if data[key]['h'] > max_val: 
                max_val = data[key]['h']
    return max_val

def min_humidity(data, date): 
    min_val = 9999
    for key in data: 
        if date == key[0:8]: 
            if data[key]['h'] < min_val: 
                min_val = data[key]['h']
    return min_val

def tot_rain(data, date): 
    total = 0
    for key in data:
        if date == key[0:8]: 
            total += data[key]['r']
    return total 

def report_daily(data, date): 

    display =          "========================= DAILY REPORT ========================\n"
    display = display + "Date                      Time  Temperature  Humidity  Rainfall\n"
    display = display + "====================  ========  ===========  ========  ========\n"
    for key in data:
        if date == key[0:8]:
            m= calendar.month_name[int(date[4:6])] + " " + str(int(date[6:8])) + ", " + str(int(date[0:4]))
            tm= key[8:10] + ":" + key[10:12] + ":" + key[12:14] 
            t= data[key]['t']
            h=data[key]['h']
            r=data[key]['r']

            display = display + f'{m:22}{tm:8}{t:13}{h:10}{r:10.2f}\n'
    return display 

def report_historical(data): 

    display= "============================== HISTORICAL REPORT ===========================\n"
    display= display + "                          Minimum      Maximum   Minumum   Maximum     Total\n"
    display = display + "Date                  Temperature  Temperature  Humidity  Humidity  Rainfall\n"
    display = display + "====================  ===========  ===========  ========  ========  ========\n"
    current_date = ''
    for key in data: 
        if current_date != key[0:8]: 
            date = key[0:8]
            m = calendar.month_name[int(date[4:6])]+ ' ' + str(int(date[6:8])) + ', ' + str(int(date[:4]))
            min_temp = min_temperature(data, date)
            max_temp = max_temperature(data, date)
            min_humd = min_humidity(data, date)
            max_humd = max_humidity(data, date)
            total_rain = tot_rain(data, date)
            current_date = date
            display += f'{m:22}{min_temp:11}{max_temp:13}{min_humd:10}{max_humd:10}{total_rain:10.2f}\n'
       
    return display