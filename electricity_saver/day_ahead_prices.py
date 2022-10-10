import time
import pandas as pd
from entsoe import EntsoeRawClient
from datetime import datetime, timedelta
from datetime import datetime
from helpers import filter_raw_data, create_hourly_prices, min_price, max_price, sort_lowest_hours
from shelly_controls import relays_onoff


def application():

    day = datetime.today().strftime('%d-%m-%Y %H:%M:%S')
    hour_now = datetime.today().strftime('%H')
    
    data = get_prices()
    clean_data = filter_raw_data(data)
    hourprices = create_hourly_prices(clean_data)       # daily hour prices in a dictionary. Key = hour: str, value = price:str
    hourprices_asc = sort_lowest_hours(hourprices)      # hourprice dict sorted based on lowest to highest values (price)

    print(f"{day} Electricity prices today between: {min_price(clean_data)}...{max_price(clean_data)} €/MWh from {hour_now} o'clock onwards: {hourprices[hour_now]} €/MWh")
    
    # After prices known and sorted. Relay controls made with relays_onoff function
    relays_onoff(day, hour_now, float(hourprices[hour_now]), hourprices_asc)     

def get_prices():

    country = "FI"              #country code
    tz = "Europe/Helsinki"      #time zone
    
    client = EntsoeRawClient("add_your_own_API_key_here")   #add your API key between " "   

    start_date_yyyymmdd = (datetime.today() + timedelta(days=1)).strftime('%Y%m%d')
    end_date_yyyymmdd = start_date_yyyymmdd
    start = pd.Timestamp(start_date_yyyymmdd, tz=tz)
    end = pd.Timestamp(end_date_yyyymmdd, tz=tz)
    
    # Requests data from entsoe platform. If no connection with server the "for" loop keeps trying 10 times and 
    # sleep time increases exponentially 10s, 20s, 40s, 80s, 160s etc. between trials.

    tries = 10                  
    sleep = 10

    for i in range(tries):

        try:
            raw_data = client.query_day_ahead_prices(country, start, end)
            return raw_data
        
        except:
            
            if i < tries - 1: # i is zero indexed
                print(f"{datetime.today().strftime('%d-%m-%Y %H:%M:%S')} Trying to establish connection...")
                time.sleep(sleep)
                sleep *= 2
                continue
            
            else:
                raise Exception("Connection lost")
        
        break            


