import re

def filter_raw_data(raw_data:str):
    prices = re.findall(r"<price.amount>\d+.\d+", raw_data)
    joined2 = " ".join(prices)
    filtered_prices = re.findall(r"\d+.\d+", joined2)
    return filtered_prices

def max_price(filtered_prices):
    max_price = 0
    for i in filtered_prices:
        i = float(i)
        if i > max_price:
            max_price = i
    return max_price

def min_price(filtered_prices):
    min_price = float("inf")
    for i in filtered_prices:
        i = float(i)
        if i < min_price:
            min_price = i
    return min_price

def create_hourly_prices(filtered_prices):
    h_prices = {
        "00":filtered_prices[0], 
        "01":filtered_prices[1], 
        "02":filtered_prices[2], 
        "03":filtered_prices[3],
        "04":filtered_prices[4], 
        "05":filtered_prices[5],
        "06":filtered_prices[6], 
        "07":filtered_prices[7],
        "08":filtered_prices[8], 
        "09":filtered_prices[9],
        "10":filtered_prices[10], 
        "11":filtered_prices[11],
        "12":filtered_prices[12], 
        "13":filtered_prices[13],
        "14":filtered_prices[14], 
        "15":filtered_prices[15],
        "16":filtered_prices[16],
        "17":filtered_prices[17],
        "18":filtered_prices[18],
        "19":filtered_prices[19],
        "20":filtered_prices[20],
        "21":filtered_prices[21],
        "22":filtered_prices[22],
        "23":filtered_prices[23],
        }
    return h_prices

def sort_lowest_hours(hourprices: dict):
    hourprice_in_numbers = {}
    for key, value in hourprices.items():            #value from str to float
        hourprice_in_numbers[key] = float(value)    
    lowest_hours_in_order = dict(sorted(hourprice_in_numbers.items(), key=lambda item: item[1]))    #sorting dict based on lowest values
    return lowest_hours_in_order

    

    

