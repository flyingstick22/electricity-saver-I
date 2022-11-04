# Control your home electrical loads based on day ahead electricity prices
The aim of this small Python project is to help Europeans to cope with ongoing energy crisis. This project requires basic knowledge in python and is meant for other smart home enthusiasts out there.

## Concept
The system uses simple python scripts to control [Shelly pro 4PM](https://shelly.cloud/knowledge-base/devices/shelly-pro-4pm/) relay. The relay has four 230 V outputs and each output is activated or deactivated based on hourly electricity price. Shelly relays are widely available in Europe and they do have open API and good documentation for personal projects like this.

The system default values are as follows (you can change all these values in *shelly_controls.py* for your liking):

* Output 1 is ON based on **six** lowest hourly day prices (= relay is 6 hours ON / day)<br>
* Output 2 goes OFF when electricity price (in that particular hour) is higher than 0.08 €/kWh (Excl. VAT)<br>
* Output 3 goes OFF when electricity price (in that particular hour) is higher than 0.16 €/kWh (Excl. VAT)<br>
* Output 4 goes OFF when electriciy price (in that particular hour) is higher than 0.32 €/kWh (Excl. VAT)<br>

Output one can be used for loads which needs to be xx hours per day ON but their timing is less critical. Such a loads could be, for example, electrical floor heating or water boiler. If six hours is not enough, you can easily increase the time for your liking.

All day-ahead prices are coming from [ENTSO-E transparency platform](https://transparency.entsoe.eu/) and requires an API key. The API key is free and can be requested directly from ENTSO-E via E-mail. Check preliminaries from [here](https://thesmartinsights.com/how-to-query-data-from-the-entso-e-transparency-platform-using-python/). All prices in the code are €/MWh without taxes, dealer margins or transmission costs (divide €/MWh by 1000 to get kWh prices :wink:).

## The beginning

Shelly relay needs to be installed first. In most countries 230 V installation belongs to professional so follow your country rules here. As soon as Shelly is up and running connect the relay to your home network with Ethernet cable or using WiFi. You'll also need a computer with Python plus following packages; panda, schedule, entsoe-py. 

<img src="/images/concept.jpeg">

## Code modifications

Some modifications are needed before this thing works:

1. copy the folder called **electricity_saver**  and save it to your computer. 

2. In *shelly_controls.py* --> change IP to your shelly IP-address

    ````  shelly_ip = "192.168.1.xx"  ````

    in this file you can also set price limits for outputs two, three and four and set duration (hours) for output one. Look comments in the code for more details.

3. In file called *day_ahead_prices.py* add your own API-key, change country code and time zone. Right country codes can be found from [here](https://www.entsoe.eu/data/energy-identification-codes-eic/). In this example we are using Finland.

    ```` client = EntsoeRawClient("add_your_own_entsoe_api_key_here") #Add your own API-key between " " marks   ```` 

    ```` country = "FI"              #change country code between " " marks   ```` 

    ```` tz = "Europe/Helsinki"      #change time zone between " " marks   ```` 


4. Save modified files.

## Run

Open the terminal/command prompt and navigate to project folder (cd your_path/electricity_saver). As soon as your are in the right folder execute the main.py script by writing (in terminal)

        python main.py

and press Enter. Programm starts running and you should see something like this:

<img src="/images/running.png" width="900">

In the first line, you'll see date & time, daily minimum and maximum prices and current hourly price.The script makes requests once per hour and controls relay outputs based on received price information. If output is "True" the relay is ON (= 230 V). The script also creates a file *logs.csv* in the same folder and saves relay output information as follows: [date, hour, hour price in €/MWh, hours ON with lowest tariffs, price limit2, price limit3, price limit4,  status relay1, status relay2, status relay3, status relay4].

If you do not see any price or relay information (e.g. you get error about connectivity) check possible errors:

1. API-key is wrong in the code (check typo's, make sure that the key is between " " marks)
2. Shelly IP is wrong in the code (check typo's, check that you are not using Shelly's AP IP-address)
3. Shelly is not same network with your computer (check your network settings e.g. from router)
4. No Internet for some reason (check router, check computer)


## Quit

You can stop the programm by pressing ctrl + c

## Summary

The project is in "alpha" phase and basic functions works as planned. There are lot of room for improvements (e.g. error handling and pure code improvements) and one possible future dev step cloud be cloud deployment so, that virtual machine in the cloud would handle relay controls (via Shelly's cloud API). This would remove the need for local computer. That's it for now.

Happy scripting!
















