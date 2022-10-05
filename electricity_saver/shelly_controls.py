import requests
import csv

def relays_onoff(day: str, hour_now: str, hourprice: float, hourprices_asc: list):

    shelly_ip = "192.168.20.67" #your Shelly pro 4PM IP-address.

    limit_tariff_2 = 80    # Electricity price limits €/MWh (VAT 0 %) for relay two (if higher than this relay goes OFF)
    limit_tariff_3 = 160   # for relay three (if higher than this relay goes OFF)
    limit_tariff_4 = 320   # for relay four (if higher than this relay goes OFF)

    hours_on = 6  #how many hours relay one (output 1) needs to be ON (using lowest tariff's / day)

    active_hours = dict(list(hourprices_asc.items())[:hours_on])  #reduce full 24h price list to wanted nr. of hours only    

    #relay 1 is automatically activated based on lowest tariff hours defined above  
    if hour_now in active_hours:
        relay1 = requests.get(f"http://{shelly_ip}/relay/0?turn=on")
    else:
        relay1 = requests.get(f"http://{shelly_ip}/relay/0?turn=off")
  
    #relay 2 goes OFF when hourly price is more than "limit_tariff_2"/Mwh (Excl. VAT)
    if hourprice > limit_tariff_2:
        relay2 = requests.get(f"http://{shelly_ip}/relay/1?turn=off")
    else:
         relay2 = requests.get(f"http://{shelly_ip}/relay/1?turn=on")

    #relay 3 goes OFF when hourly price is more than "limit_tariff_3" €/Mwh (Excl. VAT)
    if hourprice > limit_tariff_3:
        relay3 = requests.get(f"http://{shelly_ip}/relay/2?turn=off")
    else:
        relay3 = requests.get(f"http://{shelly_ip}/relay/2?turn=on")

    #relay 4 goes OFF when hourly price is more than "limit_tariff_4" €/Mwh (Excl. VAT)
    if hourprice > limit_tariff_4:
        relay4 = requests.get(f"http://{shelly_ip}/relay/3?turn=off")
    else:
        relay4 = requests.get(f"http://{shelly_ip}/relay/3?turn=on")

    #saving relays on/off status in to variables r1, r2, r3, r4
    r1, r2, r3, r4 = (relay1.json()["ison"]), (relay2.json()["ison"]), (relay3.json()["ison"]), (relay4.json()["ison"])  
   
   # saving logs in .csv file (date, time, hour, relay status)
    log_data = [day, hour_now, r1, r2, r3, r4]

    with open("logs.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow(log_data)

    print(f"Relay 1 is ON: {r1}") 
    print(f"Relay 2 is ON: {r2}")
    print(f"Relay 3 is ON: {r3}")
    print(f"Relay 4 is ON: {r4}")
    print() 
 


    